from cs1lib import *
import math
import random

class Body:

    def __init__(self, name, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestamp):

        self.x = self.x + self.vx * timestamp
        self.y = self.y + self.vy * timestamp

    def update_velocity(self, ax, ay, timestep):

        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep


    def draw(self, cx, cy, pixels_per_meter):

        set_fill_color(self.r, self.g, self.b)
        set_stroke_color(self.r, self.g, self.b)
        draw_circle(cx + self.x * pixels_per_meter, cy + self.y * pixels_per_meter, self.pixel_radius)

        set_stroke_color(1, 1, 1)
        draw_text(self.name.capitalize(), cx + self.x * pixels_per_meter - 3*len(self.name.capitalize()), cy + self.y * pixels_per_meter - self.pixel_radius - 5)


class System:

    def __init__(self, body_list):
        self.body_list = body_list

    def compute_acceleration(self, i):

        ax = 0
        ay = 0

        for m in self.body_list:

            if m != self.body_list[i]:

                if m.mass >= 1e25:
                    continue

                mass = m.mass
                G = 6.67384 * math.pow(10, -11)
                radius = math.sqrt(math.pow(m.x - self.body_list[i].x, 2) + math.pow(m.y - self.body_list[i].y, 2))
                dx = m.x - self.body_list[i].x
                dy = m.y - self.body_list[i].y

                a = (G * mass) / (math.pow(radius, 2))
                ax = ax + a * dx / radius
                ay = ay + a * dy / radius

        return ax, ay

    def update(self, timestamp):

        i = 0
        for body in self.body_list:
            x = 0
            ax = 0
            ay = 0
            ax1 = ax
            ay1 = ay
            while x <= timestamp/10:
                (ax, ay) = self.compute_acceleration(i)
                body.update_velocity((ax+ax1)/2, (ay+ay1)/2, timestamp/10)
                (ax1, ay1) = self.compute_acceleration(i)
                body.update_position(timestamp/10)
                x += 1
            i += 1

    def draw(self, cx, cy, pixel_per_meter):

        for body in self.body_list:
            body.draw(cx, cy, pixel_per_meter)
