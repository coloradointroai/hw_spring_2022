from colorado_intro_ai.hw2.enviornment import Environment
from colorado_intro_ai.hw2.pathSolver import PathSolver


"""
Robot Class

Test update

"""

# Create Robot Class
class Robot:
    """🤖"""

    # init for Robot Class
    def __init__(self, size: tuple = (10, 10), start: tuple = (0, 0), goal: tuple = (8, 9), seed: int = 0):
        """Create robot"""
        self.env = Environment(size, start, goal, seed)
        self.path_solver = PathSolver()

    def show_env(self):
        """Displays the robots initial setup"""
        self.env.show_env()

    def show_env_and_path(self, path):
        self.env.show_env_and_path(path)

    def refresh_env(self):
        self.env = Environment(self.env.size, self.env.start, self.env.goal, (self.env.seed + 1))