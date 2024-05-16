import numpy as np


class Agent():
    def __init__(self, gamma=0.99):
        self.my_hand = [i for i in range(3, 22)]
        self.dealer_hand = [i for i in range(1, 11)]
        self.ace_as_10 = [False, True]
        self.action_set = [0, 1]
        self.value = {}
        self.state = []
        self.actual_values = {}
        # self.is_state_visited = {}
        self.memory = []
        self.gamma = gamma

        self.initialize()

    def initialize(self):
        for sum in self.my_hand:
            for num in self.dealer_hand:
                for ace in self.ace_as_10:
                    self.value[(sum, num, ace)] = 0
                    self.actual_values[(sum, num, ace)] = []
                    # self.is_state_visited[(sum, num, ace)] = 0
                    self.state.append((sum, num, ace))

    def act(self, state):
        (sum, _, _) = state
        action = 0 if sum >= 21 else 1
        return action
    
    def store(self, record):
        self.memory.append(record)

    def update(self):
        for index, (state, _) in enumerate(self.memory):
            value_ = 0
            # if self.is_state_visited[state] == 0:
            # self.is_state_visited[state] += 1
            discount = 1
            for _, (_, reward) in enumerate(self.memory[index:]):
                value_ += reward * discount
                self.actual_values[state].append(value_)
        
        for state, _ in self.memory:
            self.value[state] = np.mean(self.actual_values[state])
            
        # for state in self.state:
        #     self.is_state_visited[state] = 0
            
        self.memory = []
