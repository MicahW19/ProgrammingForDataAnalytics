# Week 2 Code Samples

## What's happening!

[01-demos.py](https://github.com/blairw/ProgrammingForDataAnalytics/blob/main/CodeSamples/w02/01-demos.py)

- Get the CSV file, `owid-covid-data.csv`, from https://github.com/owid/covid-19-data/tree/master/public/data
- Key concepts:
    - Installing and importing `numpy`, `pandas`, `pandasql`
    - Very simple logging example using `print(...)` and `datetime`
    - Demo 1: CSV to Pandas DataFrame
    - Demo 2: Get the list of headings (there's a lot!)
    - Demo 3: List of locations
    - Demo 4: Most recent date available for each location
    - Demo 5: Maximum vaccinations for each location
    - Demo 6: Generate pairs of locations based on Demo 5

[02-allocation.py](https://github.com/blairw/ProgrammingForDataAnalytics/blob/main/CodeSamples/w02/02-allocation.py)

- Make sure you have run `01-demos.py` first!
- Key concepts:
    - Random number generator
    - Random seed (see also: https://en.wikipedia.org/wiki/Random_seed)
    - Allocating a line from the CSV file

## Pro Tip

Don't forget the usual venv setup!

```bash
python3 -m venv .venv
source .venv/bin/activate
```

And after you are done:

```bash
deactivate
```
