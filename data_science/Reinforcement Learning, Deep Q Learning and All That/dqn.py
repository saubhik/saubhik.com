# Credits: https://keon.io/deep-q-learning/
#
# Let's take a plunge for a day on Deep Q Learning, Reinforcement Learning, OpenAI's gym project and all that.
# We create AI agents that learn from the environment by interacting with it.
# The AI agent acts on the environment. After each action, the agent receives the feedback.
# The feedback consists of reward and the next state of the environment.
# The reward is defined by us.
# If learning a bicycle is a task, the distance from the original starting point would be the reward. The goal is to
# always maximise the reward.
#
# Google's DeepMind published a famous paper titled "Playing Atari with Deep Reinforcement Learning", in which they
# introduced the Deep Q Network (DQN) in 2013.
#
# In Q-learning algorithm, there is a function called Q function.
# Q(s, a) calculates the expected future value from state s and action a.
# In DQNs, we use a neural net to approximate the reward based on the state.
#
# We will train an agent to play CartPole, one of the simplest environments in OpenAI gym
# The goal is to balance a pole connected with a joint on top of a moving cart
# There are 4 kinds of information given by the state - angle of the pole, position of the cart
# An agent can have 2 actions - 0 and 1, pushing the cart to the left or right
#
# Designing the neural net:
# We will have one input layer that has 4 input nodes. We will have 3 hidden layers. We will have 2 output nodes in
# the output layer, corresponding to the action 0 or action 1.
#
# Let's code it up now in Keras.
#
# The fit() method feeds the input and output pairs to the model. Then the model will train on those data to approximate
# the output based on the input.
#
# Suppose the pole is tilted towards the right, then the expected reward of pushing right button will be higher as the
# pole can survive longer.
# The loss function for the DQN will be ((reward + gamma * argmax(Q(s, a'))) - Q(s, a))^2. Gamma is some sort of
# discount or decay rate. Immediate reward is valued higher than future reward.
#
# Remember
# The algorithm tends to forget the previous experiences as it overwrites them with new experiences. We need a list of
# previous experiences and observations to re-train the model with the previous experiences. We call this array of
# experiences memory and use remember() function to append state, action, reward and the next state to the memory.
#
# Replay
# A method that trains the neural net with experiences from the memory is called replay(). First, we sample some
# experiences from the memory and call them minibatch.
#
# Act
# Agent will randomly select its action by a certain percentage, called "exploration rate" or "epsilon". When it is not
# deciding the action randomly, the agent will predict the reward value based on the current state and pick the most
# rewarding action.
#
# epsilon_decay: we want to decrease the number of explorations as it gets good at playing games
# epsilon_min: we want the agent to explore at least this amount
#
# Now we will talk about the improvements
# Credits:
# https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-4-deep-q-networks-and-beyond-8438a3e2b8df
#
# Separate Target Network: We will utilize a second network during the training procedure. The second network is used
# to generate the target Q values that will be used to compute the loss for every action during the training. The issue
# with using just one network is that at every step of the training, the Q-network's values shift and we are using a
# constantly shifting set of values to adjust our network values.
#
#
#
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import backend as K
import gym
import numpy as np
import random
from collections import deque

EPISODES = 1000


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = 0.001
        self.model = self._build_model()
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

    def _huber_loss(self, target, prediction):
        error = prediction - target
        return K.mean(K.sqrt(1 + K.square(error)) - 1, axis=-1)

    def _build_model(self):
        # Neural Net for Deep Q Learning
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss=self._huber_loss, optimizer=Adam(lr=self.learning_rate))
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        action_values = self.model.predict(state)
        return np.argmax(action_values[0])

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            # If done, make our target reward
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)


# Let's code the main function now so that we can see how the dots get connected
def main():
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    agent = DQNAgent(state_size, action_size)
    agent.load("./save/cartpole-dqn.h5")
    batch_size = 32

    for e in range(EPISODES):
        state = env.reset()
        state = np.reshape(state, (1, state_size))
        for time in range(500):
            env.render()
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            reward = reward if not done else -10
            next_state = np.reshape(next_state, (1, state_size))
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}".format(e, EPISODES, time, agent.epsilon))
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)
            # if e % 10 == 0:
            #     agent.save("./save/cartpole-dqn.h5")


if __name__ == "__main__":
    main()







