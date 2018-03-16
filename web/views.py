"""
Definiton of views.
"""
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


def home(request):
    """Renders the home"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'web/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year
        }
    )


def contact(request):
    """Renders the contact"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'web/contact.html',
        {
            'title': 'Contact',
            'year': datetime.now().year
        }
    )


def about(request):
    """Renders the contact"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'web/about.html',
        {
            'title': 'About',
            'year': datetime.now().year
        }
    )




