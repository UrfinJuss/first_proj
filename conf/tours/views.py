from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    return render(request, 'tours/departur.html')


def tour_view(request, id):
    return render(request, 'tours/tour.html')


def custom_handler400(request, exception):
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
