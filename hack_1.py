"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(tx):
    tx = list (tx)
    c = 0
    a = 0
    while c < len(tx):
        a = tx[c:c+3]
        if a[1] in ['a','e','i','o','u']:
            tx[c+1]=tx[c+1].upper()
        c = c+3
    return ''.join(tx)

#print(fn_hack_1('fooziman'))