import datetime

import requests

from lab3.constants import BASE_API_URL


def get_auditory_id(auditory_name):
    # Отримуємо JSON з переліком аудиторій
    response = requests.get(f'{BASE_API_URL}/P_API_AUDITORIES_JSON')
    auditories_data = response.json()

    for building in auditories_data['university']['buildings']:
        for auditory in building['auditories']:
            if auditory['short_name'] == auditory_name:
                return auditory['id']


def print_results(teachers, groups, auditory):
    print(f'Групи та викладачі в аудиторії {auditory} сьогодні:')

    print('*Групи*')
    print(list(map((lambda group: group['name']), groups)))
    print('\n*Викладачі*')
    print(list(map((lambda teacher: teacher['full_name']), teachers)))


def print_today_events(auditory_name):
    # Шукаємо потрібну аудиторію
    auditory_id = get_auditory_id(auditory_name)

    # Визначаємо початок та кінець сьогоднішнього дня
    start_of_day = round(datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
    end_of_day = round(datetime.datetime.today().replace(hour=23, minute=59, second=59, microsecond=999999).timestamp())

    # Складаємо рядок запиту, type_id=3 (для аудиторій)

    query = (f'https://cist.nure.ua/ias/app/tt/P_API_EVEN_JSON?type_id=3&timetable_id={auditory_id}'
        f'&time_from={start_of_day}&time_to={end_of_day}&idClient=KNURESked')

    response = requests.get(query)

    # Дістаємо JSON із відповіді
    json_data = response.json()

    teachers = json_data['teachers']
    groups = json_data['groups']

    print_results(teachers, groups, auditory_name)
