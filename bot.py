import discord
import usuarios as us
import dinheiro as din

client = discord.Client()
key = '$$'
usuarios = us.load_users()

@client.event
async def on_ready():
    print('Ready!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  channel = message.channel

  ############ATALHOS##############
  msg = message.content.split(' ')
  author = message.author
  mention = message.author.mention
  #################################

  if msg[0] == f'{key}oi':
    await channel.send(f'{mention} oi')

  elif msg[0] == f'{key}criar': #OK
    await channel.send(us.add_user(author, usuarios))
    us.update_users(usuarios)

  elif msg[0] == f'{key}saldo': #OK
    saldo = din.checar_saldo(str(author), usuarios)
    await channel.send(f'{mention} o seu saldo atual é de: R$ {saldo}')

#din.set_interval_salario(usuarios, 0.01, 1) # os usuários recebem 0.01 a casa 1 segundo

client.run('NjkzNjYxNjAxMzQ1MDQ0NDkz.Xv4czw.pWcmonEBhh91Lor_7blq7zGdQl0')