# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
# import json


# @require_http_method(["GET"])
# @csrf_token
def caesar(request):
    if request.is_ajax():
        value = request.GET.get('value')
        print value
        print type(value)
        test = int(value)
        print test
        print isinstance(test,int)



    image1 = "Ae"
    context = {'image': image1,}
    return render(request, 'caesar/showcaesar.html', context)
