# Отримуємо JSON з розкладом групи за допомогою запиту GET
from datetime import time

import requests

from lab3.task2 import get_subject_by_id, timestamp_to_datetime

response = requests.get('https://cist.nure.ua/ias/app/tt/P_API_EVEN_JSON?type_id=1&timetable_id=8476450&idClient=KNURESked')

# Розпаковуємо JSON із відповіді
json_data = response.json()

# Знаходимо всі пари, що належать до групи
group_events = [event for event in json_data['events'] if 8476450 in event['groups']]

# Функція перевірки змін у розкладі та їх друку
def check_schedule_changes():
    # Зробіть новий запит, щоб отримати найсвіжіші дані розкладу
    response = requests.get('https://cist.nure.ua/ias/app/tt/P_API_EVEN_JSON?type_id=1&timetable_id=8476450&idClient=KNURESked')
    json_data = response.json()

    # Знайти всі події, які належать до групи
    new_group_events = [event for event in json_data['events'] if 8476450 in event['groups']]

    # Знайти події, які були додані або видалені з моменту останньої перевірки
    added_events = [event for event in new_group_events if event not in group_events]
    removed_events = [event for event in group_events if event not in new_group_events]

    # Оновити список подій групи новими даними
    group_events.clear()
    group_events.extend(new_group_events)

    # Вивести зміни в консоль
    if added_events:
        print('New events:')
        for event in added_events:
            nameSubject = get_subject_by_id(event['subject_id'])
            event_start_time = timestamp_to_datetime(event['start_time'])
            event_end_time = timestamp_to_datetime(event['end_time'])
            print(f"{event['number_pair']} пара: {event['auditory']}, {nameSubject}, {event_start_time.strftime('%H:%M')} - {event_end_time.strftime('%H:%M')}")
        print('')

    if removed_events:
        print('Removed events:')
        for event in removed_events:
            nameSubject = get_subject_by_id(event['subject_id'])
            event_start_time = timestamp_to_datetime(event['start_time'])
            event_end_time = timestamp_to_datetime(event['end_time'])
            print(f"{event['number_pair']} пара: {event['auditory']}, {nameSubject}, {event_start_time.strftime('%H:%M')} - {event_end_time.strftime('%H:%M')}")
        print('')

# Основний цикл, який запускає функцію check_schedule_changes() щохвилини
group_events = []
while True:
    check_schedule_changes()
    time.sleep(60)
