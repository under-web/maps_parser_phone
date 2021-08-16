# maps_parser_phone

*Парсит из GoogleMaps название организации, категорию, номер телефона, сайт. А а так же сохраняет все это в файл CSV.*

## Зависимости

>Должет быть установлен на компьютере Firefox!

Работает для 64х-разрядных систем. Для 32-х битных качаем [здесь](https://github.com/mozilla/geckodriver/releases) geckodriver
удаляем исходный вставляем в папку с проектом который скачали.

```
pip install -r requirements.txt
```

## Запуск

```
python parser_google_org.py
```
### Примечание
Решение для скрытия консоли  geckodriver.exe
\ AppData \ Roaming \ Python \ Python38 \ site-packages \ selenium \ webdriver \ common \ service.py

![Альтернативный текст](https://github.com/under-web/maps_parser_phone/blob/main/selenium_in_venv.PNG)


*Так же перед компиляцией в exe через pyinstaller помогло решение с изменением selenium в (venv) lib*


![Альтернативный текст](https://github.com/under-web/maps_parser_phone/blob/main/selenium.PNG)
