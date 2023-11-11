#!/usr/bin/env python3

import mesa
import pandas as pd
from autos_model import CarModel, CarAgent, pavimentoAgent, CoolAgent, carrilizquierdoAgent, carrilDerechoAgent

batch_run_params = {
    "width": [20],
    "height": [20],
    "num_agents": [10],
}

data = mesa.batch_run(
    CarModel,
    batch_run_params,
    iterations=100,  # Number of iterations for each parameter combination
    max_steps=150,  # Number of steps for each run
)


df = pd.DataFrame(data)

df.to_csv("CarModel_Data.csv", index=False)
