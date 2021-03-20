from .data import departures


def statistic(request):
    return {'departures': departures}
