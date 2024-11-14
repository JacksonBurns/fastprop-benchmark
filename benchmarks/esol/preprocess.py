import pandas as pd

df = pd.read_csv("delaney-processed.csv")
df[["smiles", "measured log solubility in mols per litre"]].to_csv("esol.csv", header=["smiles", "target"], index=False)

# manual splitting for the transformer-cnn architecture
for seed in range(5):
    train = df.sample(frac=0.80, random_state=seed)
    test = df[~df.index.isin(train.index)]
    train[["smiles", "measured log solubility in mols per litre"]].to_csv(f"esol_tcnn_train_{seed}.csv", header=["smiles", "target"], index=False)
    test[["smiles", "measured log solubility in mols per litre"]].to_csv(f"esol_tcnn_test_{seed}.csv", header=["smiles", "target"], index=False)
