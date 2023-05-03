# Отримуємо JSON з розкладом групи за допомогою запиту GET
from datetime import datetime

import requests

response = requests.get('https://cist.nure.ua/ias/app/tt/P_API_EVEN_JSON?type_id=3&timetable_id=56&idClient=KNURESked')

# Дістаємо JSON із резпонзу
json_data = response.json()

teachers = [teacher for teacher in json_data['teachers']]
groups = [groups for groups in json_data['groups']]


def get_today_events():
    events = json_data['events']

    today = datetime.date.today().strftime('%Y-%m-%d')

    events_today = []
    for event in events:
        if datetime.date.fromtimestamp(event['start_time']).strftime('%Y-%m-%d') == today:
            events_today.append(event)

    return events_today


# Функція для конвертування timestamp у datetime
def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)


# Функція для виведення подій за добу
def print_schedule_by_day():
    today = datetime.date.today().strftime('%Y-%m-%d')

    print('Групи та викладачі в аудиторії 309і у: ', today)
    events = get_today_events()
    for event in events:
        for teacher in event['teachers']:
            print(get_teacher_by_id(teacher))
        for group in event['groups']:
            print(get_group_by_id(group))


def get_teacher_by_id(id):
    for teacher in teachers:
        if teacher['id'] == id:
            return teacher['full_name']


def get_group_by_id(id):
    for group in groups:
        if group['id'] == id:
            return group['name']


print_schedule_by_day()
