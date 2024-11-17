from statistics import mean, stdev

import pandas as pd
from sklearn.metrics import root_mean_squared_error

rmses = []

for seed in range(5):
    truth = pd.read_csv(f"tox24_tcnn_test_{seed}.csv")
    pred = pd.read_csv(f"transformercnn/results_{seed}.csv")
    rmses.append(root_mean_squared_error(truth["target"], pred["property"]))

print(f"Transformer-CNN RMSE: {mean(rmses):.4f}+/-{stdev(rmses):.4f}")

rmses = []

for seed in range(5):
    result = pd.read_csv(f"chemprop/output_{seed}/test_scores.csv")
    rmses.append(result.iloc[0]["Fold 0 rmse"])

print(f"Chemprop RMSE: {mean(rmses):.4f}+/-{stdev(rmses):.4f}")
