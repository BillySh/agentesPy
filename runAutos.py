#Humberto Ivan Ulloa Cardona 
# Make a code that simulates two cars and a colission

#---------------------------------------------------------------------------------------------
# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import mesa
import numpy as np
# Data manipulation and analysis.
import pandas as pd
from autos_model import CarModel, CarAgent, pavimentoAgent, CoolAgent
import matplotlib.pylab as plt

def agent_portrayal(agent):
    portrayal = {}

    if isinstance(agent, CarAgent):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5
        portrayal["Filled"] = True

    if isinstance(agent, CoolAgent):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5
        portrayal["Filled"] = True

    if isinstance(agent, pavimentoAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "black"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True
    
    return portrayal




grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)

server = mesa.visualization.ModularServer(
    CarModel, [grid], "Car Model", {"width": 10, "height": 10, "num_agents": 1 }
)
server.port = 8521  # the defaul

server.launch()