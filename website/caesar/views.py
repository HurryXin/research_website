# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
from caesar.models import BrainModule
from django.http import HttpResponse
import json


# add count module function in version 1.0
# because value will grow as button click
def caesar(request):
    image = "ae"
    if request.is_ajax():
        getvalue = request.GET.get('value')
        value = int(getvalue)
        print value
        # print type(value)
        module = BrainModule.objects.get(id=value).module
        rr = [1]
        sa = [2]
        ae = [3]
        sa_rr = [4, 7]
        ae_sa = [5, 8]
        ae_rr = [6, 9]
        ae_sa_rr = [10, 11, 12, 13, 14, 15, 16, 17, 18]
        if module in ae_sa_rr:
            image = "ae_sa_rr"
        elif module in sa_rr:
            image = "sa_rr"
        elif module in ae_sa:
            image = "ae_sa"
        elif module in ae_rr:
            image = "ae_rr"
        elif module in ae:
            image = "ae"
        elif module in sa:
            image = "sa"
        elif module in rr:
            image = "rr"
        else:
            print "error module!"

        return HttpResponse(json.dumps({"image1": 1}));
    print image
    context = {"image": image}
    # context = json.dumps(context)
    print isinstance(context, dict)
    # return render(request, 'caesar/showcaesar.html', context)
    # return HttpResponse(json.dumps({"image": image}));
    return render(request, 'caesar/showcaesar.html', {"image": json.dumps(context)})
