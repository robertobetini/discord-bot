
######################carregando as tags de usuários cadastrados##########################
def load_users():

  '''
  Carrega todos os usuários ja cadastrados.
  '''

  usuarios = {}
  try:
    file = open('users/all.txt', 'x')
  except:
    file = open('users/all.txt', 'r')
    file_content = file.read().split(',')[:-1] # o último elemento sempre é uma string vazia
    print(file_content)
    #carregando o inventário dos usuários
    for user in file_content:
      items = {}
      with open(f'users/{user}.txt') as inv:
        #verificando cada linha do arquivo
        for line in inv:
          if '\n' in line: # removendo a quebra de linha ao final
            line = line[:-1]
          line = line.split('=')

          try:
            line[1] = int(line[1]) # os números de frutas no inventário precisam ser ints
          except:
            line[1] = float(line[1]) # o saldo do usuário precisa ser float

          items[line[0]] = line[1]
      usuarios[user] = items
  file.close()
  return usuarios
##########################################################################################


def add_user(usuario, dic_usuarios):

  '''
  Abre uma conta no banco para o usuário especificado.
  '''

  if str(usuario) in dic_usuarios:
    return f'{usuario.mention} já possui conta no banco!'
  dic_usuarios[usuario] = {'saldo': 0.00}
  file = open('users/all.txt', 'a')
  file.write(f'{usuario},')
  file.close()
  return f'{usuario.mention} conta aberta com sucesso!\nSaldo atual: {dic_usuarios[usuario]["saldo"]}'



def update_users(usuarios):

  '''
  Atualiza os arquivos de inventário dos usuários com os valores atuais 
  do dicionário usuários.
  '''
  
  for user in usuarios:
    file = open(f'users/{user}.txt', 'w')
    for k in usuarios[user]:
      file.write(f'{k}={str(usuarios[user][k])}\n')
    file.close()