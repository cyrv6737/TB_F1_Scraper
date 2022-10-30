# Documentation on how to use fastf1
# https://theoehrly.github.io/Fast-F1/
# https://github.com/theOehrly/Fast-F1

import fastf1
import pandas as pd
import os
import glob
from pathlib import Path

# Enable caching so its not slow as hell
fastf1.Cache.enable_cache("cache")

# create paths
Path("csv/results").mkdir(parents = True, exist_ok = True)
Path("csv/tables").mkdir(parents = True, exist_ok = True)

def get_race_results(events):
    irace = 0
    for race in events:
        filename = "RaceData_" + str(race) + ".csv"
        session = fastf1.get_session(2022, race, 'R')
        session.load()

        length = len(session.results.FullName)
        results_artifact = session.results.iloc[0:length].loc[:, ['DriverNumber', 'FirstName', 'LastName', 'TeamName', 'Position', 'Time', 'Points', 'Status']]
        # print(session.results.iloc[0:20].loc[:, ['FullName', 'TeamName', 'Position', 'Time', 'Points', 'Status']])
        results_artifact.insert(loc = 1, column = 'raceID', value = irace)
        df = pd.DataFrame(results_artifact)
        df.to_csv("csv/results/" + filename, sep=',', encoding='utf-8', index=False)
        irace = irace + 1

    race_table = os.path.join("csv/results/", "RaceData_*.csv")
    race_table = glob.glob(race_table)
    df = pd.concat(map(pd.read_csv, race_table))
    df['Time'] = df['Time'].str.replace("0 days ", "")
    df['TeamName'] = df['TeamName'].str.replace("Red Bull Racing", "0")
    df['TeamName'] = df['TeamName'].str.replace("Ferrari", "1")
    df['TeamName'] = df['TeamName'].str.replace("Mercedes", "2")
    df['TeamName'] = df['TeamName'].str.replace("Alpine", "3")
    df['TeamName'] = df['TeamName'].str.replace("McLaren", "4")
    df['TeamName'] = df['TeamName'].str.replace("Alfa Romeo", "6")
    df['TeamName'] = df['TeamName'].str.replace("Aston Martin", "6")
    df['TeamName'] = df['TeamName'].str.replace("Haas F1 Team", "7")
    df['TeamName'] = df['TeamName'].str.replace("AlphaTauri", "8")
    df['TeamName'] = df['TeamName'].str.replace("Williams", "9")
    df = df.rename(columns={'TeamName': 'ConstructorID'})
    df.to_csv("csv/tables/RaceResults.csv", sep=',', encoding='utf-8', index=False)

def get_qualifier_results(events):
    iqual = 0
    for qualifier in events:
        filename = "QualifierData_" + str(qualifier) + ".csv"
        session = fastf1.get_session(2022, qualifier, 'Q')
        session.load()

        length = len(session.results.FullName)
        results_artifact = session.results.iloc[0:length].loc[:, ['DriverNumber', 'FirstName', 'LastName', 'TeamName', 'Position', 'Q1', 'Q2', 'Q3']]
        # print(session.results.iloc[0:20].loc[:, ['FullName', 'TeamName', 'Position', 'Time', 'Points', 'Status']])
        results_artifact.insert(loc = 1, column = 'raceID', value = iqual)
        df = pd.DataFrame(results_artifact)
        df.to_csv("csv/results/" + filename, sep=',', encoding='utf-8', index=False)
        iqual = iqual + 1

    qual_table = os.path.join("csv/results/", "QualifierData_*.csv")
    qual_table = glob.glob(qual_table)
    df = pd.concat(map(pd.read_csv, qual_table))
    df['Q1'] = df['Q1'].str.replace("0 days ", "")
    df['Q2'] = df['Q2'].str.replace("0 days ", "")
    df['Q3'] = df['Q3'].str.replace("0 days ", "")
    df['TeamName'] = df['TeamName'].str.replace("Red Bull Racing", "0")
    df['TeamName'] = df['TeamName'].str.replace("Ferrari", "1")
    df['TeamName'] = df['TeamName'].str.replace("Mercedes", "2")
    df['TeamName'] = df['TeamName'].str.replace("Alpine", "3")
    df['TeamName'] = df['TeamName'].str.replace("McLaren", "4")
    df['TeamName'] = df['TeamName'].str.replace("Alfa Romeo", "6")
    df['TeamName'] = df['TeamName'].str.replace("Aston Martin", "6")
    df['TeamName'] = df['TeamName'].str.replace("Haas F1 Team", "7")
    df['TeamName'] = df['TeamName'].str.replace("AlphaTauri", "8")
    df['TeamName'] = df['TeamName'].str.replace("Williams", "9")
    df = df.rename(columns={'TeamName': 'ConstructorID'})
    df.to_csv("csv/tables/QualifierResults.csv", sep=',', encoding='utf-8', index=False)


def get_practice_results(events):
    ifp1 = 0
    for fp1 in events:
        filename = "FP1_Data_" + str(fp1) + ".csv"
        session = fastf1.get_session(2022, fp1, 'FP1')
        session.load()

        length = len(session.results.FullName)
        results_artifact = session.results.iloc[0:length].loc[:, ['DriverNumber', 'FirstName', 'LastName', 'TeamName', 'Time']]
        # print(session.results.iloc[0:20].loc[:, ['FullName', 'TeamName', 'Position', 'Time', 'Points', 'Status']])
        results_artifact.insert(loc = 1, column = 'raceID', value = ifp1)
        results_artifact.insert(loc = 1, column = 'Practice Session', value = '1')
        df = pd.DataFrame(results_artifact)
        df.to_csv("csv/results/" + filename, sep=',', encoding='utf-8', index=False)
        ifp1 = ifp1 + 1

    ifp2 = 0
    for fp2 in events:
        filename = "FP2_Data_" + str(fp2) + ".csv"
        session = fastf1.get_session(2022, fp2, 'FP2')
        session.load()

        length = len(session.results.FullName)
        results_artifact = session.results.iloc[0:length].loc[:, ['DriverNumber', 'FirstName', 'LastName', 'TeamName', 'Time']]
        # print(session.results.iloc[0:20].loc[:, ['FullName', 'TeamName', 'Position', 'Time', 'Points', 'Status']])
        results_artifact.insert(loc = 1, column = 'raceID', value = ifp2)
        results_artifact.insert(loc = 1, column = 'Practice Session', value = '2')
        df = pd.DataFrame(results_artifact)
        df.to_csv("csv/results/" + filename, sep=',', encoding='utf-8', index=False)
        ifp2 = ifp2 + 1

    ifp3 = 0
    for fp3 in events:
        ifp3 = ifp3 + 1
        # skip events without practice 3 to prevent crashing
        if fp3 == "FORMULA 1 ROLEX GRAN PREMIO DEL MADE IN ITALY E DELL'EMILIA-ROMAGNA 2022":
            continue
        elif fp3 == "FORMULA 1 ROLEX GROSSER PREIS VON ÖSTERREICH 2022":
            continue

        filename = "FP3_Data_" + str(fp3) + ".csv"
        session = fastf1.get_session(2022, fp3, 'FP3')
        session.load()

        length = len(session.results.FullName)
        results_artifact = session.results.iloc[0:length].loc[:, ['DriverNumber', 'FirstName', 'LastName', 'TeamName', 'Time']]
        # print(session.results.iloc[0:20].loc[:, ['FullName', 'TeamName', 'Position', 'Time', 'Points', 'Status']])
        results_artifact.insert(loc = 1, column = 'raceID', value = (ifp3 - 1))
        results_artifact.insert(loc = 1, column = 'Practice Session', value = '3')
        df = pd.DataFrame(results_artifact)
        df.to_csv("csv/results/" + filename, sep=',', encoding='utf-8', index=False)

    practice_table = os.path.join("csv/results/", "FP*.csv")
    practice_table = glob.glob(practice_table)
    df = pd.concat(map(pd.read_csv, practice_table))
    df['TeamName'] = df['TeamName'].str.replace("Red Bull Racing", "0")
    df['TeamName'] = df['TeamName'].str.replace("Ferrari", "1")
    df['TeamName'] = df['TeamName'].str.replace("Mercedes", "2")
    df['TeamName'] = df['TeamName'].str.replace("Alpine", "3")
    df['TeamName'] = df['TeamName'].str.replace("McLaren", "4")
    df['TeamName'] = df['TeamName'].str.replace("Alfa Romeo", "6")
    df['TeamName'] = df['TeamName'].str.replace("Aston Martin", "6")
    df['TeamName'] = df['TeamName'].str.replace("Haas F1 Team", "7")
    df['TeamName'] = df['TeamName'].str.replace("AlphaTauri", "8")
    df['TeamName'] = df['TeamName'].str.replace("Williams", "9")
    df = df.rename(columns={'TeamName': 'ConstructorID'})
    df.to_csv("csv/tables/FP_Results.csv", sep=',', encoding='utf-8', index=False)


def get_drivers():
    practice = pd.read_csv("csv/tables/FP_Results.csv", usecols = ['DriverNumber', 'FirstName', 'LastName', 'ConstructorID'])
    qualifier = pd.read_csv("csv/tables/QualifierResults.csv", usecols = ['DriverNumber', 'FirstName', 'LastName', 'ConstructorID'])
    race = pd.read_csv("csv/tables/RaceResults.csv", usecols = ['DriverNumber', 'FirstName', 'LastName', 'ConstructorID'])
    csv_list = [practice, qualifier, race]
    drivers = pd.concat(csv_list)
    drivers.drop_duplicates(subset = None, inplace = True)
    drivers.to_csv("csv/tables/Drivers.csv", sep=',', encoding='utf-8', index=False)

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
    "FORMULA 1 HONDA JAPANESE GRAND PRIX 2022",
    "FORMULA 1 ARAMCO UNITED STATES GRAND PRIX 2022"
)

# Export CSV for all races results
#get_race_results(race_names)
#get_qualifier_results(race_names)
#get_practice_results(race_names)
get_drivers()
