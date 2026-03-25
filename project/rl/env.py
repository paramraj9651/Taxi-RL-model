import random

class taxienv:
    def __init__(self):
        self.grid_size = 5
        self.max_steps = 200
        self.reset()

    def reset(self):
        self.taxi =  [random.randint(0, 4), random.randint(0, 4)]
        self.passenger = [random.randint(0, 4), random.randint(0,4)]
        self.destination = [random.randint(0, 4), random.randint(0,4)]
        self.has_passenger = False
        self.step_count = 0
        return self.get_state()
    
    def get_state(self):
        return (self.taxi[0], self.passenger[0], self.destination[0], self.has_passenger)
    
    def step(self, action):
        reward = -1
        self.step_count += 1
        
        # action: 0=up, 1=down, 2=left, 3=right, 4=pickup, 5=drop
        if action == 0 and self.taxi[0] > 0:
            self.taxi[0] -= 1
        elif action == 1 and self.taxi[0] < 4:
            self.taxi[0] += 1
        elif action == 2 and self.taxi[1] > 0:
            self.taxi[1] -= 1
        elif action == 3 and self.taxi[1] < 4:
            self.taxi[1] += 1
        elif action == 4:  # pickup
            if self.taxi == self.passenger:
                self.has_passenger = True
            else:
                reward = -10
        elif action == 5:  # drop
            if self.taxi == self.destination and self.has_passenger:
                reward = 20
                return self.get_state(), reward, True
            else:
                reward = -10
        
        done = self.step_count >= self.max_steps
        return self.get_state(), reward, done


class TaxiEnv(taxienv):
    pass
