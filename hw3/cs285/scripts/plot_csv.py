import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
  "eval_returns.csv",
  header=None,
  names=["exp_name", "step", "eval_return"],
)

exps = df["exp_name"].unique()
plt.figure(figsize=(12, 7))
for exp in exps:
  exp_data = df[df["exp_name"] == exp]
  plt.plot(exp_data["step"], exp_data["eval_return"], label=exp)

plt.xlabel("Env Steps")
plt.ylabel("Eval Returns")
plt.legend()
plt.tight_layout()
plt.savefig('eval_return.png')
