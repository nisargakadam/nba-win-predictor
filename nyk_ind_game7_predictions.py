# -*- coding: utf-8 -*-
"""nyk_ind_game7_predictions.ipynb

"""

pip install nba_api

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from nba_api.stats.endpoints import leaguegamefinder
#knicks game data
knicks = leaguegamefinder.LeagueGameFinder(team_id_nullable = '1610612752')

knicks_all = knicks.get_data_frames()[0]
knicks_all['GAME_DATE'] = pd.to_datetime(knicks_all['GAME_DATE'])
knicks2025 = knicks_all[knicks_all['GAME_DATE'] >= '2024-10-21'].copy()
knicks2025['WIN'] = knicks2025['WL'].apply(lambda x: 1 if x=='W' else 0)
knicks2025_sorted = knicks2025.sort_values('GAME_DATE')
#knicks2025_sorted = knicks2025_sorted[:-1]

#pacers game data
pacers = leaguegamefinder.LeagueGameFinder(team_id_nullable = "1610612754")

pacers_all= pacers.get_data_frames()[0]
pacers_all['GAME_DATE'] = pd.to_datetime(pacers_all['GAME_DATE'])
pacers2025 = pacers_all[pacers_all['GAME_DATE'] >= '2024-10-21'].copy()
pacers2025['WIN'] = pacers2025['WL'].apply(lambda x: 1 if x=='W' else 0)
pacers2025_sorted = pacers2025.sort_values('GAME_DATE')
#pacers2025_sorted = pacers2025_sorted[:-1]

knicks2025_sorted

metrics = ['FG_PCT', 'FG3_PCT', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PLUS_MINUS']

def playoffAverages(team, stats, n=18):
  return team.tail(n)[metrics].mean().round(3).to_dict()

knicks_avgs = playoffAverages(knicks2025_sorted, metrics, n=18)
pacers_avgs = playoffAverages(pacers2025_sorted, metrics, n=18)

knicks_avgs

X_knicks = knicks2025_sorted[metrics]
y_knicks = knicks2025_sorted['WIN']
knicks_scaler = StandardScaler()
X_knicksScaled = knicks_scaler.fit_transform(X_knicks)
knicksRF = RandomForestClassifier(random_state = 42)
knicksRF.fit(X_knicksScaled, y_knicks)



X_pacers = pacers2025_sorted[metrics]
y_pacers = pacers2025_sorted['WIN']
pacers_scaler = StandardScaler()
X_pacersScaled = pacers_scaler.fit_transform(X_pacers)
pacersRF = RandomForestClassifier(random_state = 42)
pacersRF.fit(X_pacersScaled, y_pacers)

#scale inputs

def input_lst(avgs, metrics):
  return np.array([[avgs[x] for x in metrics]])

knicksInput = input_lst(knicks_avgs, metrics)

pacersInput = input_lst(pacers_avgs, metrics)

def win_prob(teamModel, dataScaled):
  return teamModel.predict_proba(dataScaled)[0][1]

knicksProb = win_prob(knicksRF, knicksInput)

pacersProb = win_prob(pacersRF, pacersInput)

totalPercent = knicksProb + pacersProb

knicks_chance = knicksProb/totalPercent

pacers_chance = pacersProb/totalPercent

print("For the 2025 Eastern Conference Finals between the New York Knicks and the Indiana Pacers, here are each team's chance of winning Game 7:  ")
print(f"New York Knicks Chance of Winning: {round(knicks_chance *100, 3)}%")
print(f"Indiana Pacers Chance of Winning: {round(pacers_chance *100, 3)}%")

'''
For the 2025 Eastern Conference Finals between the New York Knicks and the Indiana Pacers, here are each team's chance of winning Game 7:  
New York Knicks Chance of Winning: 49.462%
Indiana Pacers Chance of Winning: 50.538%

'''
