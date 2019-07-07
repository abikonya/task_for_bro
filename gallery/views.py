from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.contrib.auth import login, logout
from gallery.models import Images, Settings
from django.forms import ClearableFileInput
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm

from PIL import ImageMode


class Main(TemplateView):
    template_name = 'main.html'
    login_template = 'enter_form.html'

    def get(self, request, page):
        ctx = dict()
        images = Images.objects.all()
        number_displayed = int(Settings.objects.all().latest('created').number_displayed)
        if images.count() >= number_displayed:
            total_pages = images.count() // number_displayed + images.count() % number_displayed
            ctx['pages'] = [x+1 for x in range(total_pages)]
            if page == 1:
                ctx['images'] = images[:number_displayed]
            else:
                ctx['images'] = images[(int(page)*number_displayed)-number_displayed:int(page)*number_displayed]
        else:
            ctx['images'] = images
        if request.user.is_authentificated:
            load_form = ClearableFileInput()
            ctx['load_form'] = load_form.render(name='upload', value='Upload')
        return render(request, self.template_name, ctx)

    def post(self, request):
        pass


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = 'enter_form.html'

    success_url = '/test_task/1'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/test_task/login')


def redirect(request):
    return HttpResponseRedirect('/test_task/1')

