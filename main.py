from rl_agent import QLearner, episode
from midi_io import melody_to_midi

def train_and_compose(episodes=1200, length=16, start="C4", out="melody.mid"):
    agent = QLearner()
    best_path, best_score = None, -1e9
    for _ in range(episodes):
        path, score = episode(agent, length=length, start_note=start)
        if score > best_score:
            best_score, best_path = score, path
    print("Best score:", round(best_score, 3))
    print("Best path:", best_path)
    fp = melody_to_midi(best_path, bpm=96, out_path=out)
    print("Saved:", fp)

if __name__ == "__main__":
    train_and_compose()
