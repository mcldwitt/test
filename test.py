import gym
from gym import wrappers

env = gym.make('CartPole-v0')
env = wrappers.Monitor(env, "/tmp/gym-results1")
for episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()