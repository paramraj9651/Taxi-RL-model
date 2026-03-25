import numpy as np
import random
import pickle
from pathlib import Path

class Agent:
    def __init__(self):
        self.q_table = {}
        self.lr = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0
        self.model_path = Path(__file__).resolve().parent.parent / "q_table.pkl"

    def get_q(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(6)
        return self.q_table[state]

    def choice_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(6)

        if random.random() < self.epsilon:
            return random.randint(0, 5)
        return np.argmax(self.q_table[state])

    def choose_action(self, state):
        return self.choice_action(state)

    def update_q_table(self, state, action, reward, next_state):
        q_value = self.get_q(state)
        next_q = self.get_q(next_state)
        max_next_q = np.max(next_q)

        q_value[action] += self.lr * (reward + self.gamma * max_next_q - q_value[action])

    def save(self):
        with self.model_path.open("wb") as f:
            pickle.dump(self.q_table, f)

    def load(self):
        with self.model_path.open("rb") as f:
            self.q_table = pickle.load(f)


class Qagent(Agent):
    pass
