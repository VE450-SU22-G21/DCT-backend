from datetime import datetime
import json

from django.http import JsonResponse
from report.models import Report
import random
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView


def index(request):
    if request.method == 'POST':
        # TODO: not tested
        key = request.POST.get('key')
        imported_keys = ['k1', 'k2', 'k3', 'k4', 'k5']
        # imported_keys = json.loads(request.body)['key']
        if key:
            objs = [Report(key=item) for item in imported_keys]
            Report.objects.bulk_create(objs)
            return JsonResponse({ 'key': key }, status=201)
        return JsonResponse({ 'error': 'key not found in data' }, status=400)

    if request.method == 'GET':
        keys = Report.objects.values('key')
        return JsonResponse({ 'keys': list(map(lambda x:x['key'], keys)) })

    return JsonResponse({ 'error': 'method not supported' }, status=405)


def fake(request):
    rand_key = random.randint(0, 2147483648)
    Report.objects.create(key=rand_key)
    return JsonResponse({ 'key': rand_key }, status=201)


class test_post(ListView):
    Report.objects.all().delete()

    model = Report
    template_name = 'test_index_post.html'
    queryset = Report.objects.all()
    # if not queryset.exists():
    imported_keys = ['k1','k2','k3','k4','k5']
    objs = [Report(key=item) for item in imported_keys]
    Report.objects.bulk_create(objs)

    def get_query_all(self):
        return Report.objects.all()