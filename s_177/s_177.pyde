# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice
from itertools import combinations

class Particle(object):

    def __init__(self):
        x = random(width)
        y = random(height)
        speed_range = [-3, 3]
        self.pos = PVector(x, y)
        self.velocity = PVector(random(*speed_range), random(*speed_range))
        self.color = color(240, 240, 240, 230)

    def move(self):
        self.pos.add(self.velocity)
        if self.is_vertical_bound:
            self.velocity.x *= -1

        if self.is_horizontal_bound:
            self.velocity.y *= -1

    @property
    def is_vertical_bound(self):
        return self.pos.x <= 0 or self.pos.x >= width

    @property
    def is_horizontal_bound(self):
        return self.pos.y <= 0 or self.pos.y >= height


    def display(self):
        noStroke()
        fill(self.color)
        #ellipse(self.pos.x, self.pos.y, 10, 10)

    def link(self, particle):
        distance = self.pos.dist(particle.pos)
        max_dist = 200
        if distance > max_dist:
            return

        alpha_v = map(distance, 0, max_dist, 240 , 0)
        stroke_w = map(distance, 0, max_dist, 6, 0)
        stroke_color = self.color
        r, g, b = red(stroke_color), green(stroke_color), blue(stroke_color)
        stroke(r, g, b, alpha_v)
        strokeWeight(stroke_w)

        line(self.pos.x, self.pos.y, particle.pos.x, particle.pos.y)

    @property
    def is_not_appearing(self):
        off_border_conditions = [
            self.pos.x < 0,
            self.pos.x > width,
            self.pos.y < 0,
            self.pos.y > height,
        ]
        return any(off_border_conditions)

    @property
    def is_appearing(self):
        return not self.is_not_appearing


particles = []
max_num_of_particles = 80

def setup():
    global combined_particles

    size(900, 900)
    for i in range(max_num_of_particles):
        new_particle = Particle()
        particles.append(new_particle)

    combined_particles = list(combinations(particles, 2))
    #frameRate(24)
    background(27)


def draw():
    global particles, combined_particles
    noStroke()
    background(27)


    for particle in particles:
        particle.move()

    for particle_1, particle_2 in combined_particles:
        particle_1.link(particle_2)

    for particle in particles:
        particle.display()

    save_video_frames(24, 60)