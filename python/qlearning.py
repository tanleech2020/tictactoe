import random

class QLearningAgent:
    def __init__(self, gamma=0.8):
        self.q_table = {}
        self.gamma = gamma

    def get_state_key(self, state):
        return str(state.reshape(9))

    #choose one of the valid actions
    def choose_action(self, state, valid_actions):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(valid_actions)
        else:
            state_key = self.get_state_key(state)
            if state_key not in self.q_table:
                return random.choice(valid_actions)
            return max(valid_actions, key=lambda x: self.q_table[state_key].get(x, 0))

    def update_q_table(self, state, action, reward, next_state, done):
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)

        if state_key not in self.q_table:
            self.q_table[state_key] = {}
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = {}

        max_future_q = max(self.q_table[next_state_key].values(), default=0)
        
        if done:
            self.q_table[state_key][action] = reward
        else:
            self.q_table[state_key][action] = reward + self.gamma * max_future_q