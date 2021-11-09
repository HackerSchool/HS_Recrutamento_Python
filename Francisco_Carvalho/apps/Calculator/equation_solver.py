import re

def evaluate_expression(expression):
    # we extract the two sides of the equation
    sides = expression.split("=")
    # 4x = 56x + 2

    # First we pass all terms with x to the other side
    # but we need to know what is the variable
    variable = "x"  # default value
    for i in expression:
        if i.isalpha():
            variable = i
            break
    
    valueToRemove = list()
    for i in range(len(sides[1])):
        # 56x + 2
        if sides[1][i] == variable:
            # if we find a variable in the 2nd side
            # x --> we have to go backwards until we get the hole number
            value = variable
            for j in reversed(range(i)):
                if sides[1][j] == " ":
                    break
                else:
                    value = sides[1][j] + value
            # 56x
            #BUG: if its a negative number the - has to be derictly before
            # now we move it tho the left side
            if value[0] == "-":
                # if its a negative number
                sides[0] += " + "+value[1:]
            else:
                sides[0] += " -"+value
            # now we remove the value on the 2nd side
            valueToRemove += [value]
    for i in valueToRemove:
        sides[1] = re.sub(i,'', sides[1])
    # ['4x + 56x -10x', '  +  + 2']
    # now we unite all the values
    unite_first = sides[0].split(" ")
    # ['4x', '+', '56x', '-10x']
    # print(unite_first)
    count_1 = 0
    for i in unite_first:
        if i != '' and i[-1] == "x" and i != "x":
            count_1 += eval(i[:-1])
        elif i == "x":
            count_1 = 1
    # 50

    unite_second = sides[1].split(" ")
    count_2 = 0
    for i in unite_second:
        if i.isnumeric():
            count_2 += eval(i)
    #print(count_1)
    #print(count_2)
    return "--> "+str(variable)+" = " + str(count_2 / count_1)

# print(evaluate_expression("4x = -56x -10x + 2"))