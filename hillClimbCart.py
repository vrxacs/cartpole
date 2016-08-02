import gym
import random
env = gym.make('CartPole-v0')


def test(param):
    step = 0.0
    # TODO: Consider averaging more than a 100 runs to get a better idea of how good the parameters are
    for j in range(100):
        observation = env.reset()
        for t in range(200):
            step += 1
            w_sum = sum([w * x for w, x in zip(param, observation)])
            action = 0 if w_sum < 0 else 1
            observation, reward, done, info = env.step(action)
            if done:
                break
    return step/100.0

# Init params
params = []
for i in range(4):
    params.append(random.random())

# Hillclimbing
old_params = params
old_result = 0
result = 0
for t in range(10000):
    if result == 200:
        print "Early end!"
        break

    print "Episode: {}".format(t)
    result = test(params)
    print "Score: {}".format(result)

    if result > old_result:
        print "SWITCH!!!"
        old_params = list(params)

    old_result = result
    params = [a + random.uniform(-0.1, 0.1) for a in params]

print "End!"
print "Score: {}".format(old_result)
print "With params: {}".format(old_params)
env.render()
observation = env.reset()
# TODO: this duplicates the above, take it out in a separate function
for t in range(200):
    w_sum = sum([w*x for w, x in zip(old_params, observation)])
    action = 0 if w_sum < 0 else 1
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
raw_input("Press Enter to terminate...")