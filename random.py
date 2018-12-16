import gym
env = gym.make('Breakout-v0')
state = env.reset()
while True:
   action = env.action_space.sample()
   state, reward, done, info = env.step(action)
   env.render()
   if reward > 0:
        print(reward)
   if done:
        env.reset()
