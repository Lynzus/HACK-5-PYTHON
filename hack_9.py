"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(tx):
    tx = {"Foo":"Fooziman"}

    return tx