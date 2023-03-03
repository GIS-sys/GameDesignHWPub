import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Rectangles")

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define a class for the rectangles
class Rectangle:
    def __init__(self, x, y, speed, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 50
        self.height = 50

    def move(self):
        # Move the rectangle horizontally
        self.x += self.speed
        if self.x > width:
            self.x = 0 - self.width
        elif self.x < 0 - self.width:
            self.x = width

        # Move the rectangle vertically
        self.y += self.speed
        if self.y > height:
            self.y = 0 - self.height
        elif self.y < 0 - self.height:
            self.y = height

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


# Create some rectangles with random colors and speeds
rectangles = []
for i in range(10):
    x = random.randint(0, width)
    y = random.randint(0, height)
    speed = random.randint(1, 5)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rectangles.append(Rectangle(x, y, speed, color))


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(white)

    # Move and draw the rectangles
    for rectangle in rectangles:
        rectangle.move()
        rectangle.draw()

    # Update the window
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()
