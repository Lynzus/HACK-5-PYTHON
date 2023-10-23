"""
generic script
         -  -
text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
cada 2 cosos agregar una raya
"""


def fn_hack_5(tx):
    tx = list(tx)
    for i in range(len(tx)):
        if i % 3 == 0 and i != 0:
            tx[i-1] = '-'
    return ''.join(tx)
print(fn_hack_5(''))