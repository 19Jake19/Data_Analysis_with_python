import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv('fcc-forum-pageviews.csv',index_col='date',parse_dates=True)
# Clean data
bottom=df['value']>=df['value'].quantile(0.025)
top=df['value']<=df['value'].quantile(0.975)

df=df[bottom & top]



def draw_line_plot():
    # Draw line plot
    
    
    df0=df.copy()
    fig,ax=plt.subplots()
    plt.plot(df0,c='red')

    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    
    
    
    df1=df.copy()
    df1=df1.groupby([df1.index.year,df1.index.month]).mean().unstack()

    d=np.arange(12)+1
    e=pd.Series(d,name='ds')
    e=pd.to_datetime(e,format="%m",).dt.month_name().tolist()
    #print (df1.head(3))


    # Draw bar plot

    fig,ax=plt.subplots(figsize=(12,18))
    df1.plot(y='value',kind='bar',ax=ax)
    ax.legend(e,title='Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')








    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
  
    df1=df.copy()
    df1.reset_index(inplace=True)
    df1['year']=[d.year for d in df1.date]
    df1['month']=[d.strftime('%b') for d in df1.date]
  
    mo=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # Draw box plots (using Seaborn)
    
    
    #fig1=plt.figure(figsize=(23,13))
    fig,ax=plt.subplots(ncols=2,figsize=(25,8))
    sns.boxplot(x='year',y='value',data =df1,ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')


    
    sns.boxplot(x='month',y='value',data =df1,order=mo,ax=ax[1])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig