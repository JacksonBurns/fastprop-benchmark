#!/bin/bash

TCNN="python ../../../transformer-cnn-7009a997e9fe626913e7e28030d3e92e0eeba818/transformer-cnn.py"

for SEED in {0..4}; do
    cat > train_config_$SEED.cfg << EOL
[Task]
train_mode = True
model_file = model_$SEED.tar
train_data_file = ../bbbp_tcnn_train_$SEED.csv
[Details]
retrain = False
canonize = False
gpu = 0
seed = 0
n_epochs = 30
batch_size = 16
EOL
    
    $TCNN train_config_$SEED.cfg

    cat > apply_config_$SEED.cfg << EOL
[Task]
train_mode = False
model_file = model_$SEED.tar
result_file = results_$SEED.csv
apply_data_file = ../bbbp_tcnn_test_$SEED.csv
[Details]
retrain = False
canonize = False
gpu = 0
seed = 0
EOL

    $TCNN apply_config_$SEED.cfg

done