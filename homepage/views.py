from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, TemplateView
from django.views.generic.edit import FormMixin
from .models import Device, QueryHistory
from .forms import DevicesUpdateForm
from api.models import Statistic
import requests

# Create your views here.
class HomepageTemplateView(FormMixin, TemplateView):
    model = Device
    template_name = 'homepage.html'
    form_class = DevicesUpdateForm

    def get_info(self, city):
        return requests.get('https://api.worldweatheronline.com/premium/v1/weather.ashx',
                     params={'q': city, 'num_of_days': 2, 'format': 'json', 'key': '063542f5c28548a680a181420241707', 'lang': 'ru'})

    def get_context_data(self, device_id, query=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cookie_device'] = {}
        context['cookie_device']['id'] = device_id
        context['cookie_device']['last_query'] = query

        info = self.get_info(query).json()
        if info.get('data').get('error') or info.get('data').get('area'):
            context['error'] = True
        else:
            context['error'] = False
            current_condition = info['data']['current_condition'][0]
            current_time = current_condition['observation_time'].split()
            time = int(''.join(current_time[0].split(':')))

            if current_time[1] == 'PM':
                time += 1200
            next_time = round(time // 300) + 1

            context['current_condition'] = {}
            context['current_condition']['temp'] = current_condition['temp_C']
            context['current_condition']['weather'] = current_condition['lang_ru'][0]['value']
            context['current_condition']['image'] = current_condition['weatherIconUrl'][0]['value']

            if next_time == 8:
                next_condition = info['data']['weather'][1]['hourly'][0]
            elif next_time == 9:
                next_condition = info['data']['weather'][1]['hourly'][1]
            else:
                next_condition = info['data']['weather'][0]['hourly'][next_time]

            context['next_condition'] = {}
            context['next_condition']['temp'] = next_condition['tempC']
            context['next_condition']['weather'] = next_condition['lang_ru'][0]['value']
            context['next_condition']['image'] = next_condition['weatherIconUrl'][0]['value']
        return context

    def get(self, request, *args, **kwargs):
        device_id = request.COOKIES.get('device')
        try:
            device = Device.objects.get(pk=device_id)
        except:
            device = None

        if not device:
            context = self.get_context_data(request)
            response = HttpResponse(render(request, 'homepage.html', context))
            new_device = Device.objects.create()
            response.set_cookie("device", str(new_device.id), 1000000)
        else:
            context = self.get_context_data(device_id, query=device.last_query)
            response = HttpResponse(render(request, 'homepage.html', context))
        return response

    def post(self, request, *args, **kwargs):
        device_id = request.COOKIES.get('device')
        form = self.get_form()
        if form.is_valid():
            form_info = form.cleaned_data.get('last_query').lower()
            context = self.get_context_data(request, query=form_info)
        else:
            form_info = ''
            context = self.get_context_data(request)
        device = Device.objects.get(pk=device_id)
        response = HttpResponse(render(request, 'homepage.html', context))

        if not context.get('error'):
            device.last_query = form_info
            device.save()
            QueryHistory.objects.create(device=device, query=form_info)
            if Statistic.objects.filter(city=form_info).exists():
                entry = Statistic.objects.get(city=form_info)
                entry.count += 1
                entry.save()
            else:
                Statistic.objects.create(city=form_info, count=1)
        return response

class QueryHistoryTemplateView(TemplateView):
    model = QueryHistory
    template_name = 'query_history.html'

    def get_context_data(self, device_id, **kwargs):
        context = super().get_context_data(**kwargs)
        items = QueryHistory.objects.filter(device_id=device_id)
        len_items = len(items)
        if len_items > 10:
            context['object_list'] = items[len(items)-10:len(items)-10:-1]
            context['count'] = 10
        else:
            context['object_list'] = items[::-1]
            context['count'] = len_items
        return context

    def get(self, request):
        device_id = request.COOKIES.get('device')
        context = self.get_context_data(device_id)
        response = HttpResponse(render(request, 'query_history.html', context))
        return response

