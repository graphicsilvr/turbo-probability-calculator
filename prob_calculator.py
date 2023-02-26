import copy
import random

import copy
import random

class Hat:
    def __init__(self, **balls):
        """
        Initialize a new hat with contents specified by the arguments.
        Args:
            **balls: keyword arguments indicating the balls and their quantity in the hat
        """
        self.contents = []
        for ball, count in balls.items():
            for i in range(count):
                self.contents.append(ball)

    def draw(self, num):
        """
        Remove `num` random balls from the hat's contents and return them.
        If `num` is greater than the number of balls in the hat, return all the balls.
        Args:
            num: the number of balls to draw
        Returns:
            A list of strings representing the balls drawn from the hat
        """
        if num >= len(self.contents):
            return self.contents.copy()
        balls_drawn = []
        for i in range(num):
            ball_index = random.randrange(len(self.contents))
            balls_drawn.append(self.contents.pop(ball_index))
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Perform a number of experiments drawing `num_balls_drawn` balls from the `hat`.
    In each experiment, count the number of times that at least the number of balls specified in
    `expected_balls` was drawn. Return the probability of that event as the fraction of experiments
    in which it occurred.
    Args:
        hat: a Hat object representing the initial contents of the hat
        expected_balls: a dictionary specifying the minimum number of times to draw each color
        num_balls_drawn: the number of balls to draw in each experiment
        num_experiments: the number of experiments to perform
    Returns:
        The probability of drawing at least the number of expected balls in `num_experiments`
    """
    # Convert `expected_balls` to a list of ball strings, duplicating each ball as many times as required
    expected_balls_list = []
    for ball, count in expected_balls.items():
        for i in range(count):
            expected_balls_list.append(ball)
    # Count the number of successful experiments
    num_successful_experiments = 0
    for i in range(num_experiments):
        # Create a deep copy of the hat so we can modify it without changing the original contents
        hat_copy = copy.deepcopy(hat)
        # Draw the required number of balls from the hat
        balls_drawn = hat_copy.draw(num_balls_drawn)
        # Make a copy of the expected balls list so we can modify it without changing the original
        expected_balls_copy = expected_balls_list.copy()
        success = True
        # For each ball in the expected list, remove it from the drawn balls if possible.
        # If not possible, the experiment is unsuccessful and we break out of the loop
        for ball in expected_balls_copy:
            if ball in balls_drawn:
                balls_drawn.remove(ball)
            else:
                success = False
                break
        if success:
            num_successful_experiments += 1
    # Calculate the probability of drawing at least the expected number of balls
    return num_successful_experiments / num_experiments

