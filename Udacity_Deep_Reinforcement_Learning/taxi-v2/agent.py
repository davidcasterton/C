import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA), dtype=np.float64)
        self.e = 0.001  # epsilon
        self.a = 1.0  # alpha
        self.g = 1.0  # gamma

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        prob = np.ones(self.nA) * self.e / self.nA
        prob[np.argmax(self.Q[state])] = 1 - self.e + (self.e / self.nA)
        action = np.random.choice(np.arange(self.nA), p=prob)

        return action

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        if not done:
            prob = np.ones(self.nA) * self.e / self.nA
            prob[np.argmax(self.Q[next_state])] = 1 - self.e + (self.e / self.nA)

            expected_reward  = np.sum(np.multiply(prob, self.Q[next_state]))
            self.Q[state][action] += self.a * (reward + self.g * expected_reward - self.Q[state][action])
