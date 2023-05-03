import json

import requests


def getAllFaculties():
    # Виконуємо GET-запит для отримання списку кафедр та їх викладачів з веб-ресурсу
    response = requests.get('https://cist.nure.ua/ias/app/tt/P_API_PODR_JSON')

    # Перевіряємо, чи був виконаний запит успішно (статус код 200)
    if response.status_code == 200:
        # Отримуємо дані у форматі JSON
        text = response.text
        text = text[:len(text) - 2] + "]}}"

        data = json.loads(text)

        # Нижче виведемо список усіх кафедр університету
        for faculty in data['university']['faculties']:
            for department in faculty['departments']:
                print(department['full_name'], department['short_name'])
    else:
        print('Помилка при виконанні запиту:', response.status_code)
