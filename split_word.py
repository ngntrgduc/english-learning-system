raw = """
VICIOUS | English meaning - Cambridge Dictionary
INSIDIOUS | English meaning - Cambridge Dictionary
CONCISE | English meaning - Cambridge Dictionary
PRAGMATIC | English meaning - Cambridge Dictionary
INQUISITIVE | English meaning - Cambridge Dictionary
GENUINE | English meaning - Cambridge Dictionary
DELEGATE | English meaning - Cambridge Dictionary
CAVEAT | English meaning - Cambridge Dictionary
ARCANE | English meaning - Cambridge Dictionary
INTIMATE | English meaning - Cambridge Dictionary
EXPOSE | English meaning - Cambridge Dictionary
DERIVE | English meaning - Cambridge Dictionary
ACCOUNT | English meaning - Cambridge Dictionary
COLLABORATE | English meaning - Cambridge Dictionary
ELABORATE | English meaning - Cambridge Dictionary
FORECAST | English meaning - Cambridge Dictionary
INSIGHT | English meaning - Cambridge Dictionary
FASCINATION | English meaning - Cambridge Dictionary
DEXTERITY | English meaning - Cambridge Dictionary
DELICATE | English meaning - Cambridge Dictionary
BIAS | English meaning - Cambridge Dictionary
HIERARCHY | English meaning - Cambridge Dictionary
SCRATCH | English meaning - Cambridge Dictionary
FIXED | English meaning - Cambridge Dictionary
CANNOT | English meaning - Cambridge Dictionary
FUR | English meaning - Cambridge Dictionary
DICTATE | English meaning - Cambridge Dictionary
MITTEN | English meaning - Cambridge Dictionary
DRIVEWAY | English meaning - Cambridge Dictionary
CHAOS | English meaning - Cambridge Dictionary
DISTINCT | English meaning - Cambridge Dictionary
GUARANTEE | English meaning - Cambridge Dictionary
ALTER | English meaning - Cambridge Dictionary
VAGUE | English meaning - Cambridge Dictionary
"""

def split_word(words_list, delimiter=' '):
    return [word.split(delimiter)[0].lower() for word in words_list]

words_list = [word for word in raw.split("\n") if len(word) > 0]
words = split_word(words_list)
print(words)

# print(raw.split('\n'))