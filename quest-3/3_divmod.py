
# fonction fiha 2 parametre
def div_mod(a, b):
    div = a // b  # la division
    mod = a % b   # lmodulo
    return div, mod  # return division and modulo


a = 13
b = 2

div, mod = div_mod(a, b)

print(div)
print(mod)
