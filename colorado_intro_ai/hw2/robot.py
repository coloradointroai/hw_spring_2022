from colorado_intro_ai.hw2.enviornment import Environment
from colorado_intro_ai.hw2.pathSolver import PathSolver

# Import info for loading in and viewing states location
from ipyleaflet import Map, Polyline, Marker
from ipywidgets import Layout
import pandas
import geopy.distance




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
        # city data from https://github.com/jasperdebie/VisInfo/blob/master/us-state-capitals.csv
        self.state_dict = self.__get_states_data('../data/us.csv')
        self.m = Map(center = (39, -97), zoom =4, layout=Layout(width='100%', height='800px'))
        self.line = None


    def show_env(self):
        """Displays the robots initial setup"""
        self.env.show_env(self.env.env)

    def show_env_and_path(self, path):
        self.env.show_env_and_path(path)

    def refresh_env(self):
        self.env = Environment(self.env.size, self.env.start, self.env.goal, (self.env.seed + 1))




    # TODO: Moves these functions to a subclass

    def get_dist_mi(self, state_1: str, state_2: str):
        return geopy.distance.geodesic(self.state_dict[state_1], self.state_dict[state_2]).mi


    def get_dist_km(self, state_1: str, state_2: str):
        return geopy.distance.geodesic(self.state_dict[state_1], self.state_dict[state_2]).km

    def show_city_connections_by_name(self, city_order: list):
        list_of_coordinates = []
        for key in city_order:
            list_of_coordinates.append(self.state_dict[key])
        self.show_city_connections_by_coordinates(list_of_coordinates)

    def show_city_connections_by_coordinates(self, city_order: list):
        """Displays a marker for each location and connects them with lines in the order they are passed in. The last element is connected to the first. """
        if len(city_order) < 2:
            print('show_city_connections input must be of len >=2')
            return

        line = Polyline(
            locations = city_order + [city_order[0]],
            color     = "black" ,
            weight    = 1,
            fill      = False
        )

        # Create a map

        # Add line end points in each state
        for center in city_order:
            marker = Marker(location=center, draggable=False)
            self.m.add_layer(marker);
        # print(self.m.layers)


        # print(line.model_id)
        # Add all line connections
        self.line = line
        self.m.add_layer(self.line)
        return self.m


    def update_map(self, city_order: list):
        """Displays a marker for each location and connects them with lines in the order they are passed in. The last element is connected to the first. """
        if len(city_order) < 2:
            print('update_map input must be of len >=2')
            return
        new_order = city_order + [city_order[0]]

        # print('Change order!', new_order)
        self.line.locations = new_order
            

        


    def __get_states_data(self, path: str):
        data = pandas.read_csv(path, delimiter=',')
        data['name'] = data['name'].str.lower()
        states = list(zip(data.latitude, data.longitude))
        return dict(zip(data.name, states))

        