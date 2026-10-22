import sys
import tomllib
from turtle import Turtle


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


def draw(system, speed=6, tracer=None):
    t = Turtle()
    if tracer is not None:
        t.screen.tracer(tracer)
    else:
        t.speed(speed)
    t.teleport(-100, 100)
    for s in system.state:
        match s:
            case "F" | "G":
                t.forward(10)
            case "+":
                t.left(system.angle)
            case "-":
                t.right(system.angle)
            # "[" and "]" not implemented

    t.screen.mainloop()


def main():
    if len(sys.argv) < 3:
        print("Usage: lsystem-turtle <definition-file> <iterations>")
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
