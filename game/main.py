import random

options = ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0

rounds = 1
while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)

  value = input('Elija piedra, papel o tijera =>')
  user_option = value.lower()

  if not user_option in options:
    print('esa opción no es válida')
    continue

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)

  if user_option == computer_option:
      print('¡Empate!')
  elif user_option == 'piedra':
      if computer_option == 'tijera':
          print('piedra gana a tijera')
          print('user ganó!')
          user_wins += 1
      else:
          print('papel gana a piedra')
          print('computer ganó!')
          computer_wins += 1
  elif user_option == 'papel':
      if computer_option == 'piedra':
          print('papel gana a piedra')
          print('user ganó!')
          user_wins += 1
      else:
          print('tijera gana a papel')
          print('computer ganó!')
          computer_wins += 1
  elif user_option == 'tijera':
      if computer_option == 'papel':
          print('tijera gana a papel')
          print('user ganó!')
          user_wins += 1
      else:
          print('piedra gana a tijera')
          print('computer ganó!')
          computer_wins += 1

  if computer_wins == 2:
    print('El ganador es el computador')
    break
  if user_wins == 2:
    print('El ganador es el usuario')
    break
  rounds += 1