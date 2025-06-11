import turtle

#game_screen = turtle.Screen()
#game_screen.setup(width=600, height=400)  # Window size: 600x400 pixels
turtle.Screen().setup(width=600, height=400)  # Window size: 600x400 pixels
turtle.setundobuffer(1)  # Enable undo buffer
turtle.bgcolor("black")  # Background color
turtle.title("Game")  # Window title
turtle.tracer(1)  # Disable animation for faster drawing
turtle.fd(0)
turtle.done()