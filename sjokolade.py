"""
Gå gjennom tallene 1-100

Hvis tallet kan deles på 3, print Sjoko
Hvis tallet kan deles på 5, print Lade
Hvis tallet kan deles på 3 og 5, print SjokoLade
Ellers print tallet (i)
"""

for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("SjokoLade")
        else:
            print("Sjoko")
    elif i % 5 == 0:
        if i % 3 == 0:
            print("SjokoLade")
        else:
            print("Lade")
    else:
        print(i)
