import numpy as np, random
from theory import SCALE, neighbors, interval_reward, cadence_bonus

class QLearner:
    def __init__(self, gamma=0.92, alpha=0.35, eps_start=0.9, eps_end=0.05, eps_decay=0.995):
        self.gamma, self.alpha = gamma, alpha
        self.eps, self.eps_min, self.eps_decay = eps_start, eps_end, eps_decay
        self.note_to_idx = {n:i for i,n in enumerate(SCALE)}
        self.idx_to_note = {i:n for n,i in self.note_to_idx.items()}
        self.Q = np.zeros((len(SCALE), len(SCALE)), dtype=float)

    def choose_action(self, state_note):
        s = self.note_to_idx[state_note]
        if random.random() < self.eps:
            return random.choice(list(neighbors(state_note)))
        neigh = list(neighbors(state_note))
        if not neigh:
            return random.choice(SCALE)
        scores = [(self.Q[s, self.note_to_idx[a]], a) for a in neigh]
        return max(scores, key=lambda x: x[0])[1]

    def update(self, s_note, a_note, reward, s_next_note):
        s = self.note_to_idx[s_note]; a = self.note_to_idx[a_note]; s_next = self.note_to_idx[s_next_note]
        td_target = reward + self.gamma * np.max(self.Q[s_next])
        self.Q[s, a] += self.alpha * (td_target - self.Q[s, a])

    def decay_eps(self):
        self.eps = max(self.eps_min, self.eps * self.eps_decay)

def episode(agent, length=16, start_note="C4"):
    path, total = [start_note], 0.0
    for _ in range(length-1):
        s = path[-1]
        a = agent.choose_action(s)
        r = interval_reward(s, a)
        if len(path) >= 2:
            prev = path[-2]
            if (prev < s and s < a) or (prev > s and s > a):
                r += 0.05
        agent.update(s, a, r, a)
        path.append(a)
        total += r
    total += cadence_bonus(path)
    agent.decay_eps()
    return path, total
