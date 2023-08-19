import glob, json
import pandas as pd

# Add repo
git_dir = os.path.abspath('../')
data_path = os.path.join("", 'data', 'hansard-parsed')

def hansard_senate_paths(year : int):
    senate_paths = glob.glob("{}/senate/{}/*.json".format(data_path, year))
    return senate_paths

def hansard_hofreps_paths(year : int):
    hofreps_paths = glob.glob("{}/hofreps/{}/*.json".format(data_path, year))
    return hofreps_paths

def hansard_from_file(file_path):
    return json.load(open(file_path))

def senate_hansard(years):
    hansard = []
    for y in years:
        for path in hansard_senate_paths(y):
            hansard += hansard_from_file(path)
    return pd.DataFrame(hansard)

def hofreps_hansard(years):
    hansard = []
    for y in years:
        for path in hansard_hofreps_paths(y):
            hansard += hansard_from_file(path)
    return pd.DataFrame(hansard)

years = list(range(2011,2021))
hofreps = hofreps_hansard(years)
senate = senate_hansard(years)