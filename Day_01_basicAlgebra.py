# Here i will make an functio from scratch which will help in solving one step equation
# to find x we will add or substract an costant from both side so that x can be evaluated

def oneStepEquation(constant):
    x = 10 - constant
    while True:
        if x + constant == 10:
            return x
print(oneStepEquation(5)) 