# Installation
```bash
git clone --branch jiahang/matbench-discovery --depth 1 https://github.com/Jielanlee/OmniMat.git
cd matbench-discovery
uv pip install -e .
```

# Test
```bash
export MATBENCH_DIR=${matbench_data_directory}
python test_matbench.py
```
* Be noted that you should replace `${matbench_data_directory}` by the actual matbench data directory in your own storage. The default data directory is `/mnt/shared-storage-gpfs2/ailab-omnimat-shared/liuzifeng/data/matbench-discovery-main/data/` since the original data source comes from zifeng.
