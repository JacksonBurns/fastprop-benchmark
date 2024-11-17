from statistics import mean, stdev

import pandas as pd
from sklearn.metrics import mean_absolute_error

maes = []

for seed in range(5):
    truth = pd.read_csv(f"qm7_clean_tcnn_test_{seed}.csv")
    pred = pd.read_csv(f"transformercnn/results_{seed}.csv")
    maes.append(mean_absolute_error(truth["target"], pred["property"]))

print(f"Transformer-CNN MAE: {mean(maes):.4f}+/-{stdev(maes):.4f}")

maes = []

for seed in range(5):
    result = pd.read_csv(f"chemprop/output_{seed}/test_scores.csv")
    maes.append(result.iloc[0]["Fold 0 mae"])

print(f"Chemprop MAE: {mean(maes):.4f}+/-{stdev(maes):.4f}")
