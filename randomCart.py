import gym
import random
env = gym.make('CartPole-v0')

# Generate 10 000 random parameters
random.seed()
paramsSet = []
for i in range(10000):
    params = []
    for j in range(4):
        params.append(random.random())
    paramsSet.append(params)

# For each parameter set run the environment and record the score
paramsScore = []
for i in range(len(paramsSet)):
    print ("Params #{}".format(i))
    step = 0.0
    for j in range(100):
        observation = env.reset()
        for t in range(200):
            step += 1
            w_sum = sum([w*x for w, x in zip(paramsSet[i], observation)])
            action = 0 if w_sum < 0 else 1
            observation, reward, done, info = env.step(action)
            if done:
                break
    print("Episode finished after {} timesteps".format(step/100.0))
    paramsScore.append(step/100.0)

# Get the best parameters and visualize it
max_index = paramsScore.index(max(paramsScore))
print ("Max score: {}".format(paramsScore[max_index]))
print ("with params: {}".format(paramsSet[max_index]))
env.render()
observation = env.reset()
# TODO: this duplicates the above, take it out in a separate function
for t in range(200):
    w_sum = sum([w*x for w, x in zip(paramsSet[max_index], observation)])
    action = 0 if w_sum < 0 else 1
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
raw_input("Press Enter to terminate...")