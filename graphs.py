#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CarModel_Data.csv")

car_df = df[df['AgentType'] == 'CarAgent']

datos_agrupados = car_df.groupby('iteration').mean()

plt.figure(figsize=(10, 6))
# plt.plot(datos_agrupados['pasos'], label='Pasos')
plt.plot(datos_agrupados['choques'], label='Choques')
plt.title('Choques por iteración')
plt.xlabel('Iteración')
plt.ylabel('Cantidad')
plt.legend()
plt.show()
