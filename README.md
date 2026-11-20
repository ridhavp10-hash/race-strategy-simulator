# Race Strategy Simulator

A pure-Python simulator that compares tyre strategies in a motorsport race.

## How it works
- A Tyre class tracks grip, wear and age; grip drops every lap.
- Lost grip makes each lap slower (0.1 s per grip point).
- strategy_time() adds all stints plus a time loss per pit stop.
- The program compares strategies and prints the fastest.

## Run
```
python race.py
```

## Result (30 laps, 20 s pit loss)
- All soft: 2823.75 s
- All hard: 2762.17 s
- Soft 10 + hard 20: 2777.2 s
- Best: All hard. The pit stop costs more than it saves.

## What went wrong
My first run gave a NameError because I used the Tyre class before defining it, and I learned that Python reads a file from top to bottom. I also wrote the number 80 directly into a penalty formula, which only worked for one tyre, so I stored the starting grip and used constants instead.

## What I learned
I learned how to use a class to give each tyre its own grip, wear and age, so I could simulate a race lap by lap. I also learned that the tyre that's fastest at the start doesn't always win the race, because wear and pit-stop time add up over 30 laps.