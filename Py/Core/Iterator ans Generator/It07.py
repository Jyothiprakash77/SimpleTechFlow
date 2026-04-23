# 7. Implement a generator that yields vowels from a string.
def vowels(string):
    for i in string:
        if i in "AEIOUaeiou":
            yield i
it=vowels("Lincon")
for i in vowels("LEO Das"):
    print(i,end=" ")
print()
for i in it:
    print(i,end=" ")