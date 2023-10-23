"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(tx):
    tx2 = tx.copy()
    if len(tx) % 2 == 0:
        for i in range (len(tx)):
            tx[i]=str(len(tx)-i)
    else:
        for i in range (len(tx)):
            tx[i]= tx2[(len(tx))-i-1]+'-'+str(len(tx)-i)
    return tx