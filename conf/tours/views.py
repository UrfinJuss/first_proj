import random

from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound,\
    HttpResponseForbidden, HttpResponseServerError

from .data import tours, title, subtitle, description, departures



def main_view(request):
    random_tours = dict(random.sample(tours.items(), 6))
    return render(request, 'index.html', context={
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'tours': random_tours,

    })


def departure_view(request, departure):
    if departure not in departures:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    dep_tours = {}
    for tour_id, tour_name in tours.items():
        if tour_name['departure'] == departure:
            dep_tours[tour_id] = tour_name
    list_prices, list_days, list_test = [], [], [i for i in dep_tours.values()]
    for i in range(len(list_test)):
        list_prices.append(list_test[i]['price'])
        list_days.append(list_test[i]['nights'])
    list_prices.sort(), list_days.sort()
    return render(request, 'departur.html', context={
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'dep_tours': dep_tours,
        'departure': departures[departure],
        'maxprice': list_prices[len(list_test) - 1],
        'minprice': list_prices[0],
        'maxday': list_days[len(list_test) - 1],
        'minday': list_days[0],

    })


def tour_view(request, id):
    if id not in tours:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'tour.html', context={
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
