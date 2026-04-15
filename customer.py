import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('customer.csv') 
df['CTR'] = df['clicks'] / df['views']


sns.barplot(x='section', y='CTR', data=df)

plt.title('CTR by Section')
plt.show() 
