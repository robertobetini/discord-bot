import threading

def set_interval(func, time):

def hello(name, time):
  t = threading.Timer(time, hello, args=[name, time])
  print(f'Hello {name}!')
  t.start()

hello('Roberto', 1)
hello('Frutose', 2)

