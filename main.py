import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = os.getcwd() + '\\data\\data.csv'
data = pd.read_csv(path)

while True:
    city_input = input("Paste city name or press enter to plot:\n")
    if city_input:
        try:
            # selects city that matches user input
            city = data.loc[data["City"] == city_input]
            city.plot(kind='bar')
            plt.title(city_input)
        except IndexError:
            print("\nCity not detected, make sure string is exact\n")
    else:
        break

plt.show()