from statistics import mean, stdev

import pandas as pd
from sklearn.metrics import mean_absolute_error

maes = []

for seed in range(5):
    truth = pd.read_csv(f"qm8_12target_tcnn_test_{seed}.csv")
    pred = pd.read_csv(f"transformercnn/results_{seed}.csv")
    maes.append(
        mean_absolute_error(
            truth[
                [
                    "target_0",
                    "target_1",
                    "target_2",
                    "target_3",
                    "target_4",
                    "target_5",
                    "target_6",
                    "target_7",
                    "target_8",
                    "target_9",
                    "target_10",
                    "target_11",
                ]
            ],
            pred[
                [
                    "property",
                    "target_1",
                    "target_2",
                    "target_3",
                    "target_4",
                    "target_5",
                    "target_6",
                    "target_7",
                    "target_8",
                    "target_9",
                    "target_10",
                    "target_11",
                ]
            ],
        )
    )

print(f"Transformer-CNN MAE: {mean(maes):.4f}+/-{stdev(maes):.4f}")

maes = []

for seed in range(5):
    result = pd.read_csv(f"chemprop/output_{seed}/test_scores.csv")
    maes.append(result.iloc[0]["Fold 0 mae"])

print(f"Chemprop MAE: {mean(maes):.4f}+/-{stdev(maes):.4f}")
