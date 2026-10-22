import sys
import tomllib
import math
from PIL import Image, ImageDraw


class LSystem:
    def __init__(self, start, angle, production):
        self.state = start
        self.angle = angle
        self.production = production

    def iterate(self, n=1):
        for _ in range(n):
            result = ""
            for c in self.state:
                rule_applied = False
                for rule in self.production:
                    if rule["from"] == c:
                        result += rule["to"]
                        rule_applied = True
                if not rule_applied:
                    result += c
            self.state = result


class Turtle:
    def __init__(self, surface):
        self.pos = (200, 200)
        self.angle = 0
        self.surface = surface

    def forward(self, step):
        start = self.pos
        rad = math.radians(self.angle)
        end = (self.pos[0] + math.cos(rad) * step, self.pos[1] + math.sin(rad) * step)
        self.line(start, end)
        self.pos = end

    def left(self, angle):
        self.angle -= angle

    def right(self, angle):
        self.angle += angle

    def clone(self):
        c = Turtle(self.surface)
        c.pos = self.pos
        c.angle = self.angle
        return c

    def line(self, start, end):
        self.surface.line([start, end])


def draw(system, output="result.png"):
    with Image.new("RGB", [1024, 1024]) as im:
        canvas = ImageDraw.Draw(im)
        saved_turtles = []
        t = Turtle(canvas)

        for c in system.state:
            match c:
                case "F" | "G":
                    t.forward(5)
                case "+":
                    t.right(system.angle)
                case "-":
                    t.left(system.angle)
                case "[":
                    saved_turtles.append(t)
                    t = t.clone()
                case "]":
                    t = saved_turtles.pop()

        im.save(output)


def main():
    if len(sys.argv) < 3:
        print("Usage: lsystem-generate <definition-file> <iterations>")
        sys.exit(1)

    file = sys.argv[1]
    iterations = int(sys.argv[2])
    with open(file, "rb") as f:
        definition = tomllib.load(f)
        system = LSystem(**definition)
        system.iterate(iterations)
        draw(system)


if __name__ == "__main__":
    main()
