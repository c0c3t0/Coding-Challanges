def double_letters(string):
    is_double_letters = False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            is_double_letters = True
            break
    return is_double_letters


print(double_letters('hello'))
print(double_letters('nono'))
