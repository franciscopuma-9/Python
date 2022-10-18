# import re
# # def arithmetic_arranger(problems):
# #
# #
# #     return arranged_problems
# # print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
#
# list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
# lista = []
# for valor in list:
#     x = lista.split(" ")[0]
#     lista.append(x)
# aux = 0
# for valor in lista:
#     if len(valor[0]) > len(valor[2]):
#         aux = len(valor[0]) + 2
#     else:
#         aux = len(valor[2]) + 2
#
#     valor.append(aux)
#     if valor[1] == '+':
#         suma = int(valor[0])+int(valor[2])
#     else:
#         suma = int(valor[0]) - int(valor[2])
#     valor.append(str(suma))
# segundovalor = 0
# xd1 = ' '*(int(lista[0][3])-len(lista[0][0]))+lista[0][0]+'\t'+' '*(int(lista[1][3])-len(lista[1][0]))+lista[1][0]+'\t'+' '*(int(lista[2][3])-len(lista[2][0]))+lista[2][0]+'\t'+' '*(int(lista[3][3])-len(lista[3][0]))+lista[3][0]
# xd2 = lista[0][1]+' '* (lista[0][3]-1)+'\t'+lista[1][1]+' '* (lista[1][3]-1)+'\t'+lista[2][1]+' '* (lista[2][3]-1)+'\t'+lista[3][1]+' '* (lista[3][3]-1)
# xd3 = ' '*(int(lista[0][3])-len(lista[0][2]))+lista[0][2]+'\t'+' '*(int(lista[1][3])-len(lista[1][2]))+lista[1][2]+'\t'+' '*(int(lista[2][3])-len(lista[2][2]))+lista[2][2]+'\t'+' '*(int(lista[3][3])-len(lista[3][2]))+lista[3][2]
# xd4 ='-'*lista[0][3]+'\t'+'-'*lista[1][3]+'\t'+'-'*lista[2][3]+'\t'+'-'*lista[3][3]
# xd5 =' '*(int(lista[0][3])-len(lista[0][4]))+lista[0][4]+'\t'+' '*(int(lista[1][3])-len(lista[1][4]))+lista[1][4]+'\t'+' '*(int(lista[2][3])-len(lista[2][4]))+lista[2][4]+'\t'+' '*(int(lista[3][3])-len(lista[3][4]))+lista[3][4]
# xdsupremo = xd1 + '\n' + xd2 + '\n' + xd3 + '\n' + xd4 + '\n'
# if segundovalor:
#     xdsupremo +=xd5
# print(xdsupremo)

import re

def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    primero = ""
    segunda = ""
    lineas = ""
    sumatoria = ""
    for problema in problems:
        if (re.search("[^\s\d.+-]", problema)):
            if (re.search("[/]", problema)) or re.search('[*]', problema):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        primerNumero = problema.split(" ")[0]
        operador = problema.split(" ")[1]
        segundoNumero = problema.split(" ")[2]
        if (len(primerNumero) >= 5 or len(segundoNumero) >= 5):
            return "Error: Numbers cannot be more than four digits."

        suma = ""
        if operador == "+":
            suma = str(int(primerNumero) + int(segundoNumero))
        elif operador == "-":
            suma = str(int(primerNumero) - int(segundoNumero))
        tamanio = max(len(primerNumero), len(segundoNumero)) + 2
        arriba = str(primerNumero).rjust(tamanio)
        abajo = operador + str(segundoNumero).rjust(tamanio - 1)
        linea = "-" * tamanio
        resultado = str(suma).rjust(tamanio)

        if problema != problems[-1]:
            primero += arriba + "    "
            segunda += abajo + "    "
            lineas += linea + "    "
            sumatoria += resultado + "    "
        else:
            primero += arriba
            segunda += abajo
            lineas += linea
            sumatoria += resultado
    if solve:
        arranged_problems = primero + "\n" + segunda + "\n" + lineas + "\n" + sumatoria
    else:
        arranged_problems = primero + "\n" + segunda + "\n" + lineas
    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))



# import re
# top = ''
# list = ["324 + 69", "381 - 22", "457 + 843", "9123 + 449"]
# for i in list:
#     firstValor = i.split(' ')[0]
#     print(firstValor)
#     top += firstValor.rjust(5)
#     print(top)
