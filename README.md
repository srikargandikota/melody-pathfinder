# 🎼 Melody Pathfinder

**Can a reinforcement-learning agent learn what makes a melody pleasant?**

A Q-learning agent that composes melodies by walking a graph of scale tones, guided by a reward function built from music theory, then exports the best one it finds as a playable MIDI file.

## The idea

Melody writing has rules that are easy to state and hard to formalize: stepwise motion sounds smooth, big leaps sound jarring, phrases want to resolve home. This project encodes those rules as rewards and lets an agent discover melodies that satisfy them:

- **State/action space:** a pentatonic-style scale (`C4`–`A5`) where each note can move up to 2 scale steps in either direction
- **Rewards:** stepwise motion earns the most (+0.25), repeated notes are lightly penalized, leaps beyond the allowed range are penalized, and continuing a melodic direction earns a momentum bonus
- **Cadence bonus:** melodies that end on C or G (tonic/dominant) get +0.4, nudging phrases to resolve
- **Learning:** tabular Q-learning with ε-greedy exploration and decay, trained over ~1,200 episodes; the best-scoring melody is rendered to MIDI at 96 BPM

## Run it

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py              # trains, prints the best melody, saves melody.mid
```

Open `melody.mid` in any DAW or media player to hear the result.

## Files

| File | Role |
|---|---|
| `theory.py` | The "music critic": scale, allowed intervals, reward function, cadence rules |
| `rl_agent.py` | Tabular Q-learner + episode loop |
| `midi_io.py` | Renders a note path to MIDI |
| `main.py` | Trains and composes |

## What I learned

Reward design *is* product design. The agent optimizes exactly what you specify, and a naive reward function produces technically-optimal, musically-boring melodies. The momentum bonus and cadence rule came from listening to outputs and asking "what's missing?", which is the same loop as shipping any product: define the metric, observe the behavior it incentivizes, refine.
