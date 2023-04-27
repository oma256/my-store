import json

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from apps.users.models import User


class LoginView(View):
    template_name = 'pages/login.html'

    def get(self, request):
        return render(request=request,
                      template_name=self.template_name)

    def post(self, request):
        data = json.loads(request.body.decode())
        user = User.objects.filter(phone_number=data.get('phoneNumber')).first()

        if user:
            login(request, user)
            return JsonResponse({'detail': 'success'}, status=200)

        return JsonResponse({'detail': 'failed'}, status=400)


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
        print(data)

        return JsonResponse({'detail': 'success'}, status=201)
