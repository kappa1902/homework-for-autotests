import requests

BASE_URL = "https://postman-echo.com"

def test_get_query_params():
    url = f"{BASE_URL}/get"
    params = {"name":"Andrey", "course": "QA"}

    response = requests.get(url, params=params)

    assert response.status_code == 400
    assert response.json()["args"] == params


def test_post_raw_text():
    url = f"{BASE_URL}/post"
    text_data = ("Что вершит судьбу человечества? Некое незримое существо или закон? … "
                 "Человек не властен даже над своей волей")

    response = requests.post(url, data=text_data)

    assert response.status_code == 200
    assert response.json()["data"] == text_data


def test_post_json():
    url = f"{BASE_URL}/post"
    payload = {"name": "Andrey", "course": "QA"}

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert response.json()["json"] == payload


def test_put_raw_text():
    url = f"{BASE_URL}/put"
    payload = ("""В этом мире нет ни правды, ни лжи. Есть только факты.
               И по ошибке мы верим лишь тем фактам, которые нам нравятся.
               Другого способа жить мы не знаем. А те, кому не нравится, что это факты — принимают их за истину.
               Так мы и входим в заблуждение.""")
    response = requests.put(url, data=payload.encode('utf-8'))
    assert response.status_code == 200
    assert response.json()["data"] == payload


def test_custom_headers():
    url = f"{BASE_URL}/get"
    headers = {"Custom-Header": "QA-Auto-Test"}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json()["headers"]["custom-header"] == "QA-Auto-Test"