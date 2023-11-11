# Humberto Ivan Ulloa Cardona
# Carlos Damian Suarez Bernal
# Diego Andres Figueroa Peart
# Make a code that simulates two cars and a colission

# ---------------------------------------------------------------------------------------------
# Has multi-dimensional arrays and matrices. Has a large collection of
# mathematical functions to operate on these arrays.
import mesa
# Data manipulation and analysis.
from autos_model import CarModel, CarAgent, pavimentoAgent, CoolAgent, carrilizquierdoAgent, carrilDerechoAgent, toretoAgent


def get_pasos(model):
    return f"Pasos: {model.pasos}"


def get_choques(model):
    return f"Choques: {model.choques}"


def get_choquesToreto(model):
    return f"Choques Toreto: {model.toretoCrash}"


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

    if isinstance(agent, toretoAgent):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "purple"
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
pasos_chart = mesa.visualization.ChartModule([{"Label": "pasos", "Color": "Red"}])
choques_chart = mesa.visualization.ChartModule([{"Label": "choques", "Color": "Black"}])
toreto_chart = mesa.visualization.ChartModule([{"Label": "toretoCrash", "Color": "Blue"}])

server = mesa.visualization.ModularServer(
    CarModel,
    [grid,
     get_choques,
     choques_chart,
     get_pasos,
     pasos_chart,
     get_choquesToreto,
     toreto_chart
     ],
    "Car Model",
    {"width": 20, "height": 20, "num_agents": 3},

)
server.port = 8521  # the default

server.launch()
