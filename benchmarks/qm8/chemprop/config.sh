chemprop_train \
--data_path ../qm8_12target.csv \
--smiles_columns smiles \
--target_columns target_0 target_1 target_2 target_3 target_4 target_5 target_6 target_7 target_8 target_9 target_10 target_11 \
--dataset_type regression \
--save_dir output_0 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 0

chemprop_train \
--data_path ../qm8_12target.csv \
--smiles_columns smiles \
--target_columns target_0 target_1 target_2 target_3 target_4 target_5 target_6 target_7 target_8 target_9 target_10 target_11 \
--dataset_type regression \
--save_dir output_1 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 1

chemprop_train \
--data_path ../qm8_12target.csv \
--smiles_columns smiles \
--target_columns target_0 target_1 target_2 target_3 target_4 target_5 target_6 target_7 target_8 target_9 target_10 target_11 \
--dataset_type regression \
--save_dir output_2 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 2

chemprop_train \
--data_path ../qm8_12target.csv \
--smiles_columns smiles \
--target_columns target_0 target_1 target_2 target_3 target_4 target_5 target_6 target_7 target_8 target_9 target_10 target_11 \
--dataset_type regression \
--save_dir output_3 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 3

chemprop_train \
--data_path ../qm8_12target.csv \
--smiles_columns smiles \
--target_columns target_0 target_1 target_2 target_3 target_4 target_5 target_6 target_7 target_8 target_9 target_10 target_11 \
--dataset_type regression \
--save_dir output_4 \
--split_sizes 0.7 0.1 0.2 \
--metric mae \
--extra_metrics rmse \
--seed 4
