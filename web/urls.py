from datetime import datetime
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from web import views, forms

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^login/$',
        login,
        {
            'template_name': 'web/login.html',
            'authentication_form': forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Log in',
                    'year': datetime.now().year
                }
        },
        name='login'
        ),
    url('^logout/$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),
]
