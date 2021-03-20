from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from .data import tours, title, subtitle, description, departures
import random


def main_view(request):
    return render(request, 'index.html', context={
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'tours': tours,

    })


def departure_view(request, departure):
    random_tours = dict(random.sample(tours.items(), 6))
    list_prices = []
    list_days = []
    list_test = [i for i in random_tours.values()]
    for i in range(6):
        list_prices.append(list_test[i]['price'])
        list_days.append(list_test[i]['nights'])
    list_prices.sort(), list_days.sort()
    return render(request, 'departur.html', context={
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'random_tours': random_tours,
        'departure': departures[departure],
        'maxprice': list_prices[5],
        'minprice': list_prices[0],
        'maxday': list_days[5],
        'minday': list_days[0],

    })


def tour_view(request, id):
    return render(request, 'tour.html', context={
        'departures': departures,
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'tours': tours[id],

    })


def custom_handler400(request, exception):
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
