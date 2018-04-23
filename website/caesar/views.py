# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
from caesar.models import BrainModule, Quota
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
        predict = BrainModule.objects.get(id=value).predict
        if not predict:
            predict = "correct"
        else:
            predict = "fake"
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

        recall = round(Quota.objects.get(id=value).recall, 2)
        disturb = round(Quota.objects.get(id=value).disturb, 2)
        precision = round(Quota.objects.get(id=value).precision, 2)
        accuracy = round(Quota.objects.get(id=value).accuracy, 2)

        # print "recall:"+str(recall)+" disturb:"+str(disturb)+" precision:"+str(precision)+" accuracy:"+str(accuracy)
        # title1 = 100
        # title2 = 100
        # title3 = 100
        return HttpResponse(json.dumps({"module": image, "predict": predict, "recall": recall, "disturb": disturb, "precision":precision, "accuracy": accuracy}));
    print image
    context = {"image": image}
    # context = json.dumps(context)
    print isinstance(context, dict)
    # return render(request, 'caesar/showcaesar.html', context)
    # return HttpResponse(json.dumps({"image": image}));
    return render(request, 'caesar/showcaesar.html', {"image": json.dumps(context)})
