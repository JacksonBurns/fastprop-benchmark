import pandas as pd

IN_NAMES = ["exp"]
OUT_NAMES = ["target"]

df = pd.read_csv("Lipophilicity.csv")
df[["smiles"] + IN_NAMES].to_csv("lipo.csv", header=["smiles"] + OUT_NAMES, index=False)

# manual splitting for the transformer-cnn architecture
for seed in range(5):
    train = df.sample(frac=0.80, random_state=seed)
    test = df[~df.index.isin(train.index)]
    train[["smiles"] + IN_NAMES].to_csv(f"lipo_tcnn_train_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
    test[["smiles"] + IN_NAMES].to_csv(f"lipo_tcnn_test_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
