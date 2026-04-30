variavel = "global"

def local():
    variavel = "local"
    print(variavel)

def variavel_global():
    print(variavel)


def global_modificada():
    global variavel
    variavel = "modificada"
    print(variavel)


local()

variavel_global()

global_modificada()
