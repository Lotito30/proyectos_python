import random


class Tictactoe:
    def __init__(self):
        self.ganador = False
        self.tablero = ['_' if _ < 6 else ' ' for _ in range(9)]

    def print_tabla(self):
        for filas in [self.tablero[j*3:(j+1)*3] for j in range(3)]:
            print('|'.join(filas))

    def ingresar_jugada_al_tablero(self, movimiento, player):
        for i in range(len(self.tablero)):
            if (i == movimiento-1) and (self.tablero[movimiento-1] == '_' or self.tablero[movimiento-1] == ' '):
                self.tablero.pop(movimiento-1)
                self.tablero.insert(movimiento-1, player)
                return True

    def movimientos_disponibles(self):
        return [i+1 for (i, libre) in enumerate(self.tablero) if libre == '_' or libre == ' ']

    def jugadas_ganadoras(self):
        ganador = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                   [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        return ganador

    def ver_ganador(self, player):
        lista_ganadora = []
        for i in self.jugadas_ganadoras():
            for j in i:
                if j in player.jugadas:
                    lista_ganadora.append(j)
                    if len(lista_ganadora) == 3:
                        self.ganador = True
                        return print(f'El ganador es ¡¡¡¡{player}!!!!'.upper())
            else:
                lista_ganadora.clear()

    def jugar(self, play):
        if play:
            print(f'Empieza el Player 1, la letra X.')
            tictactoe.print_tabla()
        letra = 'X'
        while not self.ganador:
            print(
                f'Movimientos Disponibles: {tictactoe.movimientos_disponibles()}')
            if letra == 'X':
                movimiento = player1.movimiento()
                player = player1
            else:
                movimiento = computer.movimiento()
                player = computer

            if tictactoe.ingresar_jugada_al_tablero(movimiento, letra):
                print(
                    f'La letra {letra}, Hizo su jugada en el cuadrado {movimiento}')
                tictactoe.print_tabla()
                print(' ')
                tictactoe.ver_ganador(player)
                if len(self.movimientos_disponibles()) == 0 and self.ganador == False:
                    print('Empate!'.upper())
                    self.ganador = True
                    break
            letra = '0' if letra == 'X' else 'X'


class Player:
    def __init__(self):
        self.jugadas = []

    def __str__(self):
        return 'Player 1'

    def movimiento(self):
        cuadrado_valido = False
        numero = None
        while not cuadrado_valido:
            print('_______________________________________')
            try:
                numero = int(input('X, Ingrese un numero del 1-9: '))
            except:
                print('Debes Ingresar un numero del 1-9')
                continue
            if numero in tictactoe.movimientos_disponibles():
                self.jugadas.append(numero)
                break
            else:
                print('Movimiento no disponible!!!')
                print(
                    f'Movimientos Disponibles: {tictactoe.movimientos_disponibles()}')
                tictactoe.print_tabla()
                continue
            cuadrado_valido = True    
        return numero


class Computer:
    def __init__(self):
        self.player_0 = '0'
        self.jugadas = []

    def __str__(self):
        return 'Computer'

    def movimiento(self):
        validar = random.choice(tictactoe.movimientos_disponibles())
        self.jugadas.append(validar)
        return validar


if __name__ == '__main__':
    tictactoe = Tictactoe()
    computer = Computer()
    player1 = Player()
    tictactoe.jugar(True)


#tictactoe = Tictactoe()
# tictactoe.jugar(Player.movimiento,Computer.movimiento,True)
# tictactoe.buscar_casila(self.player_x,self.player_X)
