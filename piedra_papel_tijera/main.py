import random

def main():
    contador = 0
    resultado_computer = 0
    resultado_user = 0
    while contador < 5:
        computer = random.choice(['Piedra','Papel','Tijera'])
        user = input(f'Round {contador+1}. Piedra,Papel o Tijera?: ').capitalize()
        print('--------------------------------')
        print(f'Computer: {computer}\nUser: {user}')
        print('--------------------------------')
        if (computer == 'Piedra' and user == 'Tijera') or (computer == 'Tijera' and user == 'Papel') or (computer == 'Papel' and user == 'Piedra'):
            print('Computer Win. Congrats!!')
            resultado_computer += 1
        elif (user == 'Piedra' and computer == 'Tijera') or (user == 'Tijera' and computer == 'Papel') or (user == 'Papel' and computer == 'Piedra'):
            print('User Win. Congrats!!')
            resultado_user += 1
        else:
            print(f'Equalizer. Again Round {contador+1}')
            print('--------------------------------')
            continue
        contador += 1 
        print('--------------------------------')
    if resultado_computer >= 3:
        print(f'Computer es el ganador. Resultado: {resultado_computer}-{resultado_user}')
    else:
        print(f'User es el ganador. Resultado: {resultado_user}-{resultado_computer}')
    
if __name__ == '__main__':
    print('Piedra, Papel o Tijera.\nEl ganador es quien pueda ganar 3 de 5.')
    main()