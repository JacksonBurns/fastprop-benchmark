chemprop_train \
--data_path ../qm7_clean.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type regression \
--save_dir output_0 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 0

chemprop_train \
--data_path ../qm7_clean.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type regression \
--save_dir output_1 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 1

chemprop_train \
--data_path ../qm7_clean.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type regression \
--save_dir output_2 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 2

chemprop_train \
--data_path ../qm7_clean.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type regression \
--save_dir output_3 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 3

chemprop_train \
--data_path ../qm7_clean.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type regression \
--save_dir output_4 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 4
