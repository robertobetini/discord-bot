import threading

def set_interval(func, time):
  e = threading.Event()
  while not e.wait(time):
    func()

def set_interval_salario(dic_usuarios, valor, time):
  e = threading.Event()
  while not e.wait(time):
    salario(dic_usuarios, valor)

def salario(dic_usuarios, valor):
  for usuario in dic_usuarios:
    dic_usuarios[usuario]['saldo'] += valor

def checar_saldo(usuario, dic_usuarios):
  return dic_usuarios[usuario]['saldo']