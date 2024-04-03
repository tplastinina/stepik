scopes = {
    'global': {
        'parent': None, 
        'vars': set()
    }
}

def create_f(namesp: str, parent: str): #создание нового пространства имён
    scopes[namesp] = {'parent': parent, 'vars': set()}


def add_f(namesp: str, var_name: str): #Добавление в пространство переменной
    scopes[namesp]['vars'].add(var_name)


def get_f(namesp: str, var_name: str): #Поиск имени пространства
    while namesp != None and var_name not in scopes[namesp]['vars']:
        namesp = scopes[namesp]['parent']
    return namesp



n = int(input())

for i in range(n):
    cmd, namesp, arg = input().split() 
    if cmd=="create":
        create_f(namesp, arg)
    if cmd=="add":
        add_f(namesp, arg)
    if cmd=="get":
        print(get_f(namesp, arg))
