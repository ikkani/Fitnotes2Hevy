# Fitnotes2Hevy
Python snippet to convert from FitNotes export to Hevy compatible (Strong app format).

The logic itself is pretty simple, the most useful thing about this repo is the mapping between Fitnotes to Strong workout names (available in files/map_fitnotes2strong.json). You can also tweak the json in case you want to add some custom exercise you have in fitnotes.

I also added all the default exercises of both apps in **files/fitnotes_exercises.txt** and **files/strong_exercises.txt**.

## Usage
1. Export your FitNotes data in Settings/Spreadsheet Export.

2. Copy the FitNotes csv into an accesible location.

3. Clone the repo.
```
git clone https://github.com/ikkani/Fitnotes2Hevy.git
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
