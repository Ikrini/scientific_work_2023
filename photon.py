import numpy as np
import math
import random

class Photon():
    def __init__(self, mua, mus, g, n1, n2, w, count, temp, status, x,y,z, ux,uy,uz, r, ai, at):
        """"initiate our photons"""
        self.mua = mua          # коэффициент поглощения
        self.mus = mus          # коэффициент рассеяния
        self.g = g              # параметр анизотропии
        self.n1 = n1            # показатель преломления внутренней среды
        self.n2 = n2            # показатель преломления внешней среды
        self.count = count      # количество фотонов
        self.w = w              # вес фотона
        self.temp = temp        # время жизни фотона
        self.status = status    # статус фотона
        self.x = x              # начальная координата положения фотона по x
        self.y = y              # начальная координата положения фотона по y
        self.z = z              # начальная координата положения фотона по z
        self.ux = ux            # текущая координата направление движения фотона по x
        self.uy = uy            # текущая координата направление движения фотона по y
        self.uz = uz            # текущая координата направление движения фотона по z
        self.r = r              # радиус цилиндра
        self.ai = ai            # угол падения
        self.at = at            # угол преломления

    def show_vars(self):
        print(f"mua = {self.mua}, mus = {self.mus}, g = {self.g}, n1 = {self.n1},"
              f"n2 = {self.n2}, count = {self.count}, w = {self.w}, temp = {self.temp},"
              f"status = {self.status}, x = {self.x}, y = {self.y}, z = {self.x},"
              f"ux = {self.ux}, uy = {self.ux}, uz = {self.ux}, r = {self.r}, ai = {self.ai}, at = {self.at}")

    def current_orient(self):
        """текущие координаты фотона"""
        self.x = 0
        self.y = 0
        self.z = 0

    def photons_direction(self):
        """"направление движение фотона"""
        self.ux = 0
        self.uy = 0
        self.uz = 1

    def photons_propagation(self):
        """"распространение фотона"""

    def reflection(self):
        """отражение фотона на границе раздела сред, имеющих разные показатели преломления"""
        if (self.at == 0):
            return pow((self.n2-self.n1)/(self.n2+self.n1), 2)
        elif

    def layer(self):
        """слой"""

    def snells_low(self, new_ai, new_at, new_n1, new_n2):
        self.ai = new_ai    # theta_1
        self.at = new_at    # theta_2
        self.n1 = new_n1    # n1
        self.n2 = new_n2    # n2
        new_ai_rad = np.radians(new_ai)
        new_at_rad = np.arcsin(new_n1 / new_n2 * np.sin(new_ai_rad))
        new_at = np.degrees(new_at_rad)
        self.at = new_at
        return self.at





