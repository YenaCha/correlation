import pandas as pd
import plotly.express as px
import numpy as np
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 106/tv.csv')
tv = df['Size of TV'].tolist()
time = df['Average'].tolist()
d = {'x':tv, 'y':time}
correlation = np.corrcoef(d['x'], d['y'])
print(correlation)
graphic = px.scatter(x = tv, y = time)
graphic.show()