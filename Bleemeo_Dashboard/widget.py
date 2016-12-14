# -*- encoding: utf-8 -*-
from dashing.widgets import Widget
from random import randint

cpu = randint(0, 100)


"""class NewClientsWidget(NumberWidget):
    title = 'CPU'

    def get_value(self):
        global users
        users = randint(0, 100)
        return users

    def get_detail(self):
        global users

    def get_more_info(self):
        global users"""

class NewClientsWidget(Widget):
    title = 'CPU'

    def get_title(self):
        return self.title

    def get_cpu(self):
        return randint(0, 100)

    def get_context(self):
        return {
            'title': self.get_title(),
            'cpu': self.get_cpu(),
        }
