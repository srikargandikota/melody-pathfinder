SCALE = ["C4","D4","E4","G4","A4","C5","D5","E5","G5","A5"]
ALLOWED_STEPS = {-2,-1,0,1,2}
idx = {n:i for i,n in enumerate(SCALE)}

def neighbors(note):
    i = idx[note]
    for step in ALLOWED_STEPS:
        j = i + step
        if 0 <= j < len(SCALE):
            yield SCALE[j]

def interval_reward(n1, n2):
    i1, i2 = idx[n1], idx[n2]
    step = abs(i2 - i1)
    if step == 0: return -0.05
    if step == 1: return 0.25
    if step == 2: return 0.15
    return -0.15

def cadence_bonus(path):
    end = path[-1]
    if end.startswith("C") or end.startswith("G"):
        return 0.4
    return 0.0
