# Installation
```bash
git clone --branch jiahang/matbench-discovery --depth 1 https://github.com/Jielanlee/OmniMat.git OmniMat-matbench-discovery
cd OmniMat-matbench-discovery/matbench-discovery
uv pip install -e .
```

# Test
```bash
export MATBENCH_DIR=${matbench_data_directory}
python test_matbench.py
```
* Be noted that you should replace `${matbench_data_directory}` by the actual matbench data directory in your own storage. The default data directory is `/mnt/shared-storage-gpfs2/ailab-omnimat-shared/liuzifeng/data/matbench-discovery-main/data/` since the original data source comes from zifeng.

# Test with mattersim
```bash
# You need to install mattersim as a package first by
cd ~
git clone --branch jiahang/mattersim_jiahang --depth 1 https://github.com/Jielanlee/OmniMat.git OmniMat-mattersim-jiahang
cd OmniMat-mattersim-jiahang
cd mattersim_jiahang/packages/mattersim # mattersim package on H200. If you are installing it on muxi GPU, please execute `cd mattersim_jiahang/packages/mattersim-mx` instead
uv pip install -e .

# Then go to mattersim working project
cd ~
git clone --branch jiahang/mattersim_work --depth 1 https://github.com/Jielanlee/OmniMat.git OmniMat-mattersim-work
cd OmniMat-mattersim-work

python benchmark_matbench.py --checkpoint_path ~/OmniMat-mattersim-jiahang/pretrained_models/mattersim-v1.0.0-1M.pth --log_path ./test.log
```
