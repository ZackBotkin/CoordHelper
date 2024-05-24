import plotly.express as px
import json
from helper.src.io.query_runner import QueryRunner


## THIS goes away eventually
data = []
with open('places/default.json') as json_file:
    data = json.load(json_file)

nether_highways = []
with open('places/nether.json') as json_file:
    nether_highways = json.load(json_file)

SIZE_MAX = 25

class ContextManager(object):

    def __init__(self, configs):
        self.config = configs
        self.query_runner = QueryRunner(configs)
        self.query_runner.create_all_tables()

    def figure(self):

        X = []
        Y = []
        Z = []
        sizes = []
        text = []
        symbols = []
        colors = []

        all_locations = self.query_runner.get_all_locations()
        for location in all_locations:
            text.append(location[0])
            X.append(location[1])
            Y.append(location[2])
            Z.append(location[3])
            symbols.append(location[4])
            colors.append(location[5])
            sizes.append(location[6])

        fig = px.scatter(
            title="The Overworld",
            x=X,
            y=Z,
            size=sizes,
            size_max=SIZE_MAX,
            text=text,
            symbol=symbols,
            color=colors
        )
        fig.add_vline(x=0, line_width=5, line_dash="dash")
        fig.add_hline(y=0, line_width=5, line_dash="dash")

        all_nether_routes = self.query_runner.get_all_nether_routes()
        for route in all_nether_routes:
            fig.add_shape(
                type="line",
                x0=route[0],
                y0=route[1],
                x1=route[2],
                y1=route[3],
                line_width=route[4],
                line_color=route[5],
                line_dash=route[6]
            )

        fig.show()

    def read_coords(self):
        print("Reading coords")

    def add_coords(self):
        pass

    def migrate_data(self):
        for location in data:
            self.query_runner.insert_location(
                location['symbol'],
                location['x'],
                0,  ## y coord i have not saved
                location['z'],
                location['type'],
                location['color'],
                location['size']
            )

        for route in nether_highways:
            self.query_runner.insert_nether_route(
                route['x0'],
                route['z0'],
                route['x1'],
                route['z1'],
                route['line_width'],
                route['line_color'],
                route['line_dash']
            )
