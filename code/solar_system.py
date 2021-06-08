# Author: Zimehr Abbasi
# Course: COSC 1
# Date: 15/01/2020
# Purpose: 2D representation of a Solar System

from cs1lib import *
from solar_system_classes import Body, System
import math
import random


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

TIME_SCALE = 20000  # real seconds per simulation second
PIXELS_PER_METER = 1 / 1e6  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

DENSITY = 5510

SIZE = 0
size_counter = False

solar_system_list = [Body("Sun", 1.98892e23, 0, 0, 0, 0, 24, 1, 1, 0)]

xc = 0
yc = 0

solar_system = System(solar_system_list)

def generate_star_location(n):
    global WINDOW_HEIGHT, WINDOW_WIDTH

    for i in range(n):
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT)
        yield (x, y)


NUMBER_OF_STARS = 150

star_location = [(x, y) for (x, y) in generate_star_location(NUMBER_OF_STARS)]

track_number = 0
is_track = False

instructions = False

# To get this list, I used the pandas library to download the Wikipedia list of name of exo planets and stored it
# in a text file

with open("planet_names.txt", 'r') as new_file:
    planets = new_file.readlines()

for i in range(len(planets)):
    planets[i] = planets[i][0: -1]


def get_values(mx, my, size):
    global PIXELS_PER_METER, DENSITY

    distance = math.sqrt(math.pow(-mx, 2) + math.pow(-my, 2)) / PIXELS_PER_METER
    mass = 1.98892e23
    G = 6.67384 * math.pow(10, -11)

    orbital_velocity = math.sqrt( G * mass / distance)
    #print(orbital_velocity)

    vx = (-my) / PIXELS_PER_METER * orbital_velocity / distance
    vy = (mx) / PIXELS_PER_METER * orbital_velocity / distance

    MASS = DENSITY * math.pow(SIZE, 3) * 4/3 * pi

    return (vx, vy, MASS)


def key_press(key):
    global track_number, is_track, solar_system_list, instructions

    try:
        track_number = int(key)
        if track_number < len(solar_system_list):
            if 0 < track_number < 7:
                is_track = True
    except:
        pass

    if key == 'i':
        instructions = True


def key_release(key):
    global track_number, is_track, instructions

    try:
        if 0 < int(key) < 7:
            is_track = False
            track_number = 0
    except:
        pass

    if key == 'i':
        instructions = False


def press(mx, my):
    global FRAMERATE, size_counter, xc, yc

    xc = mx
    yc = my

    size_counter = True


def release(mx, my):
    global solar_system_list, xc, yc, PIXELS_PER_METER, solar_system, SIZE, size_counter, planets

    size_counter = False

    xc = mx
    yc = my

    (vx, vy, mass) = get_values(xc - WINDOW_WIDTH / 2, yc - WINDOW_HEIGHT / 2, SIZE)

    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255

    name = planets[random.randint(0, len(planets)-1)]

    if SIZE > 1:

        if len(solar_system_list) > 6:
            solar_system_list.pop(1)

        solar_system_list.append(
            Body(name, mass, (xc - WINDOW_WIDTH / 2) / PIXELS_PER_METER, (yc - WINDOW_HEIGHT / 2) / PIXELS_PER_METER,
                 vx, vy, SIZE, r, g, b))

        solar_system = System(solar_system_list)
    # print(f"{vx}, {vy}")
    SIZE = 0


def main():
    global solar_system_list, xc, yc, PIXELS_PER_METER, solar_system, TIME_SCALE, TIMESTEP, SIZE, size_counter, \
        star_location, is_track, track_number, WINDOW_HEIGHT, WINDOW_WIDTH

    set_clear_color(0, 0, 0)    # black background

    clear()

    for x_star, y_star in star_location:
        set_fill_color(1, 1, 1)
        set_stroke_color(1, 1, 1)
        draw_circle(x_star, y_star, random.randint(0, 100)/100)

    if size_counter:
        SIZE = SIZE + 0.5

        set_fill_color(1, 1, 1)
        set_stroke_color(1, 1, 1)
        draw_circle(xc, yc, SIZE)

        if SIZE == 15:
            release(xc, yc)

    if is_track:
        if track_number == 1:
            set_stroke_color(solar_system_list[1].r, solar_system_list[1].g, solar_system_list[1].b)
            set_fill_color(0, 0, 0, 0)
            draw_circle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, math.sqrt(math.pow(solar_system_list[1].x * PIXELS_PER_METER, 2) + math.pow(solar_system_list[1].y * PIXELS_PER_METER, 2)))
            draw_line(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/2 + solar_system_list[1].x * PIXELS_PER_METER, WINDOW_WIDTH/2 + solar_system_list[1].y * PIXELS_PER_METER)
        elif track_number == 2:
            set_stroke_color(solar_system_list[2].r, solar_system_list[2].g, solar_system_list[2].b)
            set_fill_color(0, 0, 0, 0)
            draw_circle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, math.sqrt(math.pow(solar_system_list[2].x * PIXELS_PER_METER, 2) + math.pow(solar_system_list[2].y * PIXELS_PER_METER, 2)))
            draw_line(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,WINDOW_WIDTH/2 +  solar_system_list[2].x * PIXELS_PER_METER,
                      WINDOW_WIDTH/2 + solar_system_list[2].y * PIXELS_PER_METER)
        elif track_number == 3:
            set_stroke_color(solar_system_list[3].r, solar_system_list[3].g, solar_system_list[3].b)
            set_fill_color(0, 0, 0, 0)
            draw_circle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, math.sqrt(math.pow(solar_system_list[3].x * PIXELS_PER_METER, 2) + math.pow(solar_system_list[3].y * PIXELS_PER_METER, 2)))
            draw_line(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH/2 + solar_system_list[3].x * PIXELS_PER_METER,
                      WINDOW_WIDTH/2 + solar_system_list[3].y * PIXELS_PER_METER)
        elif track_number == 4:
            set_stroke_color(solar_system_list[4].r, solar_system_list[4].g, solar_system_list[4].b)
            set_fill_color(0, 0, 0, 0)
            draw_circle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, math.sqrt(math.pow(solar_system_list[4].x * PIXELS_PER_METER, 2) + math.pow(solar_system_list[4].y * PIXELS_PER_METER, 2)))
            draw_line(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH/2 + solar_system_list[4].x * PIXELS_PER_METER,
                      WINDOW_WIDTH/2 + solar_system_list[4].y * PIXELS_PER_METER)
        elif track_number == 5:
            set_stroke_color(solar_system_list[5].r, solar_system_list[5].g, solar_system_list[5].b)
            set_fill_color(0, 0, 0, 0)
            draw_circle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, math.sqrt(math.pow(solar_system_list[5].x * PIXELS_PER_METER, 2) + math.pow(solar_system_list[5].y * PIXELS_PER_METER, 2)))
            draw_line(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH/2 + solar_system_list[5].x * PIXELS_PER_METER,
                      WINDOW_WIDTH/2 + solar_system_list[5].y * PIXELS_PER_METER)
        elif track_number == 6:
            set_stroke_color(solar_system_list[6].r, solar_system_list[6].g, solar_system_list[6].b)
            set_fill_color(0, 0, 0, 0)
            draw_circle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, math.sqrt(math.pow(solar_system_list[6].x * PIXELS_PER_METER, 2) + math.pow(solar_system_list[6].y * PIXELS_PER_METER, 2)))
            draw_line(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH/2 + solar_system_list[6].x * PIXELS_PER_METER,
                      WINDOW_WIDTH/2 + solar_system_list[6].y * PIXELS_PER_METER)
        else:
            pass

    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)

    set_fill_color(0, 0, 0)
    set_stroke_color(1, 1, 1)
    draw_rectangle(10, 10, 405, 5 + len(solar_system_list) * 15)

    set_stroke_color(1, 1, 0)
    draw_text("#", 17, 25)
    draw_text("NAME", 32, 25 )
    draw_text("SPEED(m/s)", 122, 25)
    draw_text("DISTANCE(m)", 212, 25)
    draw_text("TIME PERIOD(s)", 312, 25)

    for i in range(len(solar_system_list)):
        if i > 0:
            set_stroke_width(1)
            set_stroke_color(1, 1, 1)
            draw_text(str(i), 17, 25 + 15 * i)
            draw_text(solar_system_list[i].name, 32, 25 + 15 * i)
            draw_text('%.10s' % str(math.sqrt(math.pow(solar_system_list[i].vx / PIXELS_PER_METER, 2) + math.pow(solar_system_list[i].vy / PIXELS_PER_METER, 2))),122, 25 + 15 * i)
            draw_text('%.11s' % str(math.sqrt(math.pow(solar_system_list[i].x, 2) + math.pow(solar_system_list[i].y, 2))),212, 25 + 15 * i)
            draw_text('%.11s' % str(14.26 * pi *math.sqrt(math.pow(solar_system_list[i].x, 2) + math.pow(solar_system_list[i].y, 2))/math.sqrt(math.pow(solar_system_list[i].vx / PIXELS_PER_METER, 2) + math.pow(solar_system_list[i].vy / PIXELS_PER_METER, 2))),312, 25 + 15 * i)
            if is_track:
                if track_number == 1:
                    set_stroke_width(2)
                    set_stroke_color(solar_system_list[1].r, solar_system_list[1].g, solar_system_list[1].b)
                    draw_text(str(1), 17, 40)
                    draw_text(solar_system_list[1].name, 32, 25 + 15 * 1)
                    draw_text('%.10s' % str(math.sqrt(math.pow(solar_system_list[1].vx / PIXELS_PER_METER, 2) + math.pow(solar_system_list[1].vy / PIXELS_PER_METER, 2))), 122,25 + 15 * 1)
                    draw_text('%.11s' % str(math.sqrt(math.pow(solar_system_list[1].x, 2) + math.pow(solar_system_list[1].y, 2))), 212,25 + 15 * 1)
                    draw_text('%.11s' % str(14.26 * pi * math.sqrt(
                        math.pow(solar_system_list[1].x, 2) + math.pow(solar_system_list[1].y, 2)) / math.sqrt(
                        math.pow(solar_system_list[1].vx / PIXELS_PER_METER, 2) + math.pow(
                            solar_system_list[1].vy / PIXELS_PER_METER, 2))), 312, 25 + 15 * 1)
                elif track_number == 2:
                    set_stroke_width(2)
                    set_stroke_color(solar_system_list[2].r, solar_system_list[2].g, solar_system_list[2].b)
                    draw_text(str(2), 17, 55)
                    draw_text(solar_system_list[2].name, 32, 25 + 15 * 2)
                    draw_text('%.10s' % str(math.sqrt(math.pow(solar_system_list[2].vx / PIXELS_PER_METER, 2) + math.pow(solar_system_list[2].vy / PIXELS_PER_METER, 2))), 122,25 + 15 * 2)
                    draw_text('%.11s' % str(math.sqrt(math.pow(solar_system_list[2].x, 2) + math.pow(solar_system_list[2].y, 2))), 212,25 + 15 * 2)
                    draw_text('%.11s' % str(14.26 * pi * math.sqrt(
                        math.pow(solar_system_list[2].x, 2) + math.pow(solar_system_list[2].y, 2)) / math.sqrt(
                        math.pow(solar_system_list[2].vx / PIXELS_PER_METER, 2) + math.pow(
                            solar_system_list[2].vy / PIXELS_PER_METER, 2))), 312, 25 + 15 * 2)
                elif track_number == 3:
                    set_stroke_width(2)
                    set_stroke_color(solar_system_list[3].r, solar_system_list[3].g, solar_system_list[3].b)
                    draw_text(str(3), 17, 70)
                    draw_text(solar_system_list[3].name, 32, 25 + 15 * 3)
                    draw_text('%.10s' % str(math.sqrt(math.pow(solar_system_list[3].vx / PIXELS_PER_METER, 2) + math.pow(solar_system_list[3].vy / PIXELS_PER_METER, 2))), 122,25 + 15 * 3)
                    draw_text('%.11s' % str(math.sqrt(math.pow(solar_system_list[3].x, 2) + math.pow(solar_system_list[3].y, 2))), 212,25 + 15 * 3)
                    draw_text('%.11s' % str(14.26 * pi * math.sqrt(
                        math.pow(solar_system_list[3].x, 2) + math.pow(solar_system_list[3].y, 2)) / math.sqrt(
                        math.pow(solar_system_list[3].vx / PIXELS_PER_METER, 2) + math.pow(
                            solar_system_list[3].vy / PIXELS_PER_METER, 2))), 312, 25 + 15 * 3)
                elif track_number == 4:
                    set_stroke_width(2)
                    set_stroke_color(solar_system_list[4].r, solar_system_list[4].g, solar_system_list[4].b)
                    draw_text(str(4), 17, 85)
                    draw_text(solar_system_list[4].name, 32, 25 + 15 * 4)
                    draw_text('%.10s' % str(math.sqrt(math.pow(solar_system_list[4].vx / PIXELS_PER_METER, 2) + math.pow(solar_system_list[4].vy / PIXELS_PER_METER, 2))), 122,25 + 15 * 4)
                    draw_text('%.11s' % str(math.sqrt(math.pow(solar_system_list[4].x, 2) + math.pow(solar_system_list[4].y, 2))), 212,25 + 15 * 4)
                    draw_text('%.11s' % str(14.26 * pi * math.sqrt(
                        math.pow(solar_system_list[4].x, 2) + math.pow(solar_system_list[4].y, 2)) / math.sqrt(
                        math.pow(solar_system_list[4].vx / PIXELS_PER_METER, 2) + math.pow(
                            solar_system_list[4].vy / PIXELS_PER_METER, 2))), 312, 25 + 15 * 4)
                elif track_number == 5:
                    set_stroke_width(2)
                    set_stroke_color(solar_system_list[5].r, solar_system_list[5].g, solar_system_list[5].b)
                    draw_text(str(5), 17, 100)
                    draw_text(solar_system_list[5].name, 32, 25 + 15 * 5)
                    draw_text('%.10s' % str(math.sqrt(math.pow(solar_system_list[5].vx / PIXELS_PER_METER, 2) + math.pow(solar_system_list[5].vy / PIXELS_PER_METER, 2))), 122,25 + 15 * 5)
                    draw_text('%.11s' % str(math.sqrt(math.pow(solar_system_list[5].x, 2) + math.pow(solar_system_list[5].y, 2))), 212,25 + 15 * 5)
                    draw_text('%.11s' % str(14.26 * pi * math.sqrt(
                        math.pow(solar_system_list[5].x, 2) + math.pow(solar_system_list[5].y, 2)) / math.sqrt(
                        math.pow(solar_system_list[5].vx / PIXELS_PER_METER, 2) + math.pow(
                            solar_system_list[5].vy / PIXELS_PER_METER, 2))), 312, 25 + 15 * 5)
                elif track_number == 6:
                    set_stroke_width(2)
                    set_stroke_color(solar_system_list[6].r, solar_system_list[6].g, solar_system_list[6].b)
                    draw_text(str(6), 17, 115)
                    draw_text(solar_system_list[6].name, 32, 25 + 15 * 6)
                    draw_text('%.10s' % str(math.sqrt(math.pow(solar_system_list[6].vx / PIXELS_PER_METER, 2) + math.pow(solar_system_list[6].vy / PIXELS_PER_METER, 2))), 122,25 + 15 * 6)
                    draw_text('%.11s' % str(math.sqrt(math.pow(solar_system_list[6].x, 2) + math.pow(solar_system_list[6].y, 2))), 212,25 + 15 * 6)
                    draw_text('%.11s' % str(14.26 * pi * math.sqrt(
                        math.pow(solar_system_list[6].x, 2) + math.pow(solar_system_list[6].y, 2)) / math.sqrt(
                        math.pow(solar_system_list[6].vx / PIXELS_PER_METER, 2) + math.pow(
                            solar_system_list[6].vy / PIXELS_PER_METER, 2))), 312, 25 + 15 * 6)
            else:
                pass

    if not instructions:
        set_stroke_color(1, 1, 0)
        draw_text("Press 'i' for Commands", 645, 25)
    elif instructions:
        set_fill_color(0, 0, 0)
        set_stroke_color(1, 1, 1)
        draw_rectangle(640, 10, 155, 385)
        draw_text("Press a number from", 645, 25)
        draw_text("1 - 6 on your key-", 645, 40)
        draw_text("board to highlight", 645, 55)
        draw_text("a specific planet", 645, 70)
        draw_text(" ", 645, 85)
        draw_text("Hold down your mouse", 645, 100)
        draw_text("to create a planet", 645, 115)
        draw_text("The longer you hold", 645, 130)
        draw_text("the larger the planet", 645, 145)
        draw_text("will be.", 645, 160)
        draw_text(" ", 645, 175)
        draw_text("Maximum of 6 bodies", 645, 190)
        draw_text("allowed.", 645, 205)
        draw_text(" ", 645, 175 + 45)
        draw_text("OBSERVATIONS:", 645, 100 + 90 + 45)
        draw_text(" ", 645, 115 + 90 + 45)
        draw_text("Greater the distance,", 645, 130 + 90 + 45)
        draw_text("lesser the velocity", 645, 145 + 90 + 45)
        draw_text(" ", 645, 160 + 90 + 45)
        draw_text("Greater the distance,", 645, 175 + 90 + 45)
        draw_text("Greater the time taken", 645, 190 + 90 + 45)
        draw_text("for 1 revolution", 645, 205 + 90 + 45)
        draw_text(" ", 645, 220 + 90 + 45)
        draw_text("Bodies are in a state", 645, 235 + 90 + 45)
        draw_text("of free-fall", 645, 250 + 90 + 45)


start_graphics(main, 5400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press = press, mouse_release = release, key_press = key_press, key_release = key_release)
