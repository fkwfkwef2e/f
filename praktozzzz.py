import math 
operation = str(input('Введите оператор: ')) 
try: 
    if operation == "cos" or operation == "sin" or operation == "tan" or operation == "sqrt": 
        num = int(input('Введите число: ')) 
    else: 
        firstNum = int(input('Введите 1 число: ')) 
        secondNum = int(input('Введите 2 число: ')) 
except ValueError: 
    print("Вы ввели не число") 
solution = 0 
check = True 
while True: 
    match operation: 
        case "+": 
            if check: 
                solution += (firstNum+secondNum) 
                print(solution) 
            else: 
                solution += otherNum 
                print(solution) 
        case "-": 
            if check: 
                solution += (firstNum-secondNum) 
                print(solution) 
            else: 
                solution -= otherNum 
                print(solution) 
        case "*": 
            if check: 
                solution = (firstNum*secondNum) 
                print(solution) 
            else: 
                solution *= otherNum 
                print(solution) 
        case "/": 
            if check: 
                if secondNum == 0: 
                    print('На ноль делить нельзя!') 
                    break 
                else: 
                    solution += (firstNum/secondNum) 
            else: 
                if otherNum == 0: 
                    print('На ноль делить нельзя!') 
                    break 
                else: 
                    solution /= otherNum 
                    print(solution) 
        case "!": 
            if check: 
                solution += math.factorial(firstNum,secondNum) 
                print(solution) 
            else: 
                solution += math.factorial(solution,otherNum) 
                print(solution) 
        case "pow": 
            if check: 
                solution += math.pow(firstNum,secondNum) 
                print(solution) 
            else: 
                solution += math.pow(solution,otherNum) 
                print(solution) 
        case "sqrt": 
            if check: 
                solution += math.sqrt(num) 
                print(solution) 
            else: 
                solution += math.sqrt(otherNum) 
                print(solution) 
        case "cos": 
            if check: 
                solution += (math.cos(num)) 
                print(solution) 
            else: 
                solution += math.cos(otherNum) 
                print(solution) 
        case "sin": 
            if check: 
                solution += (math.sin(num)) 
                print(solution) 
            else: 
                solution += math.sin(otherNum) 
                print(solution) 
        case "tan": 
            if check: 
                solution += (math.tan(num)) 
                print(solution) 
            else: 
                solution += math.tan(otherNum) 
                print(solution) 
        case _: 
            print('Вы ввели неверный оператор')  
    check = False 
    print('Хотите продолжить? y/n') 
    continueAnswer = str(input()) 
    if continueAnswer == "y": 
        try: 
            print('Введите число: ') 
            otherNum = int(input()) 
        except ValueError: 
            print('Вы ввели не оператор') 
            break 
        print('Введите оператор') 
        operation = str(input()) 
        continue  
    else: 
        break