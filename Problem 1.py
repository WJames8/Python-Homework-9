
from graphics import *

win = GraphWin("Bouncing Balls", 600, 400)

# Store information for three balls
balls = [
    {"height": 10, "bounces": 0, "x": 150},
    {"height": 15, "bounces": 0, "x": 300},
    {"height": 20, "bounces": 0, "x": 450}
]

# Create graphics objects and store them in a list
for ball in balls:
    ball["circle"] = Circle(Point(ball["x"], 350), 15)
    ball["circle"].setFill("blue")
    ball["circle"].draw(win)

# Simulate bouncing
while any(ball["height"] >= 0.001 for ball in balls):

    for ball in balls:
        if ball["height"] >= 0.001:
            ball["height"] *= 0.60
            ball["bounces"] += 1

            # Update ball position
            y = 350 - (ball["height"] * 10)
            ball["circle"].undraw()
            ball["circle"] = Circle(Point(ball["x"], y), 15)
            ball["circle"].setFill("blue")
            ball["circle"].draw(win)

        update(30)

# Display bounce counts
for i, ball in enumerate(balls):
    print("Ball", i + 1, "bounced", ball["bounces"], "times.")

win.getMouse()
win.close()
