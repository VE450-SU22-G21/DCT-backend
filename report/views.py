from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from report.models import Report
import random
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView

@csrf_exempt
def index(request):
    # Report.objects.all().delete()
    if request.method == 'POST':
        # key = request.POST.get('key')
        imported_keys = json.loads(request.body)["key"]
        if imported_keys:
            objs = [Report(key=item) for item in imported_keys]
            Report.objects.bulk_create(objs)
            return JsonResponse({ 'postkeys': imported_keys },safe=False)
        return JsonResponse({ 'error': 'key not found in data' }, status=400)

    if request.method == 'GET':
        keys = Report.objects.values('key')
        return JsonResponse({ 'getkeys': list(map(lambda x:x['key'], keys)) })

    return JsonResponse({ 'error': 'method not supported' }, status=405)


def fake(request):
    rand_key = random.randint(0, 2147483648)
    Report.objects.create(key=rand_key)
    return JsonResponse({ 'key': rand_key }, status=201)
