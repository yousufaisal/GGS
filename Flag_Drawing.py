import turtle

def draw_rectangle(x, y, width, height, color):
    """Draws a filled rectangle and returns the center coordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

    turtle.end_fill()
    return x + width / 2, y - height / 2  # Return center coordinates

def draw_circle(x, y, radius, color):
    """Draws a filled circle centered at (x, y)."""
    turtle.penup()
    turtle.goto(x, y - radius) 
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)  # Draw a full circle
    turtle.end_fill()

def draw_flag(x, y, scale):
    """Draws a flag with a flagpole and a center circle."""
    # Draw the flag rectangle
    center_x, center_y = draw_rectangle(x, y + 100 * scale, 150 * scale, 100 * scale, "red")  # FLAG
    
    # Draw the left flagpole
    draw_rectangle(x, y, 20 * scale, 200 * scale, "black")  # LEFT FLAGPOLE
    
    # Draw the center circle
    draw_circle(center_x, center_y, 25 * scale, "white")  # CENTER CIRCLE  

def main():
    """Sets up the background color and draws two flags."""
    turtle.bgcolor("light blue")  # Background color
    turtle.speed(5)

    draw_flag(-200, -100, 1)  # Draw larger flag
    draw_flag(100, -50, 0.7)   # Draw smaller flag

    turtle.done()

if __name__ == "__main__":
    main()