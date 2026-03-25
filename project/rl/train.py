from env import taxienv
from agent import Agent
env = taxienv()
agent = Agent()

for episode in range(10):
    state = env.reset()
    done = False
    
    while not done:
        action = agent.choice_action(state)
        next_state, reward, done = env.step(action)
        agent.update_q_table(state, action, reward, next_state)
        state = next_state
        
    agent.epsilon *= 0.995
 
agent.save()
print("Training completed")