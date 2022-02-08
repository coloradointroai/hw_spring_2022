from collections import deque
"""
 Class PathSolver

"""

# Create PathSolver Class


class PathSolver:
    """Contains methods to solve multiple path search algorithms"""

    # init for PathSolver Class
    def __init__(self):
        """Create PathSolver"""

    def path(self, previous, s): 
        """
        `previous` is a dictionary chaining together the predecessor state that led to each state

        `s` will be None for the initial state

        otherwise, start from the last state `s` and recursively trace `previous` back to the initial state,
        constructing a list of states visited as we go
        """ 
        
        if s is None:
            return []
        else:
            return self.path(previous, previous[s])+[s]

    def pathcost(self, path, step_costs):
        """add up the step costs along a path, which is assumed to be a list output from the `path` function above"""
        
        cost = 0
        for s in range(len(path)-1):
            cost += step_costs[path[s]][path[s+1]]
        return cost
    

    def breadth_first_search(self,start: tuple, goal, state_graph, return_cost=False):
        """ find a shortest sequence of states from start to the goal """
        print("calliing BFS")
        
        frontier = deque([start]) # doubly-ended queue of states
        previous = {start: None}  # start has no previous state; other states will
        
        # Return on start is goal
        if start == goal:
            path_out = [start]
            if return_cost: return path_out, self.pathcost(path_out, state_graph)
            return path_out

        # loop through frontine searching nodes until we find a goal
        while frontier:
            s = frontier.popleft()
            for s2 in state_graph[s]:
                if (s2 not in previous) and (s2 not in frontier):
                    frontier.append(s2)
                    previous[s2] = s
                    if s2 == goal:
                        path_out = self.path(previous, s2)
                        if return_cost: return path_out, self.pathcost(path_out, state_graph)
                        return path_out
        
        # no solution
        if return_cost:
            return [], 0
        else: 
            return []


    def depth_first_search(self,start: tuple, goal, state_graph, return_cost=False):
        """Problem 2.a: you need to implement this function"""

        return

    def uniform_cost_search(self,start: tuple, goal, state_graph, return_cost=False):
        """Problem 2.a: you need to implement this function"""

        return

    def a_star_euclidian(self,start: tuple, goal, state_graph, return_cost=False):
        """Problem 2.b: you need to implement this function"""
        return

    
    def a_star_manhattan(self,start: tuple, goal, state_graph, return_cost=False):
        """Problem 2c: you need to implement this function"""
        return
