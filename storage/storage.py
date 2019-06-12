import numpy as np


class Detail:
    def __init__(self, contour):
        self.contour = contour

class Product:
    def __init__(self):
        self.details = [] # детали
        self.optimal_composition = None # оптимальное разложение

class Storage:
    def __init__(self):
        self.storage = [] # проекты

    def add_new_detail(self, detail):
        self.storage.append(detail)