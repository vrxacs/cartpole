import gym
env = gym.make('CartPole-v0')
testParams = [0.2555534643279024, 0.009521762075349494, 0.906790425870466, 0.8604403044119583]
observation = env.reset()
for t in range(200):
    env.render()
    print("Step {}".format(t))
    print(observation)
    w_sum = sum([w * x for w, x in zip(testParams, observation)])
    action = action = 0 if w_sum < 0 else 1
    print(w_sum)
    print(action)
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
raw_input("Press Enter to terminate...")