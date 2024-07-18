import gym
import numpy as np

# PID Controller class
class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.previous_error = 0
        self.integral = 0

    def get_action(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return 0 if output < 0 else 1

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    pid = PIDController(Kp=1.0, Ki=0.0, Kd=0.1)
    
    EPISODES = 100
    for e in range(EPISODES):
        state = env.reset()
        done = False
        time = 0
        while not done:
            env.render()
            angle = state[2]
            action = pid.get_action(angle, 0.02)  # 0.02 is the timestep for each iteration
            next_state, reward, done, _ = env.step(action)
            state = next_state
            time += 1
            if done:
                print(f"Episode: {e + 1}/{EPISODES}, Score: {time}")
                break
    env.close()
