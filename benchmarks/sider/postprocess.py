from statistics import mean, stdev

import pandas as pd
from sklearn.metrics import roc_auc_score

aucs = []

TARGETS = [f"target_{i}" for i in range(27)]

for seed in range(5):
    truth = pd.read_csv(f"sider_clean_tcnn_test_{seed}.csv")
    pred = pd.read_csv(f"transformercnn/results_{seed}.csv")
    pred = pred.rename(columns={"property": "target_0"})
    aucs.append(roc_auc_score(truth[TARGETS], pred[TARGETS]))

print(f"Transformer-CNN ROC-AUC: {mean(aucs):.4f}+/-{stdev(aucs):.4f}")

aucs = []

for seed in range(5):
    result = pd.read_csv(f"chemprop/output_{seed}/test_scores.csv")
    aucs.append(result.iloc[0]["Fold 0 auc"])

print(f"Chemprop ROC-Auc: {mean(aucs):.4f}+/-{stdev(aucs):.4f}")
