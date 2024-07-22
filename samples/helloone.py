import gym
import numpy as np

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = 0
        self.previous_error = 0

    def compute_action(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        action = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return action

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    # PID parameters
    Kp = 0.5
    Ki = 0
    Kd = 1
    pid_controller = PIDController(Kp, Ki, Kd)

    EPISODES = 100

    for e in range(EPISODES):
        state = env.reset()
        done = False
        score = 0
        while not done:
            env.render()
            pole_angle = state[2]
            error = -pole_angle  # error is thec deviation from upright position (angle zero)
            action = 1 if pid_controller.compute_action(error, 1) > 0 else 0

            next_state, reward, done, _ = env.step(action)
            state = next_state
            score += reward

            if done:
                print(f"episode: {e}/{EPISODES}, score: {score}")
                break
    env.close()
