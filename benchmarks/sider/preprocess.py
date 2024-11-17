import pandas as pd

IN_NAMES = [
    "Hepatobiliary disorders",
    "Metabolism and nutrition disorders",
    "Product issues",
    "Eye disorders",
    "Investigations",
    "Musculoskeletal and connective tissue disorders",
    "Gastrointestinal disorders",
    "Social circumstances",
    "Immune system disorders",
    "Reproductive system and breast disorders",
    "Neoplasms benign, malignant and unspecified (incl cysts and polyps)",
    "General disorders and administration site conditions",
    "Endocrine disorders",
    "Surgical and medical procedures",
    "Vascular disorders",
    "Blood and lymphatic system disorders",
    "Skin and subcutaneous tissue disorders",
    "Congenital, familial and genetic disorders",
    "Infections and infestations",
    "Respiratory, thoracic and mediastinal disorders",
    "Psychiatric disorders",
    "Renal and urinary disorders",
    "Pregnancy, puerperium and perinatal conditions",
    "Ear and labyrinth disorders",
    "Cardiac disorders",
    "Nervous system disorders",
    "Injury, poisoning and procedural complications",
]
OUT_NAMES = [f"target_{i}" for i in range(len(IN_NAMES))]

df = pd.read_csv("sider.csv")
df[["smiles"] + IN_NAMES].to_csv("sider_clean.csv", header=["smiles"] + OUT_NAMES, index=False)

# manual splitting for the transformer-cnn architecture
for seed in range(5):
    train = df.sample(frac=0.80, random_state=seed)
    test = df[~df.index.isin(train.index)]
    train[["smiles"] + IN_NAMES].to_csv(f"sider_clean_tcnn_train_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
    test[["smiles"] + IN_NAMES].to_csv(f"sider_clean_tcnn_test_{seed}.csv", header=["smiles"] + OUT_NAMES, index=False)
