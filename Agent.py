import numpy as np


class Agent():
    def __init__(self, eps=0.1, gamma=0.99):
        self.my_hand = [i for i in range(3, 22)]
        self.dealer_hand = [i for i in range(1, 11)]
        self.ace_as_10 = [False, True]
        self.action_set = [0, 1]
        
        self.state_set = []
        self.memory = []
        self.values = {} #mean values of states
        self.values_ = {} #momentary values of states
        self.policy = {}
        
        self.gamma = gamma
        self.eps = eps

        self.initialize()


    def initialize(self):
        for sum in self.my_hand:
            for num in self.dealer_hand:
                for ace in self.ace_as_10:
                    state = (sum, num, ace)
                    self.state_set.append(state)
                    for action in self.action_set: 
                        self.values[(state, action)] = 0
                        self.values_[(state, action)] = []
        
        num_actions = len(self.action_set)
        for state in self.state_set:
            self.policy[state] = [1/num_actions for _ in range(num_actions)]


    def act(self, state):
        action = np.random.choice(self.action_set, p=self.policy[state])
        return action

    
    def store(self, record):
        self.memory.append(record)


    def update(self):
        #updating values_
        for index, (state, action, _) in enumerate(self.memory):
            value_ = 0
            discount = 1
            for _, (_, _, reward) in enumerate(self.memory[index:]):
                value_ += reward * discount
                discount *= self.gamma
                self.values_[(state, action)].append(value_)
        
        for state, action, _ in self.memory:
            #updating values
            self.values[(state, action)] = np.mean(self.values_[(state, action)])
            
            #updating policies
            max_action = np.argmax([self.values[(state, action_)] for action_ in self.action_set])
            num_actions = len(self.action_set)
            chances = []
            for action_ in self.action_set:
                if action_ == max_action:
                    chance = 1 - self.eps + (self.eps / num_actions)
                else:
                    chance = self.eps / num_actions
                chances.append(chance)
            self.policy[state] = chances
            
        self.memory = []