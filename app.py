import random

# Establecer la puntuación inicial del jugador
player_score = 0

# Lista de elementos a elegir
elements = ['rock', 'paper', 'scissors']

# Función para obtener la opción del oponente


def get_opponent_option():
  return random.choice(elements)

# Función para determinar el ganador de una ronda


def determine_winner(player_option, opponent_option):
  if player_option == opponent_option:
    return 'Empate'
  elif (player_option == 'rock' and opponent_option == 'scissors') or \
      (player_option == 'paper' and opponent_option == 'rock') or \
      (player_option == 'scissors' and opponent_option == 'paper'):
    return 'Jugador'
  else:
    return 'Oponente'

# Función para obtener la opción del jugador


def get_player_option():
  while True:
    player_option = input("Escribe 'rock', 'paper' o 'scissors': ").lower()
    if player_option in elements:
      return player_option
    else:
      print("Opción no válida. Por favor, inténtalo de nuevo.")

# Función para controlar el flujo del juego


def play_game():
  global player_score
  while True:
    player_option = get_player_option()
    opponent_option = get_opponent_option()
    winner = determine_winner(player_option, opponent_option)
    if winner == 'Jugador':
      player_score += 1
      print(
        f"Has elegido {player_option}. El oponente ha elegido {opponent_option}. ¡Has ganado!")
    elif winner == 'Oponente':
      print(
        f"Has elegido {player_option}. El oponente ha elegido {opponent_option}. Has perdido.")
    else:
      print(
        f"Has elegido {player_option}. El oponente ha elegido {opponent_option}. Es un empate.")
    play_again = input("¿Quieres jugar de nuevo? (Sí/No): ").lower()
    if play_again == 'no':
      break
  print(f"Puntuación final del jugador: {player_score}")


# Iniciar el juego
play_game()
