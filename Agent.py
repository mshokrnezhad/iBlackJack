import numpy as np

class Agent():
    def __inii__(self, gamma=0.99):
        self.my_state = [i for i in range(3, 22)]
        self.dealer_state = [i for i in range(1, 11)]
        self.ace_state = [False, True]
        
        self.action_set = [0, 1]
        self.value = {}
        
        self.state = []
        self.actual_values = {}
        self.is_state_visited = {}
        self.memory = []
        self.gamma = gamma
        
        self.initialize()
        
    def initialize(self):
        for sum in self.my_state:
            for num in self.dealer_state:
                for ace in self.ace_state:
                    self.value[(sum, num, ace)] = 0
                    self.actual_values[(sum, num, ace)] = []
                    self.is_state_visited[(sum, num, ace)] = 0
                    self.state.append((sum, num, ace))
    
    