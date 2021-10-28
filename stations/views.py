from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from stations.csv_reader import read_csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stations_list = read_csv(BUS_STATION_CSV)
    page_number = request.GET.get('page', 1)
    element_per_page = 10
    paginator = Paginator(stations_list, element_per_page)
    page = paginator.get_page(page_number)
    context = {'bus_stations': page.object_list,
               'page': page
    }
    return render(request, 'stations/index.html', context)
