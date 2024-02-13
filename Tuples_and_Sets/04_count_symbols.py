occurances = {}

for sym in input():
    occurances[sym] = occurances.get(sym, 0) + 1

for sym, times in sorted(occurances.items()):
    print(f"{sym}: {times} time/s")

#text = input()
#for symbol in sorted(set(text)):
#   print(f"{symbol}: {text.count(symbol)} time/s")
