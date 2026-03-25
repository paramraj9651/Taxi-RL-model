# Taxi RL Model

Simple reinforcement learning demo for a taxi pickup-and-drop problem with a Flask UI.

## Overview

This project trains and serves a Q-learning based taxi agent on a small grid world. The web app runs a trained agent and shows the sequence of actions taken by the model.

## Project Structure

```text
project/
  app.py                 Flask app
  q_table.pkl            Trained Q-table used by the app
  rl/
    agent.py             Q-learning agent
    env.py               Taxi environment
    train.py             Training script
  static/
    script.js            Frontend logic
    style.css            Styles
  templates/
    index.html           UI template
```

## Features

- Q-learning based taxi agent
- Custom taxi grid environment
- Flask backend with JSON response
- Simple frontend to run the trained agent

## Requirements

- Python 3.10+
- `flask`
- `numpy`

Install dependencies:

```bash
pip install flask numpy
```

## Run The App

From the `project` directory:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Train The Agent

The training script is inside `project/rl`.

```bash
cd project/rl
python train.py
```

After training, the Q-table is saved and the Flask app loads it from:

```text
project/q_table.pkl
```

## Notes

- The current environment uses a 5x5 grid.
- Actions are mapped as:
  - `0`: up
  - `1`: down
  - `2`: left
  - `3`: right
  - `4`: pickup
  - `5`: drop
