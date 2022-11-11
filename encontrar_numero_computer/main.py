import random
def main():
    random_numero = random.randint(1,10)
    numero = 0
    oportunidad = 3
    print('Adivina un numero del 1 al 10')
    while numero != random_numero:
        if oportunidad > 0: 
            numero = int(input('Ingresa un numero: '))
            if numero < random_numero:
                print(f'El numero {numero} esta por debajo')
            elif numero > random_numero:
                print(f'El numero {numero} esta por arriba')
            
            else:
                print(f'El numero {numero} es el correcto. Felicitaciones')
                break
            oportunidad -= 1
        else:
            print(f'Perdiste!! El numero correcto era el {random_numero}')        
            break

if __name__=='__main__':
    main()
 

