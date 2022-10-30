import random

options = ('piedra','papel','tijera')

comp_wins = 0
user_wins = 0

rounds = 1

while True:

  print('*' * 10)
  print(f'ROUND {rounds}')
  print('*' * 10)


  user_opt = input('piedra, papel, tijera ==> ').lower().strip()
  
  if not user_opt in options:
    print('Elige una opción válida')
  
  comp_opt = random.choice(options)
  
  print(f'El usuario eligió ==> {user_opt}')
  print(f'La maquina eligió ==> {comp_opt}')
  
  if user_opt == comp_opt:
    print('Empate')
  
  elif user_opt == 'piedra':
    if comp_opt == 'tijera':
      print('piedra gana a tijera')
      print('user gano')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('comp gano')
      comp_wins += 1
  
  elif user_opt == 'papel':
    if comp_opt == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('comp gano')
      comp_wins += 1
  
  else:
    if user_opt == 'tijera' and comp_opt == 'papel':
      print('tijera gana a papel')
      print('user gano')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('comp gano')
      comp_wins += 1

  print('*' * 10)
  print(f'Puntos USER {user_wins}')
  print(f'Puntos COMPU {comp_wins}')
  print('*' * 10)
  
  if comp_wins == 2:
    print('GANADOR COMPU')
    break
  elif user_wins == 2:
    print('GANADOR USER')
    break

  rounds += 1