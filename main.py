import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == "-":
        result = num1 - num2
    elif operador == "*":
        result = num1 * num2
    elif operador == "/":
        result = num1 / num2
    elif operador == "^":
        result = num1 ^ num2
    return result

def menu():
    try:
        num1 = float(input("Introduza o primeiro número: "))
        num2 = float(input("Introduza o segundo número: "))
    except: raise ValueError
    while True:
        print("\nIndique a operação que pretende realizar com estes números:"
              f"\n[1] - Somar {num1} com {num2}\n[2] - Subtrair {num1} por {num2}"
              f"\n[3] - Multiplicar {num1} por {num2}\n[4] - Dividir {num1} por {num2}"
              f"\n[5] - Potenciar {num1} com expoente {num2}")
        try:
            escolha = int(input("> "))
            match escolha:
                case 1: operador = "+"
                case 2: operador = "-"
                case 3: operador = "*"
                case 4: operador = "/"
                case 5: operador = "^"
                case _: raise Exception
        except ValueError:
            print('\nDados inválidos! -> Tente novamente!')
            time.sleep(2)
            continue
        except Exception:
            print('\nEscolha fora das opções! -> Tente novamente!')
            time.sleep(2)
            continue
        break
    return [num1, num2, operador]

if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            
            menu()


        except ValueError:
            print('\nDados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('\nImpossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
        break

    print('\nVolte sempre!\n')
