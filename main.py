import gym
from Agent import Agent
from tqdm import tqdm
import collections.abc as cabc

if __name__ == "__main__":
    env = gym.make("Blackjack-v1")
    agent = Agent()
    num_games = 100000
    for g in tqdm(range(num_games)):
        raw_state = env.reset()
        state = raw_state[0] #if isinstance(raw_state, cabc.Sequence) else raw_state
        done = False
        while not done:
            action = agent.act(state)
            state_, reward, done, info, _ = env.step(action)
            agent.store((state, reward))
            state = state_
        agent.update()
        
    print(agent.value[(21, 3, True)])
    print(agent.value[(4, 1, False)]) 
        