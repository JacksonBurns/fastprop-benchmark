import pandas as pd

IN_NAMES = ["u0_atom"]
OUT_NAMES = ["target"]

df = pd.read_csv("qm7.csv")
df[["smiles"] + IN_NAMES].to_csv("qm7_clean.csv", header=["smiles"] + OUT_NAMES, index=False)

# manual splitting for the transformer-cnn architecture
for seed in range(5):
    train = df.sample(frac=0.80, random_state=seed)
    test = df[~df.index.isin(train.index)]
    train[["smiles"] + IN_NAMES].to_csv(f"qm7_clean_tcnn_train_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
    test[["smiles"] + IN_NAMES].to_csv(f"qm7_clean_tcnn_test_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
