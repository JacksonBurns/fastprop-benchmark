# fastprop-benchmark
Benchmarking [`fastprop`](https://github.com/JacksonBurns/fastprop), [Chemprop](https://github.com/chemprop/chemprop), and [Transformer-CNN](https://github.com/bigchem/transformer-cnn) on various open datasets.

Summary table follows - see below for instructions about reproducing these results.
All reported results are an average across five randomly selected train/val/test splits of 0.70/0.10/0.20, for MAE and RMSE lower is better and for ROC-AUC higher is better.
The Tukey test is used to check for pairwise statistical differences between the three models.
The best performing models which are statistically significantly different from the others are shown in bold.

|    Dataset    | Entries |  Metric | Chemprop | transformer-cnn | fastprop |
|:-------------:|:-------:|:-------:|:--------:|:---------------:|:--------:|
|      HIV      |41,127| ROC-AUC |__0.8275+/-0.0150__|0.5604+/-0.1301|__0.7844+/-0.01989__|
|      QM8      |21,786|   MAE   |__0.0056+/-0.0001__|0.0136+/-0.0004|0.0164+/-0.0002|
|      QM7      |6,834|   MAE   |68.10+/-2.70|62.40+/-2.20|__57.08+/-2.76__|
| Lipophilicity |4,200|   RMSE  |0.5974+/-0.0331|__0.7019+/-0.0298__|__0.7356+/-0.0196__|
|      BBBP     |2,050| ROC-AUC |0.9183+/-0.0157|__0.9650+/-0.0032__|0.9030+/-0.0131|
|      BACE     |1,513| ROC-AUC |0.8558+/-0.0103|__0.8991+/-0.0163__|__0.8781+/-0.0154__|
|    ClinTox    |1,484| ROC-AUC |__0.8770+/-0.0346__|__0.9814+/-0.0083__|0.6377+/-0.1347|
|     SIDER     |1,427| ROC-AUC |__0.6621+/-0.0385__|__0.6119+/-0.0307__|__0.6287+/-0.0164__|
|     Tox24     |1,212|   RMSE  |__26.27+/-1.93__|__25.00+/-1.07__|__27.42+/-1.70__|
|      ESOL     |1,128|   RMSE  |__0.6833+/-0.0438__|__0.7007+/-0.0569__|__0.805+/-0.152__|
|    FreeSolv   |642|   RMSE  |__1.32+/-0.23__|__1.50+/-0.23__|__1.29+/-0.15__|

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
