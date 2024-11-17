chemprop_train \
--data_path ../bbbp.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type classification \
--save_dir output_0 \
--split_sizes 0.7 0.1 0.2 \
--metric auc \
--extra_metrics accuracy \
--seed 0

chemprop_train \
--data_path ../bbbp.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type classification \
--save_dir output_1 \
--split_sizes 0.7 0.1 0.2 \
--metric auc \
--extra_metrics accuracy \
--seed 1

chemprop_train \
--data_path ../bbbp.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type classification \
--save_dir output_2 \
--split_sizes 0.7 0.1 0.2 \
--metric auc \
--extra_metrics accuracy \
--seed 2

chemprop_train \
--data_path ../bbbp.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type classification \
--save_dir output_3 \
--split_sizes 0.7 0.1 0.2 \
--metric auc \
--extra_metrics accuracy \
--seed 3

chemprop_train \
--data_path ../bbbp.csv \
--smiles_columns smiles \
--target_columns target \
--dataset_type classification \
--save_dir output_4 \
--split_sizes 0.7 0.1 0.2 \
--metric auc \
--extra_metrics accuracy \
--seed 4