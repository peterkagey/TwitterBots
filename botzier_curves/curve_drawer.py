from PIL import Image, ImageDraw
import random
import math

class BezierCurveDrawer():
    def __init__(self):
        self.x_max = 10000
        self.y_max = 10000
        self.x_range = [self.x_max,0]
        self.y_range = [self.y_max,0]
        self.img = Image.new("RGBA", (self.x_max, self.y_max), (255,255,255,0))
        self.draw = ImageDraw.Draw(self.img)
        self.initialize_random_points()

    def curve_points(self, fx, fy):
        points = []
        for i in range(1001):
            t = i / 1000
            points += [(int(fx(t)), int(fy(t)))]
            self.x_range[0] = min(self.x_range[0], fx(t))
            self.x_range[1] = max(self.x_range[1], fx(t))
            self.y_range[0] = min(self.y_range[0], fy(t))
            self.y_range[1] = max(self.y_range[1], fy(t))
        return points

    def f(t):
        return 400 + 200 * (t**2 - 1)

    def g(t):
        return 200 + 100 * math.sin(t*math.pi)

    def bezier_curve(self, p1, p2, p3, p4):
        (x1,y1) = p1
        (x2,y2) = p2
        (x3,y3) = p3
        (x4,y4) = p4
        def fx(t):
            return (1-t)**3 * x1 + 3 * (1-t)**2 * t * x2 + 3 * (1-t) * t**2 * x3 + t**3 * x4
        def fy(t): 
            return (1-t)**3 * y1 + 3 * (1-t)**2 * t * y2 + 3 * (1-t) * t**2 * y3 + t**3 * y4
        return (fx, fy)

    def draw_bezier_curve(self, p1, p2, p3, p4, color="red"):
        (f, g) = self.bezier_curve(p1, p2, p3, p4)
        # draw.line(curve_points(f, g), fill=color, width=100, joint="curve")
        for (x, y) in self.curve_points(f, g):
            self.draw.ellipse((x-50, y-50, x+50, y+50), fill=color)

    def random_point(self):
        return (random.randrange(0,self.x_max), random.randrange(0,self.y_max)) 

    def random_color(self):
        return (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)) 

    # rand_p3 = (random.randrange(0,x_max), random.randrange(0,y_max))
    # rand_p4 = (random.randrange(0,x_max), random.randrange(0,y_max))
    # k = random.uniform(0.25,0.75)
    # endpoint = (rand_p3[0]*k + rand_p4[0]*(1-k), rand_p3[1]*k + rand_p4[1]*(1-k))
    # draw_bezier_curve(random_point(), random_point(), rand_p3, endpoint, random_color())
    # draw_bezier_curve(endpoint, rand_p4, random_point(), random_point(), random_color())

    def color_spectrum(self):
        (x1, y1, z1) = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        (x2, y2, z2) = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        (x3, y3, z3) = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        (x4, y4, z4) = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)) # (x1,y1,z1)
        def fx(t):
            return (1-t)**3 * x1 + 3 * (1-t)**2 * t * x2 + 3 * (1-t) * t**2 * x3 + t**3 * x4
        def fy(t): 
            return (1-t)**3 * y1 + 3 * (1-t)**2 * t * y2 + 3 * (1-t) * t**2 * y3 + t**3 * y4
        def fz(t): 
            return (1-t)**3 * z1 + 3 * (1-t)**2 * t * z2 + 3 * (1-t) * t**2 * z3 + t**3 * z4
        return (fx, fy, fz)

    def initialize_random_points(self):
        self.p1 = self.random_point()
        self.p2 = self.random_point()
        self.p3 = self.random_point()
        self.p4 = self.random_point()
        self.end_point = self.p1

    def draw_it(self):
        colors = self.color_spectrum()
        steps = 20
        for i in range(steps + 1):
            red = int(colors[0](i/steps))
            green = int(colors[1](i/steps))
            blue = int(colors[2](i/steps))
            k = random.uniform(0.25,0.75)
            start_point = self.end_point
            self.end_point = (self.p3[0]*k + self.p4[0]*(1-k), self.p3[1]*k + self.p4[1]*(1-k))
            self.draw_bezier_curve(start_point, self.p2, self.p3, self.end_point, (red, green, blue))
            self.p2 = self.p4
            self.p3 = self.random_point()
            self.p4 = self.random_point()

        filename = "/Users/peter/Programming/parametric.png"
        self.img.resize((900,900)).save(filename)
        return filename