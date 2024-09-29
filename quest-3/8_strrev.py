def str_rev(s):
    reversed_string = ''  # nsawbo string khawi njem3o fih dakchi meglob
    for char in s:  # nloopiw 3la les caracteres
        reversed_string = char + reversed_string
    return reversed_string

s = "hello hi 12345"
s = str_rev(s)
print(s)
