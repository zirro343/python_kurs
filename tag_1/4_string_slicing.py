"""
Die Slice-Notation (für alle sequentiellen Datentypen)
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String

"""
string = "Test-String"
print(string[0:4])  # [0:10]

"""
# Übung
# Schneide jeweils alle A aus den Strings
AAAAB => AAAA
BBAAABBB => AAA
AAAABBBB => AAAA
ABBBBB => A
"""
string = "AAAAB"
print("AAAAB => AAAA: ", string[:-1])

string = "BBAAABBB"
print("BBAAABBB => AAA: ", string[2:5])

string = "AAAABBBB"
print("AAAABBBB => AAAA: ", string[:-4])

string = "BBAABBBB"
print("BBAABBBB => AA: ", string[2:-4])

string = "ABBBBB"
print("ABBBBB => A: ", string[:1])