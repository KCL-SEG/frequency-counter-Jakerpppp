"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    length = len(items)
    for item in items:
        item = str(item)
        count = 0
        if item not in frequencies.keys():
            for again in items:
                again = str(again)
                if again == item:
                    count += 1
            frequencies[item] = count
        

    return frequencies

