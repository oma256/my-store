from django.http import JsonResponse


def check_registration_data(data: dict):
    print(len(data.get('phoneNumber')))

