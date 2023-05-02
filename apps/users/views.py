import json

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from apps.users.models import User
from utils.validation import check_registration_data


class LoginView(View):
    template_name = 'pages/login.html'

    def get(self, request):
        return render(request=request,
                      template_name=self.template_name)

    def post(self, request):
        data = json.loads(request.body.decode())
        user = User.objects.filter(phone_number=data.get('phoneNumber')).first()

        if user:
            if not user.check_password(data.get('password')):
                return JsonResponse(
                    {'detail': {'password': 'incorrect'}}, status=200
                )

            login(request, user)
            return JsonResponse({'detail': 'success'}, status=200)

        return JsonResponse({'detail': {'user': 'not found'}}, status=200)


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)

        return HttpResponseRedirect(reverse('movie_list'))


class RegistrationView(View):
    template_name = 'pages/registration.html'

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        data = json.loads(request.body.decode())
        if not data.get('password'):
            return JsonResponse({'detail': {'password': 'empty'}})
        if not data.get('repeatPassword'):
            return JsonResponse({'detail': {'repeatPassword': 'empty'}})
        if data.get('password') != data.get('repeatPassword'):
            return JsonResponse({'detail': {'password': 'not match'}})
        if len(data.get('password')) < 7:
            return JsonResponse(
                {'detail': {'password': 'password length less 6 symbols'}})

        if not data.get('phoneNumber'):
            return JsonResponse({'detail': {'phoneNumber': 'empty'}})

        if not data.get('firstName'):
            return JsonResponse({'detail': {'firstName': 'empty'}})

        if not data.get('lastName'):
            return JsonResponse({'detail': {'lastName': 'empty'}})

        return JsonResponse({'detail': 'success'}, status=201)
