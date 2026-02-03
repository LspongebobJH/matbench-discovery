from matbench_discovery.data import ase_atoms_from_zip, DataFilesCustomized
# from utils_matbench import DataFilesCustomized
import pandas as pd

print("Loading WBM summary data")

# df_wbm = pd.read_csv(DataFiles.wbm_summary.path)
df_wbm = pd.read_csv(DataFilesCustomized.wbm_summary.path)
# confirm test set size
assert df_wbm.shape == (256_963, 18)
# available columns in WBM summary data
assert tuple(df_wbm) == (
    "material_id",
    "formula",
    "n_sites",
    "volume",
    "uncorrected_energy",
    "e_form_per_atom_wbm",
    "e_above_hull_wbm",
    "bandgap_pbe",
    "wyckoff_spglib_initial_structure",
    "uncorrected_energy_from_cse",
    "e_correction_per_atom_mp2020",
    "e_correction_per_atom_mp_legacy",
    "e_form_per_atom_uncorrected",
    "e_form_per_atom_mp2020_corrected",
    "e_above_hull_mp2020_corrected_ppd_mp",
    "site_stats_fingerprint_init_final_norm_diff",
    "wyckoff_spglib",
    "unique_prototype"
)

# WBM initial structures in pymatgen JSON format
print("Loading WBM initial structures")
df_init_structs = pd.read_json(DataFilesCustomized.wbm_initial_structures.path, lines=True)
assert tuple(df_init_structs) == ("material_id", "formula_from_cse", "initial_structure")

# WBM initial structures as ASE Atoms
print("Loading WBM initial structures as ASE Atoms")
wbm_init_atoms = ase_atoms_from_zip(DataFilesCustomized.wbm_initial_atoms.path)
assert len(wbm_init_atoms) == 256_963

print("All data loaded successfully")