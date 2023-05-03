import datetime
import calendar
import requests
import constants

BASE_API_URL = constants.BASE_API_URL


# Функція для конвертування timestamp у datetime
def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)


def find_group_id(group_name):
    # Отримуємо JSON з переліком груп
    response = requests.get(f'{BASE_API_URL}/P_API_GROUP_JSON')
    groups_data = response.json()

    for faculty in groups_data['university']['faculties']:
        for direction in faculty['directions']:
            print('[direction]', direction)
            for speciality in direction['specialities']:
                for group in speciality['groups']:
                    if group['name'] == group_name:
                        return group['id']
            if 'groups' in direction:
                print('groups in direction')
                for group in direction['groups']:
                    print('[group]', group)
                    if group['name'] == group_name:
                        return group['id']


def get_subject_by_id(id, subjects):
    for subject in subjects:
        if subject['id'] == id:
            return subject['brief']


def print_schedule_by_day(group_name, day):
    group_id = find_group_id(group_name)

    # Отримуємо JSON з розкладом групи за допомогою запиту GET
    response = requests.get(f'{BASE_API_URL}/P_API_EVEN_JSON?type_id=1&timetable_id={group_id}&idClient=KNURESked')

    # Розпаковуємо JSON із відповіді
    json_data = response.json()

    # Знаходимо всі пари, що належать до групи
    group_events = [event for event in json_data['events'] if group_id in event['groups']]
    subjects = [subject for subject in json_data['subjects']]

    print('Розклад занять групи за', day.strftime('%d.%m.%Y'))
    for event in group_events:
        event_start_time = timestamp_to_datetime(event['start_time'])
        event_end_time = timestamp_to_datetime(event['end_time'])
        if event_start_time.date() == day.date():
            name_subject = get_subject_by_id(event['subject_id'], subjects)
            print(
                f"{event['number_pair']} пара: {event['auditory']}, {name_subject}, {event_start_time.strftime('%H:%M')} - {event_end_time.strftime('%H:%M')}")


#
# Функція для виведення розкладу за тиждень
def print_schedule_by_week(group_name, week):
    group_id = find_group_id(group_name)

    week_start = week - datetime.timedelta(days=week.weekday())
    week_end = week_start + datetime.timedelta(days=6)

    # Отримуємо JSON з розкладом групи за допомогою запиту GET
    response = requests.get(f'{BASE_API_URL}/P_API_EVEN_JSON?type_id=1&timetable_id={group_id}&idClient=KNURESked')

    # Розпаковуємо JSON із відповіді
    json_data = response.json()

    # Знаходимо всі пари, що належать до групи
    group_events = [event for event in json_data['events'] if group_id in event['groups']]
    subjects = [subject for subject in json_data['subjects']]

    print('Розклад занять групи на тиждень (', week_start.strftime('%d.%m.%Y'), ' - ', week_end.strftime('%d.%m.%Y'), ')')
    for event in group_events:
        event_start_time = timestamp_to_datetime(event['start_time'])
        event_end_time = timestamp_to_datetime(event['end_time'])
        if week_start.date() <= event_start_time.date() <= week_end.date():
            name_subject = get_subject_by_id(event['subject_id'], subjects)
            print(
                f"{event['number_pair']} пара: {event['auditory']}, {nameSubject}, {event_start_time.strftime('%d.%m.%Y %H:%M')} - {event_end_time.strftime('%H:%M')}")

#
# # Функція для виведення розкладу за місяць
# def print_schedule_by_month(month):
#     month_start = datetime.datetime(month.year, month.month, 1)
#     month_end = datetime.datetime(month.year, month.month, calendar.monthrange(month.year, month.month)[1])
#     print('Розклад занять групи за', month_start.strftime('%B %Y'))
#     for event in group_events:
#         event_start_time = timestamp_to_datetime(event['start_time'])
#         event_end_time = timestamp_to_datetime(event['end_time'])
#         if month_start.date() <= event_start_time.date() <= month_end.date():
#             nameSubject = get_subject_by_id(event['subject_id'])
#             print(
#                 f"{event['number_pair']} пара: {event['auditory']}, {nameSubject}, {event_start_time.strftime('%d.%m.%Y %H:%M')} - {event_end_time.strftime('%H:%M')}")
#
#
# day = datetime.datetime(2023, 3, 10)
# week = datetime.datetime(2023, 3, 13)
# month = datetime.datetime(2023, 3, 1)
# print_schedule_by_week(week)
# print_schedule_by_month(month)
