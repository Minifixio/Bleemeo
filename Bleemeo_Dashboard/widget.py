# -*- encoding: utf-8 -*-
from dashing.widgets import Widget
from random import randint

class CPUWidget(Widget):
    title = 'CPU'
    data = []

    def get_title(self):
        return self.title

    def get_cpu(self):
        return randint(0, 100)

    def get_data(self):
        return self.data

    def get_context(self):
        return {
            'title': self.get_title(),
            'cpu': self.get_cpu(),
            'data': self.get_data(),
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

class MemoryWidget(Widget):
    title = 'Memory'
    data = []

    def get_title(self):
        return self.title

    def get_memory(self):
        return randint(50, 90)

    def get_data(self):
        return self.data

    def get_context(self):
        return {
            'title': self.get_title(),
            'memory': self.get_memory(),
            'data': self.get_data(),
}
