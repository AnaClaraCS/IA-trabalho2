import numpy as np
from feature_extractor import FeatureExtractor

class Actions:
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3

class FrozenLakeFeatureExtractor(FeatureExtractor):
    __actions_one_hot_encoding = {
        Actions.LEFT:  np.array([1, 0, 0, 0]),
        Actions.DOWN:  np.array([0, 1, 0, 0]),
        Actions.RIGHT: np.array([0, 0, 1, 0]),
        Actions.UP:    np.array([0, 0, 0, 1])
    }

    def __init__(self, env):
        self.env = env
        self.n_rows = int(np.sqrt(env.observation_space.n))
        self.n_cols = self.n_rows
        self.features_list = []
        self.features_list.append(self.f0)
        self.features_list.append(self.f1)
        self.features_list.append(self.f2) 

    def get_num_features(self):
        return len(self.features_list) + self.get_num_actions()

    def get_num_actions(self):
        return len(self.get_actions())

    def get_action_one_hot_encoded(self, action):
        return self.__actions_one_hot_encoding[action]

    def is_terminal_state(self, state):
        return state == (self.n_rows * self.n_cols - 1)

    def get_actions(self):
        return [Actions.LEFT, Actions.DOWN, Actions.RIGHT, Actions.UP]

    def get_features(self, state, action):
        feature_vector = np.zeros(len(self.features_list))
        for i, f in enumerate(self.features_list):
            feature_vector[i] = f(state, action)

        action_vector = self.get_action_one_hot_encoded(action)
        return np.concatenate([feature_vector, action_vector])

    def f0(self, state, action):
        return 1.0

    def f1(self, state, action):
        row, col = divmod(state, self.n_cols)
        return row / (self.n_rows - 1)

    def f2(self, state, action):
        row, col = divmod(state, self.n_cols)
        return col / (self.n_cols - 1)
