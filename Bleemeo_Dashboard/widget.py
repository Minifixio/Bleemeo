# -*- encoding: utf-8 -*-
from dashing.widgets import Widget
from random import randint
import requests
from django.conf import settings


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

class MeteoWidget(Widget):
    title = 'Meteo'
    data = []

    def get_title(self):
        return self.title

    def get_data(self):
        return self.data

    def get_number(self):
        return randint(50, 90)

    def get_context(self):
        return {
            'title': self.get_title(),
            'data': self.get_data(),
            'cpu': self.get_number(),
}
