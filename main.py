import requests

# 1) Функция для запроса случайного изображения кошки
def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data and 'url' in data[0]:
                return data[0]['url']
        return None
    except requests.RequestException:
        return None

# 2) Тестирование функции с использованием pytest

def test_successful_cat_image_request(monkeypatch):
    class MockResponse:
        status_code = 200

        @staticmethod
        def json():
            return [{"url": "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg"}]

    def mock_get(*args, **kwargs):
        return MockResponse()

    # Используем monkeypatch для замены requests.get на mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # Проверяем, что URL правильный
    result = get_random_cat_image()
    assert result == "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg"

def test_failed_cat_image_request(monkeypatch):
    class MockResponse:
        status_code = 404

        @staticmethod
        def json():
            return {}

    def mock_get(*args, **kwargs):
        return MockResponse()

    # Используем monkeypatch для замены requests.get на mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # Проверяем, что при неуспешном запросе возвращается None
    result = get_random_cat_image()
    assert result is None
