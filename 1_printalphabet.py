# Initialize wa7ed string khawi njem3o fih l'alphabet
alphabet = ''

# Iterate through the ASCII values men 'a' l 'z' (men 97 l 122) 
for i in range(97, 123):
    # n'convertéw ascii l charactere a l'aide de chr()
    alphabet += chr(i)

# Print the resulting string
print(alphabet)




'''
# men 65 l 90 bach tprinté l majuscule
alphabet = ''

for i in range (65,91):
    alphabet += chr(i)

print(alphabet)

'''



# autre solution kankhedmo b la fonction range() et ord()

'''
for c in range(ord('a'), ord('z'), 1):  # Step hna ndiro 1 bach netmechaw wa7ed b wa7ed
    print(chr(c), end='')  

print() 

'''