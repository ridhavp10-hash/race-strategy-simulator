MAX_GRIP = 100
TIME_LOSS_PER_GRIP = 0.1
BASE_TIME = 90
PIT_LOSS = 20


class Tyre:
    def __init__(self, name, grip, wear):
        self.name = name
        self.grip = grip
        self.wear = wear
        self.age = 0

    def drive_lap(self):
        self.grip = max(0, self.grip - self.wear)
        self.age += 1

    def lap_time(self, base_time):
        return base_time + (MAX_GRIP - self.grip) * TIME_LOSS_PER_GRIP


def stint_time(name, grip, wear, laps, base_time):
    tyre = Tyre(name, grip, wear)
    total = 0
    for _ in range(laps):
        total += tyre.lap_time(base_time)
        tyre.drive_lap()
    return total


def strategy_time(stints, base_time, pit_loss):
    total = 0
    for name, grip, wear, laps in stints:
        total += stint_time(name, grip, wear, laps, base_time)
    total += pit_loss * (len(stints) - 1)
    return round(total, 2)


SOFT = ("soft", 95, 2.5)
HARD = ("hard", 80, 0.05)

strategies = {
    "All soft": [(*SOFT, 30)],
    "All hard": [(*HARD, 30)],
    "Soft 10 + hard 20": [(*SOFT, 10), (*HARD, 20)],
}

results = {}
for label, stints in strategies.items():
    results[label] = strategy_time(stints, BASE_TIME, PIT_LOSS)
    print(f"{label}: {results[label]}")

best = min(results, key=results.get)
print("Best strategy:", best)