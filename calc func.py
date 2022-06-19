# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.  
# Обработать ошибку: “Деление на ноль” 
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def calc():
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    operations = input('+-/*: ')
    try:
        if operations == '+':
            print(first_number+second_number)
        elif operations == '-':
            print(first_number-second_number)
        elif operations == '*':
            print(first_number*second_number)
        elif operations == '/':
            print(first_number/second_number)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    calc_onemore()
def calc_onemore():
    a = input('Plese, enter 0 if you want to exit: ')
    if a == '0':
        print('Good bye')
    else:
        calc()
calc()


