import pandas as pd

OUT_COLS = ["smiles", "CT_TOX"]
HEADER = ["smiles", "target"]

df = pd.read_csv("clintox.csv")
df[OUT_COLS].to_csv("clintox_clean.csv", header=HEADER, index=False)

# manual splitting for the transformer-cnn architecture
for seed in range(5):
    train = df.sample(frac=0.80, random_state=seed)
    test = df[~df.index.isin(train.index)]
    train[OUT_COLS].to_csv(f"clintox_clean_tcnn_train_{seed}.csv", header=HEADER, index=False)
    test[OUT_COLS].to_csv(f"clintox_clean_tcnn_test_{seed}.csv", header=HEADER, index=False)
