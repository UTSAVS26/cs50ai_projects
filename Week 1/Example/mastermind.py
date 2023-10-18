from logic import *

colors = ["red", "blue", "green", "yellow"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color} {i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color} 0"),
        Symbol(f"{color} 1"),
        Symbol(f"{color} 2"),
        Symbol(f"{color} 3")
    ))

# Only one position per color.
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.add(Implication(
                    Symbol(f"{color} {i}"), Not(Symbol(f"{color} {j}"))
                ))

# Only one color per position.
for i in range(4):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                knowledge.add(Implication(
                    Symbol(f"{c1} {i}"), Not(Symbol(f"{c2} {i}"))
                ))

knowledge.add(Or(
    And(Symbol("red 0"), Symbol("blue 1"), Not(Symbol("green 2")), Not(Symbol("yellow 3"))),
    And(Symbol("red 0"), Symbol("green 2"), Not(Symbol("blue 1")), Not(Symbol("yellow 3"))),
    And(Symbol("red 0"), Symbol("yellow 3"), Not(Symbol("blue 1")), Not(Symbol("green 2"))),
    And(Symbol("blue 1"), Symbol("green 2"), Not(Symbol("red 0")), Not(Symbol("yellow 3"))),
    And(Symbol("blue 1"), Symbol("yellow 3"), Not(Symbol("red 0")), Not(Symbol("green 2"))),
    And(Symbol("green 2"), Symbol("yellow 3"), Not(Symbol("red 0")), Not(Symbol("blue 1")))
))

knowledge.add(And(
    Not(Symbol("blue 0")),
    Not(Symbol("red 1")),
    Not(Symbol("green 2")),
    Not(Symbol("yellow 3"))
))

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)