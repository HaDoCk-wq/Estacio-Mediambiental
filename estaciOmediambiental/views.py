from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
import json


class test(View):
    def get(self, request):
        context = {
            'reservas': "reservas",
            'user': "request"
        }
        return render(request, 'test.html', context)


class xhr(View):
    def post(self, request):
        dades = json.loads(request.body.decode("utf-8"))
        data = {
            'like': dades["like"],
            'post': dades["post"],
        }
        return JsonResponse(data)


class dades(View):
    def get(self, request):
        context = {
            'reservas': "reservas",
            'user': "request",
        }
        return render(request, 'dades.html', context)
