from django.shortcuts import render
from django.views import View


class LoginView(View):
    template_name = 'pages/login.html'

    def get(self, request):
        return render(request=request,
                      template_name=self.template_name)

    def post(self, request):
        print(request.body)
