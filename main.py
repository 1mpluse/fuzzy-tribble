import requests

# URL для запроса к API Advice Slip
url = 'https://api.adviceslip.com/advice'

# Отправляем запрос к API Advice Slip
response = requests.get(url)

# Печатаем результат запроса
if response.status_code == 200:
    advice_data = response.json()
    advice = advice_data['slip']['advice']
    print(f"Случайный совет: {advice}")
else:
    print("Произошла ошибка при запросе к API Advice Slip")
