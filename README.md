# 🎼 Melody Pathfinder

**Teaching a reinforcement learning agent what makes a melody pleasant.**

Melody Pathfinder is a Q-learning agent that composes melodies by walking a graph of scale tones, guided by a reward function built from music theory, and it exports the best melody it finds as a playable MIDI file.

## The idea

Melody writing has rules that are easy to state and hard to formalize, such as stepwise motion sounding smooth, big leaps sounding jarring, and phrases wanting to resolve home. This project encodes those rules as rewards and lets an agent figure out melodies that satisfy them.

- **State and action space.** The agent moves through a pentatonic-style scale from `C4` to `A5`, where each note can move up to 2 scale steps in either direction.
- **Rewards.** Stepwise motion earns the most (+0.25), repeated notes are lightly penalized, leaps beyond the allowed range are penalized, and continuing in one melodic direction earns a momentum bonus.
- **Cadence bonus.** Melodies that end on C or G (the tonic or dominant) get +0.4, which nudges phrases to resolve.
- **Learning.** Tabular Q-learning with ε-greedy exploration and decay trains over about 1,200 episodes, and the best-scoring melody is rendered to MIDI at 96 BPM.

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
| `theory.py` | The "music critic," with the scale, allowed intervals, reward function, and cadence rules |
| `rl_agent.py` | The tabular Q-learner and its episode loop |
| `midi_io.py` | Renders a note path to MIDI |
| `main.py` | Trains the agent and composes |

## What I learned

Reward design turned out to be product design, because the agent optimizes exactly what you specify, and a naive reward function produces melodies that are technically optimal and musically boring. The momentum bonus and the cadence rule both came from listening to outputs and asking myself what was missing. That is the same loop as shipping any product; you define the metric, watch the behavior it rewards, and then go back and refine it.
