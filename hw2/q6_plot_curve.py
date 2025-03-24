import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
  df = pd.read_csv(
    'q6_metrics.csv',
    header=None,
    names=['exp_name', 'seed', 'env_step', 'avg_eval_return'],
  )

  exps = df['exp_name'].unique()
  max_steps = df['env_step'].max()
  print(max_steps)
  x_steps = np.linspace(0, max_steps, 10000)

  plt.figure(figsize=(12, 7))
  plt.hlines(1000, 0, max_steps, colors='r')
  for exp in exps:
    exp_data = df[df['exp_name'] == exp]
    interpolated_data = []
    for seed in exp_data['seed'].unique():
      seed_data = np.interp(
        x_steps,
        exp_data[exp_data['seed'] == seed]['env_step'],
        exp_data[exp_data['seed'] == seed]['avg_eval_return'],
        right=np.nan,
      )
      interpolated_data.append(seed_data)

    mean_curve = np.mean(interpolated_data, axis=0)
    std_curve = np.std(interpolated_data, axis=0)

    plt.plot(x_steps, mean_curve, label=exp)
    plt.fill_between(x_steps, mean_curve+std_curve, mean_curve-std_curve, alpha=0.3)

  plt.xlabel('Env Steps')
  plt.ylabel('Average Eval Return (across 5 seeds)')
  plt.legend()
  #plt.tight_layout()
  plt.savefig('q6_curves.png')



