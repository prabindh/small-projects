import numpy as np


class ReplayMemory:
    def __init__(self, max_size):
        self.max_size = max_size
        self.counter = 0
        self.experiences = [None] * self.max_size

    def add_experience(self, experience):
        self.experiences[self.counter % self.max_size] = experience
        self.counter += (1 if self.counter < self.max_size else 0)

    def sample_experiences(self, sample_size):
        # random choice from counter makes it possible
        # to sample when not filled
        indices = np.random.choice(self.counter, size=sample_size, replace=False)
        sample = [self.experiences[ind] for ind in indices]
        return sample