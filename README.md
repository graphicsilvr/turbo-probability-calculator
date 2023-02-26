# Probability Calculator
This is a Python program for estimating the probability of drawing certain balls randomly from a hat.

# Getting Started
To use this program, you will need to have Python 3 installed on your computer.

Clone this repository to your local machine.
Open a terminal and navigate to the project directory.
Run the program using the command python main.py.
How to Use
The program consists of two files: prob_calculator.py and main.py.

prob_calculator.py contains the Hat class and the experiment function. The Hat class takes a variable number of arguments that specify the number of balls of each color that are in the hat, and has a draw method that removes balls at random from the hat and returns them as a list. The experiment function takes a Hat object, an expected_balls dictionary, the number of balls to draw in each experiment, and the number of experiments to perform, and returns the estimated probability of drawing the expected balls.

main.py is an example of how to use the Hat class and experiment function. It creates a Hat object with a specified number of balls of different colors, and runs an experiment to estimate the probability of drawing a certain number of balls of each color.

# Example
Here is an example of how to use the program:

python
from prob_calculator import Hat, experiment

# Create a hat object
hat = Hat(red=5, blue=3, green=2)

# Set the expected balls
expected_balls = {'red': 2, 'blue': 1}

# Set the number of balls to draw and experiments to perform
num_balls_drawn = 4
num_experiments = 1000

# Run the experiment and print the result
probability = experiment(hat=hat, expected_balls=expected_balls, num_balls_drawn=num_balls_drawn, num_experiments=num_experiments)
print(f"Probability of drawing {expected_balls} in {num_balls_drawn} balls: {probability}")
This will output the estimated probability of drawing 2 red balls and 1 blue ball in 4 balls drawn from the hat, based on 1000 experiments. The probability will be different each time the code is run due to the random nature of the experiments.

# Authors
This program was created by Sylvious.

# Lisence
This project is licensed under the MIT License or the Apache License. Please see the LICENSE file for details.