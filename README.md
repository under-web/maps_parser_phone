# maps_parser_phone

*Парсит из GoogleMaps название организации,номер телефона, сайт. А а так же сохраняет все это в файл CSV.*

## Зависимости

Должет быть установлен на компьютере Firefox!

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

![Альтернативный текст](https://github.com/under-web/maps_parser_phone/blob/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA.PNG)

