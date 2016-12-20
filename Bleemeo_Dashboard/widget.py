# -*- encoding: utf-8 -*-
from dashing.widgets import Widget
from random import randint
from django.conf import settings

import requests
import datetime


class CPUWidget(Widget):
    title = 'CPU'
    data = []

    def get_title(self):
        return self.title

    def get_cpu(self):
        r = requests.get(settings.BLEEMEO_CPU_URL, auth=(settings.BLEEMEO_USER, settings.BLEEMEO_PASSWORD))
        return r.json()['values'][-1]['value']

    def get_data(self):
        return self.data

    def get_context(self):
        return {
            'data': {'title': self.get_title(),'value': self.get_cpu()},
}

class MemoryWidget(Widget):
    title = 'Memory'
    data = []

    def get_title(self):
        return self.title

    def get_memory(self):
        r = requests.get(settings.BLEEMEO_MEMORY_URL, auth=(settings.BLEEMEO_USER, settings.BLEEMEO_PASSWORD))
        return r.json()['values'][-1]['value']

    def get_cpu(self):
        return self.data

    def get_context(self):
        return {
            'data': {'title': self.get_title(),'value': self.get_memory()},
}

class LoadWidget(Widget):
    title = 'Load'
    data = []

    def get_title(self):
        return self.title

    def get_load(self):
        r = requests.get('https://panel.bleemeo.com/v1/metric/04d6e237-d3ca-41a2-9b75-6d0c08d5b991/data/', auth=(settings.BLEEMEO_USER, settings.BLEEMEO_PASSWORD))

        minValue = 1000
        maxValue = 0
        nb = 0
        somme = 0


        for loadValue in r.json()['values'] :
            value = loadValue['value']

            nb += 1
            somme += value

            if value < minValue :
                minValue = value

            if value > maxValue :
                maxValue = value

        average = float("{0:.2f}".format(somme/nb))

        return {'minValue': minValue,'maxValue': maxValue, "average" : average}


    def get_context(self):
        return {
            'data': {'title': self.get_title(),'value': self.get_load()},
}

class MeteoWidget(Widget):
    title = 'Meteo'
    data = []

    def get_title(self):
        return self.title

    def get_city(self):
        r = requests.get(settings.METEO_URL)
        return r.json()['city']['name']

    def get_temp(self):
        r = requests.get(settings.METEO_URL)
        tempMin = r.json()['list'][0]['main']['temp_min']
        tempMax = r.json()['list'][0]['main']['temp_max']
        return {'tempMin' : tempMin, 'tempMax': tempMax}

    def get_time(self):
        r = requests.get(settings.METEO_URL)

        time1 = datetime.datetime.fromtimestamp(
                    int(r.json()['list'][0]['dt'])
                ).strftime('%H:%M')
        time2 = datetime.datetime.fromtimestamp(
                    int(r.json()['list'][1]['dt'])
                ).strftime('%H:%M')
        time3 = datetime.datetime.fromtimestamp(
                    int(r.json()['list'][2]['dt'])
                ).strftime('%H:%M')

        return {'time1' : time1, 'time2': time2, 'time3': time3}

    def get_tempImg(self):
        r = requests.get(settings.METEO_URL)
        img1 = 'http://openweathermap.org/img/w/' + r.json()['list'][0]['weather'][0]['icon'] + '.png'
        img2 = 'http://openweathermap.org/img/w/' + r.json()['list'][1]['weather'][0]['icon'] + '.png'
        img3 = 'http://openweathermap.org/img/w/' + r.json()['list'][2]['weather'][0]['icon'] + '.png'
        return {'img1': img1,'img2': img2, "img3" : img3}


    def get_context(self):
        return {
            'data': {'title': self.get_title(),'temp': self.get_temp(), 'city' : self.get_city(), 'tempImg' : self.get_tempImg(), 'time': self.get_time()},

}
