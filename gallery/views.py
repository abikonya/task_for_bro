from django.shortcuts import render
from django.views.generic import TemplateView
from gallery.models import Images


class Main(TemplateView):
    template_name = 'main.html'
    login_template = 'enter_form.html'

    def get(self, request):
        ctx = dict()
        ctx['images'] = Images.objects.all()
        return render(request, self.template_name, ctx)