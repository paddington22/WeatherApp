1) Написаны тесты
2) Все помещено в Dockerfile
3) При повторном посещении сайта выводится информация последнего запроса
4) История пользователя доступна по кнопке "История запросов"
5) API со статистикой всех запросов доступно по кнопке "API"

Для отображения основной страницы и истории запросов был использован Django + HTML шаблоны.
Для отображения API статистики использован Django Rest Framework.\
Для работы со сторонним API использована библиотека requests.

Для запуска проекта предлагаю два варианта:
1) Cкачайте репозиторий с GitHub, распакуйте zip папку, зайдите в командную строку,
зайдите в директорию проекта.\
В моем случае(Windows) zip папка скачана в: C:\Users\МКА_136\Downloads,\
после распаковки: C:\Users\МКА_136\Downloads\test_task_ocomplex-main\test_task_ocomplex-main,\
после открытия командной строки мы находимся: C:\Users\МКА_136,\
выполняем команду: cd Downloads\test_task_ocomplex-main\test_task_ocomplex-main, 
чтобы оказаться в папке с проектом.\
Далее запустите Docker desktop, если он не был запущен предварительно,\
выполните команду docker-compose up --build,\
приложение доступно по адресу localhost:8000

2) откройте IDE, в моем случае PyCharm, создайте новый пустой проект,\
в терминале введите команду  git clone https://github.com/paddington22/test_task_ocomplex.git,  
для перехода в папку с проектом выполните команду cd test_task_ocomplex,\
запустите Docker desktop, если он не был запущен предварительно,\
выполните команду docker-compose up --build,\
приложение доступно по адресу localhost:8000