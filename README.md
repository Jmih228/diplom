В проекте представлена авторизация пользователя по коду, отправленному на номер телефона.
Авторизация реализована похожим образом с jwt токенами, т.е. делаем запрос на один url для получения
кода и передаем его в headers проекта со значениями key=Authorization и value=SMS_code ваш код.
Отправка смс сымитирована выводом кода в терминале в ответ на запрос на соответствующий эндпоинт.
Также реализована задача инвайт кодов. После первой авторизации каждый пользователь получает себе
в профиль случайно сгенерированный инвайт код. Также можно ввести инвайт код другого пользователя.
В профиле пользователя выводятся номера телефонов от людей, активировавших инвайт код текущего пользователя.
Реализована документация через Swagger и ReDoc.
Суперюзер создается через кастомную команду "python manage.py csu".

Для начала работы с проектом:
1) Клонируйте себе репозиторий, расположенный по ссылке https://github.com/Jmih228/diplom310.
2) Заполните переменные окружения, определенные в .env.sample.
3) Создайте базу данных и заполните ее из файла data.json.
4) Установите зависимости и примените миграции.
5) Запустите сервер.
