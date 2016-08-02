import gym
import random
env = gym.make('CartPole-v0')


def run(param, render):
    step = 0.0
    if render:
        env.render()
    observation = env.reset()
    for t in range(200):
        step += 1
        # TODO: change the below to the gaussian
        w_sum = sum([w * x for w, x in zip(param, observation)])
        action = 0 if w_sum < 0 else 1
        observation, reward, done, info = env.step(action)
        if done:
            break
    return step


def test(param):
    step = 0.0
    # TODO: Consider averaging more than a 100 runs to get a better idea of how good the parameters are
    for j in range(100):
        step += run(param, False)
    return step/100.0

# Init params
params = []
for i in range(4):
    params.append(random.random())

alpha = 0.01
# TODO: We don't need to randomize this, correct?
eps = 0.01

for t in range(10000):

    # Run test(param)?
    res = test(params)
    print "t: ", t
    print "res: ", res

    if res == 200.0:
        print "Reached 200.0 average result! Early end!"
        break

    # Find gradient
    grad = []
    for i in range(len(params)):
        tmp = list(params)
        tmp[i] += eps
        partial = (test(tmp) - res)/eps
        grad.append(partial)

    for i in range(len(params)):
        params[i] += alpha*grad[i]

run(params, True)
raw_input("Press Enter to terminate...")
