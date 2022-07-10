import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from report.models import Report
import random
from django.shortcuts import render

@csrf_exempt
def index(request):
    if request.method == 'POST':
        imported_keys = json.loads(request.body)['keys']
        if imported_keys:
            objs = [Report(key=item) for item in imported_keys]
            Report.objects.bulk_create(objs)
            return JsonResponse({ 'message ': 'created' }, status = 201)
        return JsonResponse({ 'error': 'keys not found in data' }, status=400)

    if request.method == 'GET':
        keys = Report.objects.values('key')
        return JsonResponse({ 'keys ': list(map(lambda x:x['key'], keys)) })

    return JsonResponse({ 'error': 'method not supported' }, status=405)


def fake(request):
    rand_key = random.randint(0, 2147483648)
    Report.objects.create(key=rand_key)
    return JsonResponse({ 'key': rand_key }, status=201)
