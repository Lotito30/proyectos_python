import time

def cuenta_regresiva(seg):
    while seg:
        minutos, segundos = divmod(seg,60)
        min_seg_format = "{:02d}:{:02d}".format(minutos,segundos)
        print(min_seg_format,end='\r')
        time.sleep(1)
        seg -= 1
    print('Here We Go!')

if __name__ == '__main__':
    seg = int(input('Segundos de la cuenta regresiva?: '))
    cuenta_regresiva(seg)

