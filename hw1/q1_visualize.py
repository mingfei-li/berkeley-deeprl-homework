import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('q1_logs.csv')
x = df['n_steps']
y = df['Eval_AverageReturn']
error = df['Eval_StdReturn']
plt.plot(x, y, 'b-', label='Data')
plt.fill_between(x, y - error, y + error, alpha=0.3, color='b', label='Error')
plt.xlabel('num_agent_train_steps_per_iter')
plt.ylabel('Eval_AverageReturn')
plt.savefig('bc_hyperparameter_tuning.jpg')