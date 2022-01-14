def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor



def run():
    num = input("ingresa un numero : ")
    assert num.isnumeric(), "Debes ingresar un Numero"
    print(divisor(int(num)))
    print("termino mi programa")
   

if __name__ == '__main__':
    run()