import plotly.express as px
import json

data = []
with open('places/default.json') as json_file:
    data = json.load(json_file)

nether_highways = []
with open('places/nether.json') as json_file:
    nether_highways = json.load(json_file)

SIZE_MAX = 25

X = list(map(lambda row: row["x"], data))
Z = list(map(lambda row: row["z"], data))
sizes = list(map(lambda row: row["size"], data))
text = list(map(lambda row: row["symbol"], data))
symbols = list(map(lambda row: row["type"] if "type" in row else "other", data))
colors = list(map(lambda row: row["color"] if "color" in row else "blue", data))

class ContextManager(object):

    def __init__(self, configs):
        self.config = configs
        ## TODO : query runner stuff

    def figure(self):
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
        for route in nether_highways:
            fig.add_shape(
                type="line",
                x0=route["x0"],
                x1=route["x1"],
                y0=route["z0"],
                y1=route["z1"],
                line_width=route["line_width"],
                line_color=route["line_color"],
                line_dash=route["line_dash"]
            )
        fig.show()

    def read_coords(self):
        print("Reading coords")

    def add_coords(self):
        pass
