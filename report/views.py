from django.http import JsonResponse
from report.models import Report
import random
import sys

def index(request):
    if request.method == 'POST':
        # TODO: not tested
        key = request.POST.get('key')

        if key:
            Report.objects.create(key=key)
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
