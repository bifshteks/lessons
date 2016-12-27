alf = 'abcd'       #input()
res_alf = '*d%#'          #input()

encode = 'abacabadaba'           #input()
decode = '#*%*d*%'          #input()

code = {}
decrypt = {}
for i in range(len(alf)):
    code.update([(alf[i], res_alf[i])])
    decrypt.update([(res_alf[i], alf[i])])

print(code)
res_encode = []
for letter in encode:
    res_encode.append(code[letter])

print(''.join(res_encode))

res_decode = [decrypt[let] for let in decode]
print(''.join(res_decode))
