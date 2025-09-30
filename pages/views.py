from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'pages/home_page.html'


class AboutPageView(generic.TemplateView):
    template_name = 'pages/about_page.html'


class ContactPageView(generic.TemplateView):
    template_name = 'pages/contact_page.html'
