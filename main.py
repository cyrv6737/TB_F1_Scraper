# Documentation on how to use fastf1
# https://theoehrly.github.io/Fast-F1/
# https://github.com/theOehrly/Fast-F1

import fastf1
import pandas as pd
import os
import glob

# Enable caching so its not slow as hell
fastf1.Cache.enable_cache("cache")

# Takes Session.results
def format_race_table(race, race_num) :
    race.drop(labels = ["FullName", "Abbreviation", "BroadcastName", "Q1", "Q2", "Q3", "TeamColor"], axis = 1, inplace = True)
    race.insert(loc = 0, column = 'raceID', value = race_num)

def race_results(year, names) :
    i = 0
    for race_name in names:
        temp_race = fastf1.get_session(year, race_name, 'R'); temp_race.load()
        format_race_table(temp_race.results, (i + 1))
        csv_name = 'csv/results/R' + str(i + 1) + '_Race_Results.csv'
        temp_race.results.to_csv(csv_name, sep=',', encoding='utf-8', index=False) # Ensure utf-8 encoding for compat
        i = i + 1

    results = os.path.join("csv/results/", "R*.csv")
    results = glob.glob(results)
    df = pd.concat(map(pd.read_csv, results), ignore_index = True)
    df.to_csv('csv/tables/results.csv', sep=',', encoding='utf-8', index=False)


def format_lap_tables(laps, race_num) :
    laps.drop(labels = ["LapNumber", "Sector1SessionTime", "Sector2SessionTime", "Sector3SessionTime", "SpeedI1", "SpeedI2", "SpeedFL", "SpeedST", "IsPersonalBest", "TyreLife", "FreshTyre", "Stint", "LapStartTime", "Team", "Driver", "TrackStatus", "IsAccurate", "LapStartDate" ], axis = 1, inplace = True)
    laps.insert(loc = 0, column = 'raceID', value = race_num)

def lap_results(year, names) :
    i = 0
    for race_name in names:
        temp_race = fastf1.get_session(year, race_name, 'R'); temp_race.load()
        temp_laps = temp_race.laps
        format_lap_tables(temp_laps, (i + 1))
        csv_name = 'csv/laps/R' + str(i + 1) + '_Lap_Results.csv'
        temp_laps.to_csv(csv_name, sep=',', encoding='utf-8', index=False) # Ensure utf-8 encoding for compat
        i = i + 1

    results = os.path.join("csv/laps/", "R*.csv")
    results = glob.glob(results)
    df = pd.concat(map(pd.read_csv, results), ignore_index = True)
    df.to_csv('csv/tables/laps.csv', sep=',', encoding='utf-8', index=False)

# All race names for this season
race_names = (
    "FORMULA 1 GULF AIR BAHRAIN GRAND PRIX 2022",
    "FORMULA 1 STC SAUDI ARABIAN GRAND PRIX 2022",
    "FORMULA 1 HEINEKEN AUSTRALIAN GRAND PRIX 2022",
    "FORMULA 1 ROLEX GRAN PREMIO DEL MADE IN ITALY E DELL'EMILIA-ROMAGNA 2022",
    "FORMULA 1 CRYPTO.COM MIAMI GRAND PRIX 2022",
    "FORMULA 1 PIRELLI GRAN PREMIO DE ESPAÑA 2022",
    "FORMULA 1 GRAND PRIX DE MONACO 2022",
    "FORMULA 1 AZERBAIJAN GRAND PRIX 2022",
    "FORMULA 1 AWS GRAND PRIX DU CANADA 2022",
    "FORMULA 1 LENOVO BRITISH GRAND PRIX 2022",
    "FORMULA 1 ROLEX GROSSER PREIS VON ÖSTERREICH 2022",
    "FORMULA 1 LENOVO GRAND PRIX DE FRANCE 2022",
    "FORMULA 1 ARAMCO MAGYAR NAGYDÍJ 2022",
    "FORMULA 1 ROLEX BELGIAN GRAND PRIX 2022",
    "FORMULA 1 HEINEKEN DUTCH GRAND PRIX 2022",
    "FORMULA 1 PIRELLI GRAN PREMIO D’ITALIA 2022",
    "FORMULA 1 SINGAPORE AIRLINES SINGAPORE GRAND PRIX 2022",
    "FORMULA 1 HONDA JAPANESE GRAND PRIX 2022"
)

drivers = (
    "VER",
    "RUS",
    "LEC",
    "HAM",
    "PER",
    "ALO",
    "NOR",
    "SAI",
    "OCO",
    "STR",
    "GAS",
    "ALB",
    "MSC",
    "VET",
    "MAG",
    "ZHO",
    "RIC",
    "LAT",
    "BOT",
    "TSU"
)

# Export CSV for all races results
race_results(2022, race_names)
lap_results(2022, race_names)