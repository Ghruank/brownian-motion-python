import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class BrownianRobot:
    def __init__(self, arena_size, step_size):
        self.arena_size = arena_size
        self.step_size = step_size*2  
        self.position = np.array([arena_size / 2, arena_size / 2])
        self.direction = np.random.uniform(0, 2 * np.pi)

    def move(self):
        self.position += self.step_size * np.array([np.cos(self.direction), np.sin(self.direction)])
        self.check_boundary_collision()

    def check_boundary_collision(self):
        if self.position[0] <= 0 or self.position[0] >= self.arena_size:
            self.direction = np.random.uniform(0, 2 * np.pi)  
            self.position[0] = np.clip(self.position[0], 0, self.arena_size)
        if self.position[1] <= 0 or self.position[1] >= self.arena_size:
            self.direction = np.random.uniform(0, 2 * np.pi)  
            self.position[1] = np.clip(self.position[1], 0, self.arena_size)

class BrownianSimulation:
    def __init__(self, arena_size, step_size):
        self.arena_size = arena_size
        self.step_size = step_size
        self.robot = BrownianRobot(arena_size, step_size)

    def update(self, frame, scat):
        self.robot.move()
        scat.set_offsets(self.robot.position)
        return scat,

    def run(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.arena_size)
        ax.set_ylim(0, self.arena_size)
        scat = ax.scatter(self.robot.position[0], self.robot.position[1])

        ani = animation.FuncAnimation(fig, self.update, fargs=(scat,), interval=50)
        plt.show()

def main():
    arena_size = 100
    step_size = 1
    simulation = BrownianSimulation(arena_size, step_size)
    simulation.run()

if __name__ == "__main__":
    main()
