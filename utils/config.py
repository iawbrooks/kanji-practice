import json
from pathlib import Path

import pandas as pd
import numpy as np
import yaml


ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"


def load_all_kanji() -> pd.DataFrame:
    fp = DATA_DIR / "kanji.json"
    with fp.open('rb') as f:
        kanji: dict[str, dict[str, str]] = json.load(f)
    
    # Create dataframe
    columns = ["kanji"] + list(next(iter(kanji.values())).keys())
    index = np.arange(len(kanji))
    kanji_df = pd.DataFrame(index=index, columns=columns, dtype=object)

    # Convert
    for i, (kj, kj_data) in enumerate(kanji.items()):
        kanji_df.at[i, "kanji"] = kj
        for k, v in kj_data.items():
            kanji_df.at[i, k] = v

    return kanji_df


def load_all_kana() -> dict:
    fp = DATA_DIR / "kana.yaml"
    with fp.open('rb') as f:
        kana = yaml.safe_load(f)
    return kana
