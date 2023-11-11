#Humberto Ivan Ulloa Cardona 
# Make a code that simulates two cars and a colission

#---------------------------------------------------------------------------------------------
# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import mesa
import numpy as np
# Data manipulation and analysis.
import pandas as pd
from autos_model import CarModel, CarAgent, pavimentoAgent, CoolAgent, carrilizquierdoAgent, carrilDerechoAgent
import matplotlib.pylab as plt

def get_choques(model):
    """
    Display a text count of how many crashes have occured.
    """
    return f"Choques: {model.choques}"

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
    
    if isinstance(agent,carrilizquierdoAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True
    
    if isinstance(agent,carrilDerechoAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True
    
    return portrayal



grid = mesa.visualization.CanvasGrid(agent_portrayal,20, 20)
choques_chart = mesa.visualization.ChartModule([{"Label": "choques", "Color": "Black"}])

server = mesa.visualization.ModularServer(
    CarModel,
    [grid, get_choques, choques_chart],
    "Car Model",
    {"width": 20, "height": 20, "num_agents": 3 },

)
server.port = 8521  # the defaul

server.launch()
