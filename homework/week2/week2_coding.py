import pandas as pd
import os
from matplotlib import pyplot as plt

data = pd.read_csv('data/coding-environment-exercise.csv')

plt.plot(data.date, data.value)
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation = 45)
plt.show()
