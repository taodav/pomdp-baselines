import gym
from time import time
from tqdm import trange

if __name__ == "__main__":
    import envs
    steps = int(1e7)

    t = time()
    env_name = "WalkerBLT-V-v0"
    env = gym.make(env_name)
    obs = env.reset()
    done = False
    step = 0
    for i in trange(steps):
        next_obs, rew, done, info = env.step(env.action_space.sample())
        step += 1
        if done:
            obs = env.reset()

        # print(step, done, info)

    new_t = time()
    total_runtime = new_t - t
    print(f'Total runtime for {env_name} environment with {steps} steps:', total_runtime)
