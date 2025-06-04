# 🏀 NBA Game Win Predictor: ECF Edition  
### *"Predicting Playoff Outcomes, One Game at a Time"*

Ever watched tip-off and wondered: *"Who's actually going to win this?"*  
This project uses real-time NBA data and machine learning to predict the outcome of **each Eastern Conference Finals game** between the **New York Knicks** and the **Indiana Pacers**.

> 📈 *Final result: 66.7% accuracy across 6 Eastern Conference Finals games — not bad for first time NBA predictions!*
---

## 📦 What This Repo Contains

This repo includes prediction files for **Games 1 through 7** of the 2025 Eastern Conference Finals between the New York Knicks and Indiana Pacers.

Each `.py` file:
- Pulls updated game stats via [`nba_api`](https://github.com/swar/nba_api)
- Computes rolling team averages over the last `n` games (FG%, REB, AST, STL, etc.)
- Trains a `RandomForestClassifier` model per team based on win history
- Outputs **normalized win probabilities** for each game
- Includes visualizations (in select files) to track momentum shifts and key stat trends

---

## 🧠 Why I Built This

As a Knicks fan and a grad student studying computer science, I wanted to combine my:
- Curiosity around **stat-driven performance under pressure**
- Passion for **sports analytics**
- Personal need to emotionally prepare using predictive modeling 

---

## 🔮 How It Works

Each game prediction script:
1. Pulls season stats for each team
2. Filters for games after the season start (e.g., `2024-10-21`)
3. Calculates recent game averages over the last 18 games
4. Trains a `RandomForestClassifier` on historical win data
5. Predicts each team's win probability and normalizes results
6. A few plots relevant statistical trends using `matplotlib` or `seaborn`

---
## 📊 Game Predictions: 2025 Eastern Conference Finals


| Game | Knicks Win % | Pacers Win % | Predicted Winner | Actual Outcome | Prediction Accuracy |
|------|--------------|---------------|------------------|----------------|---------------------|
| 1    | 49.73%       | 50.27%        | Pacers           | Pacers         | ✅                  |
| 2    | 48.65%       | 51.35%        | Pacers           | Pacers         | ✅                  |
| 3    | 47.85%       | 52.15%        | Pacers           | Knicks         | ❌                  |
| 4    | 48.13%       | 51.87%        | Pacers           | Pacers         | ✅                  |
| 5    | 48.39%       | 51.61%        | Pacers           | Knicks         | ❌                  |
| 6    | 49.20%       | 50.80%        | Pacers           | Pacers         | ✅                  |
| 7    | 49.46%       | 50.54%        | Pacers           | *Not Played*   | —                   |



**Overall Model Accuracy:** 4 correct predictions out of 6 games  
🎯 **Prediction Accuracy:** **66.7%**

The model correctly predicted Games 1, 2, 4, and 6, proving surprisingly reliable under high-pressure playoff conditions. While Game 7 was never played, its prediction was still generated for completeness and fun.


---

## 📊 Visuals (in select files)

- FG% and 3PT% over recent games
- Turnovers, Assists, and Rebounds
- Plus/Minus metrics for momentum analysis

> **Note:** Not every script includes plots — this is a future improvement area.

---

## ⚙️ Tech Stack

- Python  
- [`nba_api`](https://github.com/swar/nba_api) for pulling game stats  
- `pandas`, `numpy` for data wrangling  
- `scikit-learn` for modeling  
- `matplotlib`, `seaborn` for visualization  

---

## 📌 Future Goals

- Add a **Tableau** dashboard to interactively explore predictions    
- Include **player-level data** and injury reports  
- Simulate full **finals brackets** using Monte Carlo simulations  

