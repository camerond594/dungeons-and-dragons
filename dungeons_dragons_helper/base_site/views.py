# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render

# Create your views here.


def get_base(request):
    return render(request, 'base_site/index.html', {})
