import os
import sys
import pandas as pd
import numpy as np
import json
from config import *

if __name__ == "__main__":

    for path, label in [(FIT_NOTES_PATH, "FIT_NOTES_PATH"), (MAP_PATH, "MAP_PATH")]:
        if not os.path.isfile(path):
            sys.exit(f"{label} not found: {path} (check config.py)")

    with open(MAP_PATH, 'r', encoding='utf-8') as f:
        map_fn2strong = json.load(f)

    df_fn = pd.read_csv(FIT_NOTES_PATH)

    df_fn_mod = df_fn.copy()
    df_fn_mod = df_fn_mod.sort_values("Date")
    df_fn_mod["Workout #"] = df_fn_mod["Date"].rank(method="dense").astype(int)

    df_fn_mod['Date'] = df_fn_mod['Date'] + ' ' + DEFAULT_TRAINING_TIME

    df_fn_mod['Workout Name'] = DEFAULT_WORKOUT_NAME

    df_fn_mod['Duration'] = DEFAULT_DURATION

    df_fn_mod["Exercise Name"] = df_fn_mod["Exercise"].map(map_fn2strong)
    unmapped = sorted(df_fn_mod.loc[df_fn_mod["Exercise Name"].isna(), "Exercise"].unique())
    if unmapped:
        print(f"Unmapped exercises (set to 'Other'): {unmapped}")
    df_fn_mod["Exercise Name"] = df_fn_mod["Exercise Name"].fillna('Other')

    df_fn_mod['Set Order'] = (df_fn_mod.groupby(['Date', 'Exercise Name']).cumcount() + 1).astype(object)

    df_fn_mod['Reps'] = df_fn_mod['Reps'].astype(float)

    df_fn_mod['RPE'] = np.nan

    df_fn_mod['Distance'] = np.nan

    df_fn_mod['Seconds'] = np.nan

    df_fn_mod['Notes'] = df_fn_mod['Comment']

    df_fn_mod['Workout Notes'] = np.nan

    df_fn_mod_rest = df_fn_mod.copy()
    df_fn_mod['training'] = True
    df_fn_mod_rest['training'] = False
    df_fn_mod = pd.concat([df_fn_mod, df_fn_mod_rest])
    df_fn_mod["index"] = df_fn_mod.index
    df_fn_mod = df_fn_mod.sort_values(["index", "training"], ascending=[True, False])
    df_fn_mod.loc[~df_fn_mod.training, ["Set Order", "Weight", "Reps", "Seconds", "Notes"]] = [
        "Rest Timer", np.nan, np.nan, DEFAULT_REST_TIME, np.nan
    ]

    df_fn_mod[STRONG_COLUMNS].to_csv(RESULT_PATH, index=False)