import requests

BASE_URL = "https://postman-echo.com"


# GET-запрос: проверка передачи параметров в URL
def test_get_query_params():
    url = f"{BASE_URL}/get"
    params = {"name":"Andrey", "course": "QA"}

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.json()["args"] == params

# POST-запрос: проверка отправки обычного текста в теле запроса
def test_post_raw_text():
    url = f"{BASE_URL}/post"
    text_data = ("Что вершит судьбу человечества? Некое незримое существо или закон? … "
                 "Человек не властен даже над своей волей")

    response = requests.post(url, data=text_data)

    assert response.status_code == 200
    assert response.json()["data"] == text_data

# POST-запрос: проверка отправки данных в формате JSON
def test_post_json():
    url = f"{BASE_URL}/post"
    payload = {"name": "Andrey", "course": "QA"}

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert response.json()["json"] == payload

# PUT-запрос: проверка обновления данных текстом в кодировке UTF-8
def test_put_raw_text():
    url = f"{BASE_URL}/put"
    payload = ("""В этом мире нет ни правды, ни лжи. Есть только факты.
               И по ошибке мы верим лишь тем фактам, которые нам нравятся.
               Другого способа жить мы не знаем. А те, кому не нравится, что это факты — принимают их за истину.
               Так мы и входим в заблуждение.""")
    response = requests.put(url, data=payload.encode('utf-8'))

    assert response.status_code == 200
    assert response.json()["data"] == payload

# GET-запрос: проверка передачи пользовательских заголовков (headers)
def test_custom_headers():
    url = f"{BASE_URL}/get"
    headers = {"Custom-Header": "QA-Auto-Test"}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json()["headers"]["custom-header"] == "QA-Auto-Test"