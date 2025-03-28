# Brownian Motion Simulation

This project simulates the random motion of a robot in a 2D arena using Brownian motion principles. The robot moves in random directions and bounces off the arena boundaries when it collides with them.

## How It Works

1. **BrownianRobot Class**:
   - Represents the robot in the arena.
   - The robot starts at the center of the arena and moves in random directions.
   - If the robot hits the boundary of the arena, it changes direction in a random way and stays within bounds.

2. **BrownianSimulation Class**:
   - Manages the simulation of the robot's motion.
   - Uses Matplotlib to visualize the robot's movement in real-time.
   - Animates the robot's motion using `FuncAnimation`.


## How to Run the Code

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install numpy matplotlib
   ```
3. Run the script:
   ```bash
   python3 main.py
   ```
4. A window will open showing the robot's motion in the arena.

## Example Video

Below is an example video demonstrating the simulation:

<video width="640" height="360" controls>
  <source src="example.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## YouTube Link

Watch the project in action on YouTube: [Brownian Motion Simulation](https://www.youtube.com/watch?v=example_link)