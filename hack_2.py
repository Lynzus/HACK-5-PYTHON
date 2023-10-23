"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
vocales, usa while siempre que manipules el tama;o en listas
"""


def fn_hack_2(tx):
    tx = list(tx)
    i = len(tx)
    while i != 0:
        if tx[i-1] in ['a','e','i','o','u']:
            tx.pop(i-1)
        i=i-1
    return "".join(tx)
