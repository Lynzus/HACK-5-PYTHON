"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(tx):
    tx = list(tx)
    if len(tx) > 0:    
        for i in range(len(tx)):
            if i % 2 == 0:
                tx[i]=str(i+1)
            else:
                tx[i]=i+1
    else:
        tx.append(0)
    return tx
print(fn_hack_7(''))