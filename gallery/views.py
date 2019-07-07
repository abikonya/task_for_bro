from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.contrib.auth import login, logout
from gallery.models import Images, Settings
from django.forms import FileInput
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm

from PIL import ImageMode


class Main(TemplateView):
    template_name = 'main.html'
    login_template = 'enter_form.html'

    def get(self, request, page):
        ctx = dict()
        settings = Settings.objects.all().latest('created')
        if settings.method == 'RND':
            images = Images.objects.all()
        elif settings.method == 'D':
            images = Images.objects.all().order_by('created')
        else:
            images = Images.objects.all().order_by('name')
        number_displayed = int(settings.number_displayed)
        if images.count() >= number_displayed:
            total_pages = int(images.count() // number_displayed + images.count() / number_displayed)
            ctx['pages'] = [x+1 for x in range(total_pages)]
            if page == 1:
                ctx['images'] = images[:number_displayed]
            else:
                ctx['images'] = images[(int(page)*number_displayed)-number_displayed:int(page)*number_displayed]
        else:
            ctx['images'] = images
        if request.user.is_authenticated:
            load_form = FileInput()
            max_photos_to_upload = [x for x in range(10)]
            all_forms = []
            for each in max_photos_to_upload:
                name = 'upload' + str(each)
                value = 'Upload' + str(each)
                all_forms.append(load_form.render(name=name, value=value))
            ctx['all_forms'] = all_forms
        return render(request, self.template_name, ctx)

    def post(self, request, *args):
        for each in request.FILES:
            file = request.FILES[each]
            new_image = Images(tags=request.POST.get('tags'), image=file)
            new_image.save()
        return HttpResponseRedirect('/test_task/')


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

