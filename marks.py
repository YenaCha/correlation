import pandas as pd
import plotly.express as px
import numpy as np
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 106/marks.csv')
marks = df['Marks In Percentage'].tolist()
present = df['Days Present'].tolist()
d = {'x':present, 'y':marks}
correlation = np.corrcoef(d['x'],d['y'])
print(correlation)
graph = px.scatter(x = present, y = marks)
graph.show()