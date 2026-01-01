# Here i will make an functio from scratch which will help in solving one step equation
# to find x we will add or substract an costant from both side so that x can be evaluated

def oneStepEquation(constant):
    x = 10 - constant
    while True:
        if x + constant == 10:
            return x
        else:
            user_input = int(input("enter again"))
            if user_input > 10:
                print(user_input,"try a number lesser than 10")
            else:
                print(user_input, "try number greater than 0")

        return 0

print(oneStepEquation(5))