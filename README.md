# iBlackJack

Instructing an agent in the strategies of playing Blackjack using Monte Carlo control.

### Introduction

This serves as a straightforward example demonstrating how Monte Carlo methods can be practically applied in gaming scenarios. Essentially, the approach involves repeatedly playing BlackJack to obtain accurate estimates for the expected value of each possible state. Actions are then selected based on these calculated values.

### Strategy Overview

The final code implementation utilizes the epsilon-soft action selection strategy. Here's a breakdown:

$$
\text{Exploratory action probability} \gets \frac{\epsilon}{|\boldsymbol{S}|}
$$

$$
\text{Greedy action probability} \gets 1 - \epsilon + \frac{\epsilon}{|\boldsymbol{S}|}
$$

$$
\text{The greed increases over time.}
$$

However, in earlier commits, you'll find simpler action selection strategies.

### Let's Get Started!

Feel free to explore, experiment, and have fun! 🎮😄


