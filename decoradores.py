
def function_decoradora(function_parametro):
    def function_interna(*args):
        #acciones adicionales que decorar
        print("Vamos a realizar un calculo: ")
        function_parametro(*args)
        print("Ya se realizo el calculo.")
    return function_interna


@function_decoradora
def suma(a,b):
    print(a+b)

@function_decoradora
def resta(a,b):
    print(a-b)

suma(7,5)

resta(12,10)