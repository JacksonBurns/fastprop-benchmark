from statistics import mean, stdev

import pandas as pd
from sklearn.metrics import roc_auc_score

aucs = []

for seed in range(5):
    truth = pd.read_csv(f"bbbp_tcnn_test_{seed}.csv")
    pred = pd.read_csv(f"transformercnn/results_{seed}.csv")
    # sometimes tcnn errors
    drop_mask = pred["property"] == "error"
    truth = truth.drop(truth[drop_mask].index)
    pred = pred.drop(pred[drop_mask].index)
    aucs.append(roc_auc_score(truth["target"], pred["property"]))

print(f"Transformer-CNN ROC-AUC: {mean(aucs):.4f}+/-{stdev(aucs):.4f}")

aucs = []

for seed in range(5):
    result = pd.read_csv(f"chemprop/output_{seed}/test_scores.csv")
    aucs.append(result.iloc[0]["Fold 0 auc"])

print(f"Chemprop ROC-AUC: {mean(aucs):.4f}+/-{stdev(aucs):.4f}")
