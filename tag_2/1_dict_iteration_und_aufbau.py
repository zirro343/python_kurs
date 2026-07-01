"""
Ein Dict iterativ aufbauen
"""

# Word-Counter (Frequenzanalyse) wc
sentence = "the quick brown fox jumps over the lazy dog dog fox"
wc = {}
for word in sentence.split():
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1

print(wc)
######################################
wc = {}

for word in sentence.split():
    # get ergbit 0 wenn nicht enthalten
    wc[word] = wc.get(word, 0) + 1

print(wc)


## Iteration über Dict
### über ein Dict iteriere, gibt die KEYS
for key in wc:
    print("=>", key, wc[key])

print(list(wc.items()))  # [('the', 2), ('quick', 1), ('brown', 1),]
for key, value in wc.items():
    print("=>", key, wc[key])
