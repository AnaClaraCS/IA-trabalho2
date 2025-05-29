import gym
import numpy as np
from environment import Environment
import random

class MountainCarEnvironment(Environment):
    def __init__(self, env, bins=(30, 30)):
        super().__init__(env)
        self.bins = bins

        self.low = np.array(self.env.observation_space.low, dtype=np.float32)
        self.high = np.array(self.env.observation_space.high, dtype=np.float32)

        self.bin_width = (self.high - self.low) / np.array(self.bins, dtype=np.float32)
        self.num_states = bins[0] * bins[1]
        self.num_actions = self.env.action_space.n

    def get_num_states(self):
        return self.num_states

    def get_num_actions(self):
        return self.num_actions

    def get_random_action(self):
        return self.env.action_space.sample()

    # Recebe um estado contínuo e retorna uma representação discreta
    def get_state_id(self, state):
        pos, vel = state

        # 1- Divida a posição e velocidade em um número fixo de intervalos (bins)
        pos_bin = int((pos - self.low[0]) / self.bin_width[0])
        vel_bin = int((vel - self.low[1]) / self.bin_width[1])

        pos_bin = min(self.bins[0] - 1, max(0, pos_bin))
        vel_bin = min(self.bins[1] - 1, max(0, vel_bin))

        # 2- Mapeie os estados contínuos para representações discretas
        return pos_bin * self.bins[1] + vel_bin
