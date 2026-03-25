from flask import Flask, jsonify, render_template
from rl.env import TaxiEnv
from rl.agent import Qagent

app = Flask(__name__)

env = TaxiEnv()
agent = Qagent()

# Load trained Q-table
try:
    agent.load()
    agent.epsilon = 0.0
    print("Q-table loaded")
except Exception:
    print("No trained model found")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run_agent():
    state = env.reset()
    done = False
    steps = []

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        steps.append({
            "state": list(state),
            "action": int(action),
            "reward": int(reward),
        })

        state = next_state

    return jsonify(steps)


if __name__ == "__main__":
    app.run(debug=True)
