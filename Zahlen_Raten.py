
import random

print("heyo, ich soll ein Nummer rate spiel ballern.")
print("ich denk mir jetzt eine zahl zwichen 1 und 100 aus rate mal welche zahl")
print("ich hab jetzt git")

number = random.randint(1, 100)
versuche = 0
print("aber zuerst musst du die schwierigkeit auswählen.\n1. Einfach 10 chances.\n2. Mittel 5 chances.\n3. Schwer nur 3 chances")

while True:
    difficulty = input()

    if difficulty == "1":
        print("Ah du baby wählst einfach")
        versuche = 10
        break
    elif difficulty == "2":
        print("Ein Casual wie ich sehe")
        versuche = 5
        break
    elif difficulty == "3":
        print("Was ein macher")
        versuche = 3
        break
    else:
        print("schon nicht so gut 1, 2 oder 3 das wird wohl nicht so schwer sein")

print(f"Du hast also {versuche} Versuche!")
while versuche > 0:
    user = int(input("Dann versuch es mal: "))
    versuche -= 1
    
    if user < number:
        print(f"Ne {user} ist kleiner als meine Zahl.")
    elif user > number:
        print(f"Ne {user} ist größer als meine Zahl")
    else:
        print(f"Yeah BITSCH {user} war wirklich meine zahl und du hattest übrigens noch {versuche} übrig.")
        break
if versuche == 0:
    print("echt schwach")
else:
    print("sei stolz eine random zahl erraten zu haben")
#darf ich so jetzt mal version control updaten
