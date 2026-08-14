# Fitnotes2Hevy

[![GitHub stars](https://img.shields.io/github/stars/szejkerek/Fitnotes2Hevy?style=social)](https://github.com/szejkerek/Fitnotes2Hevy/stargazers)

Convert your **FitNotes** workout export CSV into a **Hevy** (Strong app format) CSV.

Migrating from FitNotes to Hevy? This Python script maps exercise names and rebuilds your workout log so you can import it straight into Hevy.

The logic itself is pretty simple, the most useful thing about this repo is the mapping between Fitnotes to Strong workout names (available in files/map_fitnotes2strong.json). You can also tweak the json in case you want to add some custom exercise you have in fitnotes.


## Usage
1. Export your FitNotes data in Settings/Spreadsheet Export.

2. Copy the FitNotes csv into an accesible location.

3. Clone the repo.
```
git clone https://github.com/szejkerek/Fitnotes2Hevy.git
cd Fitnotes2Hevy
```

4. Install dependences if you do not have Pandas and Numpy.
```
pip install -r requirements.txt
```

5. Change variables in config.py with your own configuration (important to set the path of the FitNotes export).

6. Execute the code.
```
python main.py
```

## Fixing/improving exercise mapping

If an exercise doesn't import right, it's a mapping gap, not a bug.

1. Run the script once, unmapped exercises get printed.
2. Open **files/map_fitnotes2strong.json**.
3. Find your FitNotes exercise name as it appears in your CSV (check **files/fitnotes_exercises.txt** for the full default list).
4. Add or fix entries.
5. Pick the Hevy-side name from **files/strong_exercises.txt** so it matches exactly (case-sensitive).
6. Re-run `python main.py`.
