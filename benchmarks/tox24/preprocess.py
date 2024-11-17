import pandas as pd

IN_NAMES = ["activity"]
OUT_NAMES = ["target"]

df = pd.read_csv("all_smiles_data.csv")
df = df.dropna(subset=["activity"])
df = df.rename(columns={"pubchem_smiles_no_salts": "smiles"})
df[["smiles"] + IN_NAMES].to_csv("tox24.csv", header=["smiles"] + OUT_NAMES, index=False)

# manual splitting for the transformer-cnn architecture
for seed in range(5):
    train = df.sample(frac=0.80, random_state=seed)
    test = df[~df.index.isin(train.index)]
    train[["smiles"] + IN_NAMES].to_csv(f"tox24_tcnn_train_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
    test[["smiles"] + IN_NAMES].to_csv(f"tox24_tcnn_test_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
