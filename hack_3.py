"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
empieza y termina en mayus, si el caracter no es un numero (title)
termina en mayus si es mayor a 2
"""


def fn_hack_3(tx):
    tx = list(tx)
    for i in range(len(tx)):
        if tx[i] in ['a','e','i','o','u']:
            if tx[i]=='a':
                tx[i]='@'
            elif tx[i]=='e':
                tx[i]='3'
            elif tx[i]=='i':
                tx[i]='¡'
            elif tx[i]=='o':
                tx[i]='0'
            elif tx[i]=='u':
                tx[i]='v'
    tx=''.join(tx)
    if tx[0:1]!='3':
        tx=tx.capitalize()
    else:
       tx = tx[:len(tx)-1] + tx[len(tx)-1].capitalize()
    if len(tx)>2:
       tx = tx[:len(tx)-1] + tx[len(tx)-1].capitalize()
       print(tx)
    return tx