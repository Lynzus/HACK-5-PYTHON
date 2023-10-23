"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(tx):
    tx = list(tx)
    if len(tx) > 3:
        tx.pop(len(tx)-1)
        tx.pop(0)
    print(tx)
    return ''.join(tx)
fn_hack_4('2')