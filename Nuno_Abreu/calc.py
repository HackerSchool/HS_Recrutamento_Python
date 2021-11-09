

def main(x):
    print(f'''Bem vind@ a calculadora {x}.
Por favor use:
    + para soma;
    - para subtracao;
    * para multiplicacao;
    / para divisao;
    ** para expoente.

Para sair pressione <Enter>''')
    exp = input()
    if not exp:
        return 's'
    print(calc(exp))


def calc(y):
    exp = []
    if type(y) == str:
        j = 0
        i = 0
        while i < len(y):
            if y[i] != ' ':
                exp.insert(j, y[i])
                j += 1
                if y[i].isnumeric() and i < len(y) - 1:
                    k = i + 1
                    while y[k].isnumeric():

                        exp[j - 1] = exp[j - 1] + y[k]
                        i += 1
                        k += 1
                        if k >= len(y):
                            break
                i += 1
            else:
                i += 1
    else:
        exp = y

    if '(' in exp:
        par_o = exp.index('(')
        par_c = len(exp) - exp[-1::-1].index(')') - 1
        nlist = []
        for i in range(1, par_c - par_o, 1):
            nlist.insert(i, exp[par_o + i])
        val_t = calc(nlist)
        for i in range(par_c - par_o, -1, -1):
            exp.pop(par_o + i)
            if i == 0:
                exp.insert(par_o, val_t)

    while True:
        if '*' in exp:
            mult = exp.index('*')
            if exp[mult + 1] != '*':
                val = float(exp[mult - 1]) * float(exp[mult + 1])
                exp[mult - 1] = val
                exp.pop(mult + 1)
                exp.pop(mult)

            else:
                val = float(exp[mult - 1]) ** float(exp[mult + 2])
                exp[mult - 1] = val
                exp.pop(mult + 2)
                exp.pop(mult + 1)
                exp.pop(mult)

        else:
            break
    while True:
        if '/' in exp:
            div = exp.index('/')
            val = float(exp[div - 1]) / float(exp[div + 1])
            exp[div - 1] = val
            exp.pop(div + 1)
            exp.pop(div)
        else:
            break
    while True:
        if '-' in exp:
            sub = exp.index('-')
            val = float(exp[sub - 1]) - float(exp[sub + 1])
            exp[sub - 1] = val
            exp.pop(sub + 1)
            exp.pop(sub)
            print(exp)
        else:
            break
    while True:
        if '+' in exp:
            som = exp.index('+')
            val = float(exp[som - 1]) + float(exp[som + 1])
            exp[som - 1] = val
            exp.pop(som + 1)
            exp.pop(som)
        else:
            break
    return exp[0]
