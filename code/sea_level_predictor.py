import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

def draw_plot():
	df=pd.read_csv('epa-sea-level.csv')
	plt.figure(figsize=(16,8))
	plt.scatter('Year','CSIRO Adjusted Sea Level',label='ORG', data =df)
	reg=st.linregress(df.Year,df['CSIRO Adjusted Sea Level'])
	x_1880 = pd.Series(range(1880, 2051, 1), dtype='float')
	plt.plot(x_1880,reg.intercept + reg.slope *x_1880,'r',label='best fit')

	x_2000=pd.Series(range(2000,2051,1),dtype='float')
	new_df=df[df['Year']>=2000]
	new_reg=st.linregress(new_df['Year'],new_df['CSIRO Adjusted Sea Level'])
	plt.plot(x_2000, new_reg.intercept +new_reg.slope * x_2000,'g',label='new data')

	plt.xlabel("Year")
	plt.ylabel("Sea Level (inches)")
	plt.title("Rise in Sea Level")
	plt.savefig('sea_level_plot.png')
	return plt.gca()

