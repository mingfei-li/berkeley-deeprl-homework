import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('q2_logs.csv')
ref_y = df.loc[df['mode'] == 'train', 'avg_return'].values[0]
ref_error = df.loc[df['mode'] == 'train', 'std_return'].values[0]

df = df.drop(df[df['mode'] == 'train'].index)
x = df['iter']
y = df['avg_return']
error = df['std_return']
plt.plot(x, y, 'b-', label='Behavior Clone Agent')
plt.fill_between(x, y - error, y + error, alpha=0.3, color='b')
plt.xlabel('Dagger Iter')
plt.ylabel('Average Return')

plt.hlines(xmin=x.values[0], xmax=x.values[-1], y=ref_y, color='r', label='Expert policy')
plt.fill_between(x, ref_y - ref_error, ref_y + ref_error, color='r', alpha=0.3)

plt.legend()
plt.savefig('dagger.jpg')