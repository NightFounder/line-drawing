import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.title("midPoint line Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def midPoint(X1,Y1,X2,Y2):

  dx = X2 - X1
  dy = Y2 - Y1


  d = dy - (dx/2)
  x = X1
  y = Y1


  #print("X: ",x, "\tY: ", y)
  x_coorinates = []
  y_coorinates = []

  while (x < X2):
    x=x+1

    if(d < 0):
      d = d + dy

    else:
      d = d + (dy - dx)
      y=y+1
    #print("X: ",x, "\tY: ", y)
    print("X: ",x, "\tY: ", y)
    x_coorinates.append(x)
    y_coorinates.append(y)
  fig = plt.figure(figsize=(10, 4))
  plt.title("Midpoint Line Algorithm")
  plt.xlabel("X-Axis")
  plt.ylabel("Y-Axis")
  plt.plot(x_coorinates, y_coorinates, marker="o", markersize=1, markerfacecolor="green")
  plt.show()
  st.pyplot(fig)
  


if __name__=='__main__':
  X1 = 10
  Y1 = 10
  X2 = 60
  Y2 = 60
  midPoint(X1, Y1, X2, Y2)
