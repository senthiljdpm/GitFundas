# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 07:02:13 2017
@author: senthil
"""
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')
