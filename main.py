import gym
import matplotlib.pyplot as plt
from Agent import Agent
from tqdm import tqdm

if __name__ == "__main__":
    env = gym.make("Blackjack-v1")
    agent = Agent(eps=0.001)
    num_games = 200000
    results = {-1:0, 0:0, 1:0}
    win_rates = []
    
    for g in tqdm(range(num_games)):
        if g > 0 and g % 1000 == 0:
            win_rates.append(results[1] / g)
            
        state = env.reset()[0]
        done = False
        while not done:
            action = agent.act(state)
            state_, reward, done, info, _ = env.step(action)
            agent.store((state, action, reward))
            state = state_
        agent.update()
        results[reward] += 1
    
    plt.plot(win_rates)
    plt.show()
        