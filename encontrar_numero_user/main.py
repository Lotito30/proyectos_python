import random
import time
def main(n):
    number_computer = 0
    number_user = int(input(f'Numero a adivinar del 1 al {n}?: '))
    life = 3
    while number_user != number_computer:
        if life > 0:
            number_computer = random.randint(1,n)
            if number_computer != number_user:
                print(f'The number is {number_computer}')
                time.sleep(1)
                print(f'The number {number_computer} not is correct.\nComputer try again\n...')               
                time.sleep(2)
                print('Procesando...')
                time.sleep(2)               
            else:
                print(f'Congratulations!! The correct number is {number_computer}')
                break
            life -= 1
        else:
            print(f'Computer You Lose. The correct number is {number_user}')
            break
        
if __name__ == '__main__':
    n = int(input('Numero mayor de adivinanza?: '))
    main(n)