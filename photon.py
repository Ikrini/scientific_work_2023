import numpy as np
import math
import random

class Photon():
    def __init__(self, mua, mus, g, boundary, n1, n2, w, count, temp, status, current, direction, r, ai, at, l_run, dz, dr, mut, albedo, nz, nr, atot, f):
        """"initiate our photons"""
        self.mua = mua                      # коэффициент поглощения
        self.mus = mus                      # коэффициент рассеяния
        self.g = g                          # параметр анизотропии
        self.boundary = boundary            # граница среды
        self.n1 = n1                        # показатель преломления внутренней среды
        self.n2 = n2                        # показатель преломления внешней среды
        self.count = count                  # количество фотонов
        self.w = w                          # вес фотона
        self.temp = temp                    # время жизни фотона
        self.status = status                # статус фотона
        self.current = current              # начальная координата положения фотона по x,y,z
        self.direction = direction          # текущая координата направление движения фотона по ux, ux, uy
        self.r = r                          # радиус цилиндра
        self.ai = ai                        # угол падения
        self.at = at                        # угол преломления
        self.l_run = l_run                  # длина свободного пробега
        self.dz = dz                        # воксель z / расстоние между линиями сетки в направление z
        self.dr = dr                        # воксель r / расстоние между линиями сетки в направление r
        self.mut = self.mua + self.mus      # общий коэффициент взаимодействия mua + mus
        self.albedo = self.mus / self.mut   # вес уменьшающегося фотона
        self.nz = 5                       # кол-во линий (ячеек) по направлению z
        self.nr = 5                       # кол-во линий (ячеек) по направлению r
        self.atot = atot                    # суммарный вес фотона
        self.f = [[0],[0]]                         # матрица мощности флуорисценции

    def show_vars(self):
        print(f" mua = {self.mua},\n mus = {self.mus},\n g = {self.g},\n n1 = {self.n1},\n boundary = {self.boundary},\n"
              f" n2 = {self.n2},\n count = {self.count},\n w = {self.w},\n temp = {self.temp},\n"
              f" status = {self.status},\n current = {self.current},\n direction = {self.direction},\n"
              f" r = {self.r},\n ai = {self.ai},\n at = {self.at},\n l_run = {self.l_run},\n dz = {self.dz},\n dr = {self.dr},\n mut = {self.mut},\n albedo = {self.albedo},\n"
              f" nz = {self.nz},\n nr = {self.nr}\n, atot = {self.atot},\n")

    def current_orient(self, current):
        """текущие координаты фотона"""
        self.current = current
        return current

    def change_orient(self, current, l_run, direction):
        """расчёт координат фотона"""
        current0 = self.current
        current['x'] = current0['x'] + l_run * direction['x']
        current['y'] = current0['y'] + l_run * direction['y']
        current['z'] = current0['z'] + l_run * direction['z']

        current['x'] = abs(direction['x'])
        current['y'] = abs(direction['y'])
        current['z'] = abs(direction['z'])
        return current

    def direction_orient(self, direction):
        """текущие координаты фотона"""
        self.direction = direction
        return direction

    def photons_direction(self, direction, teta, fi):
        """"направление движение фотона"""
        self.direction = direction
        if abs(direction['z']) > 0.99999:
            direction['x'] = math.cos(fi) * math.sin(teta)
            direction['y'] = math.sin(fi) * math.sin(teta)
            direction['z'] = np.sign(direction['z']) * math.cos(teta)
        elif abs(direction['z']) <= 0.99999:
            direction['x'] = ((math.sin(teta)) / math.sqrt(1 - pow(direction['z'], 2)) *
                              (direction['x'] * direction['z'] * math.cos(fi) - direction['y'] * math.sin(fi) +
                               direction['y'] * math.cos(teta)))
            direction['y'] = ((math.sin(teta)) / math.sqrt(1 - pow(direction['z'], 2)) *
                              (direction['x'] * direction['z'] * math.cos(fi) + direction['y'] * math.sin(fi) +
                               direction['y'] * math.cos(teta)))
            direction['z'] = (-math.sin(teta) * math.cos(fi) * math.sqrt(1 - pow(direction['z'], 2)) + direction['z'] * math.cos(teta))

            #direction['x'] = abs(direction['x'])
            #direction['y'] = abs(direction['y'])
            #direction['z'] = abs(direction['z'])

        return direction

    def photons_propagation(self):
        """"распространение фотона"""

    def angles_direction(self):
        """"углы для нахождения направления движения фотона"""
        teta = 0                                    # cos teta
        fi = (math.pi*2)*random.random()            # Угол Фи
        if(self.g == 0):
            teta = (2 * random.random()) - 1
        elif (self.g > 0):
            teta = 1 / (2 * self.g) * (1 + math.pow(self.g, 2) -
                      math.pow( (1 - self.g * self.g) / 1 - self.g + 2 * self.g * random.random(), 2) )
        return [math.cos(teta), fi]

#    def reflection(self):
#        """отражение фотона на границе раздела сред, имеющих разные показатели преломления"""
##TO_DO
#        refl = 1
#        if (self.ai == 0):
#            return pow((self.n2-self.n1)/(self.n2+self.n1), 2)
#
#        elif (self.at < pow(math.sin, -1) < (self.n1/self.n2)):
#
#            return ( 1/2 * ((math.sin**2(self.ai - self.at)) / (math.sin**2(self.ai - self.at)) +
#                     (math.tan**2(self.ai - self.at)) / (math.tan**2(self.ai + self.at)) ))
#        elif (self.ai > math.sin**-1(self.n1/self.n2)):
#            return refl
#        print("refl = " + refl)
#

    def layer(self):
        """слой"""

    def free_run(self):
        """расчёт длины свободного пробега"""
        return -math.log(1 - random.random() * 1) / (self.mus + self.mua)
        #return l_run

    def total_weight(self):
        """формирование матрицы (ячеек) для заданных nz, nr"""
        f = self.f
        for i in range(self.nr):
            for r in range(self.nz):
                f[i][r] = 0.0
                return
                #print(i, r, end=' ')

    #def absorption(self):
    #    absorb =  * (1 - albedo);

    def bulk(self):
        """расчёт объёма с заданными границами(boundary)"""
        boundary = self.boundary
        bulk = pow(boundary, 3)
        return bulk

    def split_voxels(self):
        """расчёт колиечства вокселей"""
        voxel_perimeter = (self.dz + self.dr) * 2
        return voxel_perimeter


    def weight(self, current_w, l_run):
        """расчёт веса фотона"""
        #w0 = self.w
        #w = self.w * (self.mua /
        #         (self.mus)+(self.mua))


        #w = current_w * self.mua / (self.mus + self.mua)
        w = current_w * (math.exp(-self.mua * l_run))
        return w

    def snells_low(self, new_ai, new_at, new_n1, new_n2):
        self.ai = new_ai    # theta_1
        self.at = new_at    # theta_2
        self.n1 = new_n1    # n1
        self.n2 = new_n2    # n2
        new_ai_rad = np.radians(new_ai)
        new_at_rad = np.arcsin(new_n1 / new_n2 * np.sin(new_ai_rad))
        new_at = np.degrees(new_at_rad)
        self.at = new_at
        return [self.ai, self.at]
