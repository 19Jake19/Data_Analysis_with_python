import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df=pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    
    
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    sl,inter,r_val,p_val,std_e=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    
    x1=[]
    y1=[]
    for i in range(1880,2051):
        x1.append(i)
        y1.append(i*sl+inter)

    plt.plot(x1,y1,label='Best',c='red')



    # Create second line of best fit
    
    j=df[df['Year']>1999]
    bl2=linregress(j['Year'],j['CSIRO Adjusted Sea Level'])

    x2=[]
    y2=[]
    for i in range(2000,2051):
        x2.append(i)
        y2.append(i*bl2.slope+bl2.intercept)

    plt.plot(x2,y2,label='Second Best',c='blue')

    
    # Add labels and title

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()