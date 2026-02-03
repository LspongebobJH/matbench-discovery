from pathlib import Path
import pandas as pd
from matbench_discovery.data import Files, download_file
from enum import auto
import os
import builtins
import sys
import functools
from matbench_discovery import PKG_DIR
import yaml
from pathlib import Path
from pymatviz.enums import Key

MATBENCH_DIR = os.environ.get("MATBENCH_DIR", f"/mnt/shared-storage-gpfs2/ailab-omnimat-shared/liuzifeng/data/matbench-discovery-main/data/")

class DataFilesCustomized(Files):
    """Enum of data files with associated file directories and URLs."""

    mp_computed_structure_entries = (
        "mp/2023-02-07-mp-computed-structure-entries.json.gz",
        "https://figshare.com/ndownloader/files/40344436",
    )
    mp_elemental_ref_entries = (
        "mp/2023-02-07-mp-elemental-reference-entries.json.gz",
        "https://figshare.com/ndownloader/files/40387775",
    )
    mp_energies = (
        "mp/2023-01-10-mp-energies.csv.gz",
        "https://figshare.com/ndownloader/files/49083124",
    )
    mp_patched_phase_diagram = (
        "mp/2023-02-07-ppd-mp.pkl.gz",
        "https://figshare.com/ndownloader/files/48241624",
    )
    mp_trj_extxyz = (
        "mp/2024-09-03-mp-trj.extxyz.zip",
        "https://figshare.com/ndownloader/files/49034296",
    )
    # snapshot of every task (calculation) in MP as of 2023-03-16 (14 GB)
    all_mp_tasks = (
        "mp/2023-03-16-all-mp-tasks.zip",
        "https://figshare.com/ndownloader/files/43350447",
    )

    wbm_computed_structure_entries = (
        "wbm/2022-10-19-wbm-computed-structure-entries.json.bz2",
        "https://figshare.com/ndownloader/files/40344463",
    )
    wbm_relaxed_atoms = (
        "wbm/2024-08-04-wbm-relaxed-atoms.extxyz.zip",
        "https://figshare.com/ndownloader/files/48169600",
    )
    wbm_initial_structures = (
        "wbm/2022-10-19-wbm-init-structs.json.bz2",
        "https://figshare.com/ndownloader/files/40344466",
    )
    wbm_initial_atoms = (
        "wbm/2024-08-04-wbm-initial-atoms.extxyz.zip",
        "https://figshare.com/ndownloader/files/48169597",
    )
    wbm_cses_plus_init_structs = (
        "wbm/2022-10-19-wbm-computed-structure-entries+init-structs.json.bz2",
        "https://figshare.com/ndownloader/files/40344469",
    )
    wbm_summary = (
        "wbm/2023-12-13-wbm-summary.csv.gz",
        "https://figshare.com/ndownloader/files/44225498",
    )
    alignn_checkpoint = (
        "2023-06-02-pbenner-best-alignn-model.pth.zip",
        "https://figshare.com/ndownloader/files/41233560",
    )
    mp_trj = (
        "mp/2022-09-16-mp-trj.json",
        "https://figshare.com/ndownloader/files/41619375",
    )

    def __str__(self) -> str:
        """File path associated with the file URL. Use str(DataFiles.some_key) if you
        want the absolute file path without auto-downloading the file if it doesn't
        exist yet, e.g. for use in script that generates the file in the first place.
        """
        # return f"{type(self).base_dir}/{self._rel_path}"  # type: ignore[attr-defined]
        # return f"{self.data_dir}/{self.rel_path}"
        return f"/mnt/shared-storage-gpfs2/ailab-omnimat-shared/liuzifeng/data/matbench-discovery-main/data/{self.rel_path}"

    @property
    def path(self) -> str:
        """Return the file path associated with the file URL if it exists, otherwise
        download the file first, then return the path.
        """
        key, url, rel_path = self.name, self._url, self._rel_path  # type: ignore[attr-defined]
        # abs_path = f"{type(self).base_dir}/{rel_path}"
        abs_path = f"/mnt/shared-storage-gpfs2/ailab-omnimat-shared/liuzifeng/data/matbench-discovery-main/data/{rel_path}"
        if not os.path.isfile(abs_path):
            is_ipython = hasattr(__builtins__, "__IPYTHON__")
            # default to 'y' if not in interactive session, and user can't answer
            answer = (
                input(
                    f"{abs_path!r} associated with {key=} does not exist. Download it "
                    "now? This will cache the file for future use. [y/n] "
                )
                if is_ipython or sys.stdin.isatty()
                else "y"
            )
            if answer.lower().strip() == "y":
                if not is_ipython:
                    print(f"Downloading {key!r} from {url} to {abs_path} for caching")
                download_file(abs_path, url)
        return abs_path
    
class Logger:
    def __init__(self, log_path: str):
        assert log_path is not None, "Logger requires a valid log_path"
        self.log_path = log_path
        self.df_path = Path(log_path).with_suffix(".csv")


    def __call__(self, msg: str):
        print(msg)
        log_path = Path(self.log_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
            f.flush()

    def log_df(self, df: pd.DataFrame):
        df.to_csv(self.df_path, index=False)