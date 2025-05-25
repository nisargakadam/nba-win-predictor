## Predicting NBA Playoff Wins with Machine Learning 🏀📊

# 🏀 NBA Game Win Predictor

Ever watched tip-off and wondered: *"Who's actually going to win this?"*  
This project answers that question using machine learning + NBA stats to predict game outcomes—one matchup at a time.

---

## 📦 What This Repo Contains

This repo holds **individual prediction files** for specific NBA games. Each `.py` file:
- Pulls the latest season stats using [`nba_api`](https://github.com/swar/nba_api)
- Calculates each team’s recent average performance (FG%, REB, AST, etc.)
- Trains a `RandomForestClassifier` for each team to model win probability
- Normalizes both predictions to output a clean head-to-head chance of winning

---

## 🧠 Why I Built This

As a longtime Knicks fan and data science grad student, I wanted a way to explore:
- **How recent team stats reflect performance under pressure**
- **Whether machine learning can give fans a smarter edge to reduce playoff heartbreak**


---


## 🔮 How It Works

Each file predicts the outcome of one game. Just run in it in your own terminal!

---

## 🔮 Game 1 Eastern Conference Finals Predicton

  🗽 New York Knicks chance of winning: 49.733%  
  🟡 Indiana Pacers chance of winning: 50.267%


---


## 📈Plus, you'll get graphs like:

- FG% and 3PT% over time
- Rebounding and assists
- Turnovers, steals, and blocks
- Plus/Minus (momentum indicator)


---


## ⚙️ Tech Stack

  - Python 
  - nba_api for game data
  - scikit-learn for model building
  - pandas / numpy for data wrangling
  - matplotlib / seaborn for visualizations


---


## 📌 Future Goals

- Add more matchups and playoff games
- Build a Tableau dashboard to let users interactively explore win predictions and stat trends
- Experiment with player-level stats (injuries, starters, etc.)
- Add Monte Carlo simulations for series predictions
