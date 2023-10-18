from logic import *

rain = Symbol("Rain") # It is Raining.
hagrid = Symbol("Hagrid") # Harry visited Hagrid.
dumbledore = Symbol("Dumbledore") # Harry visited Dumbledore.

# First
sentence = And(rain, hagrid)
print(sentence.formula())

# Second
knowledge = Implication(Not(rain), hagrid)
print(knowledge.formula())

# Third
knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)
print(knowledge.formula())

# Fourth
knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)
print(model_check(knowledge, rain))