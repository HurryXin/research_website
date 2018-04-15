# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader


def caesar(request):
    context = {}
    return render(request, 'caesar/showcaesar.html', context)
