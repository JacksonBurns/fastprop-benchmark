import pandas as pd

IN_NAMES = ["E1-CC2", "E2-CC2", "f1-CC2", "f2-CC2", "E1-PBE0", "E2-PBE0", "f1-PBE0", "f2-PBE0", "E1-CAM", "E2-CAM", "f1-CAM", "f2-CAM"]
OUT_NAMES = [f"target_{i}" for i in range(len(IN_NAMES))]

df = pd.read_csv("qm8.csv")
df[["smiles"] + IN_NAMES].to_csv("qm8_12target.csv", header=["smiles"] + OUT_NAMES, index=False)

# manual splitting for the transformer-cnn architecture
for seed in range(5):
    train = df.sample(frac=0.80, random_state=seed)
    test = df[~df.index.isin(train.index)]
    train[["smiles"] + IN_NAMES].to_csv(f"qm8_12target_tcnn_train_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
    test[["smiles"] + IN_NAMES].to_csv(f"qm8_12target_tcnn_test_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
