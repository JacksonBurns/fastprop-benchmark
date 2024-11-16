# fastprop-benchmark
Benchmarking [`fastprop`](https://github.com/JacksonBurns/fastprop), [Chemprop](https://github.com/chemprop/chemprop), and [Transformer-CNN](https://github.com/bigchem/transformer-cnn) on various open datasets.

Summary table follows - see below for instructions about reproducing these results.
All reported results are an average across five randomly selected train/val/test splits of 0.70/0.10/0.20, for MAE and RMSE lower is better and for ROC-AUC higher is better.

|    Dataset    | Entries |  Metric | Chemprop | transformer-cnn | fastprop |
|:-------------:|:-------:|:-------:|:--------:|:---------------:|:--------:|
|      HIV      |41,127| ROC-AUC |0.8275+/-0.0150|0.5604+/-0.1301|0.7844+/-0.01989|
|      QM8      |21,786|   MAE   |0.0056+/-0.0001|0.0136+/-0.0004|0.0164+/-0.0002|
|    ToxCast    |8,597| ROC-AUC |          |                 |          |
|     Tox21     |7,831| ROC-AUC |          |                 |          |
|      QM7      |6,834|   MAE   |          |                 |          |
| Lipophilicity |4,200|   RMSE  |          |                 |          |
|      BBBP     |2,050| ROC-AUC |          |                 |          |
|      BACE     |1,513| ROC-AUC |          |                 |          |
|    ClinTox    |1,484| ROC-AUC |          |                 |          |
|     SIDER     |1,427| ROC-AUC |          |                 |          |
|      ESOL     |1,128|   RMSE  |0.6833+/-0.0438|0.7007+/-0.0569|0.805+/-0.152|
|    FreeSolv   |642|   RMSE  |          |                 |          |

# Installation
Conda environment files for the three packages are provided - use `conda env create -f <name>.yml` to create an appropriate environment.

Note that transformer-cnn is not available on any packaging services.
You will need to create the environment as above and then manually download the code.

Benchmark data can be downloaded according to the instructions in `provenance.md`.
`preprocess.py`, if present, prepares the data for running with the three different models.
`postprocess.py` collates model predictions - run after running the below training commands.
Both of these can be run from the environment used to run `fastprop`.

Running the benchmarks can be done with the following command, from the appropriate directory for each benchmark (i.e. go to `benchmarks/esol/fastprop`):
 - `fastprop train config.yml`
 - `. config.sh` _(requires bash)_
 - `. config.sh` _(requires bash)_
