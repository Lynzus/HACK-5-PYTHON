"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(tx):
    tx = list(tx)
    if len(tx) > 0:    
        for i in range(len(tx)):
            tx[i]=str(i+1)
            if i % 2 == 0 and i != 0:
                tx[i-1] = '-'
    else:
        tx=['0']
    return tx