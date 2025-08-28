from tictactoe import TicTacToe
from qlearning import QLearningAgent

env = TicTacToe()
agent = QLearningAgent()

num_episodes = 10000

for episode in range(num_episodes):
    state = env.reset()
    done = False

    while not done:
        valid_actions = env.get_valid_actions()
        action = agent.choose_action(state, valid_actions)
        next_state, reward, done = env.step(action, 1)
        agent.update_q_table(state, action, reward, next_state, done)
        state = next_state

    agent.decay_exploration()