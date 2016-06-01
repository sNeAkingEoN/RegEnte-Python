#RegEnte: Ein Programm, das RegEx überprüft und dabei Entengeräusche von sich gibt.

import re

print("Hallo. Hier ist deine RegEnte. Naknak.")
# rrrrichtig cool wäre ein Anzeigen-Delay, um es ein bisschen lebendiger wirken zu lassen.

print("Bitte gib einen regulären Ausdruck ein, naknak.")
prompt1 = "RegEx "
regex = input(prompt1)
#String-Interpolierungs-ersatz: du hast... eingegeben.
regex_helper = regex + "$"
# regex = regex
print("Vielen Dank, naknaknak. Jetzt gib bitte den Text, der gematcht werden soll, ein, naknaknak.")
prompt2 = "Zeichenkette "
string = input(prompt2)
#String-Interpolierungs-ersatz: du hast... eingegeben.
print("QuakQuakQuakQuak.")

main_pattern = re.compile(regex)
help_pattern = re.compile(regex_helper)
if main_pattern.match(string) and help_pattern.match(string):
  print("Dein String matcht deine RegEx. Naknaknak.")
elif main_pattern.search(string):
  print("Deine RegEx findet sich im String wieder, aber da ist noch mehr.... Naknak.")
else:
  print("Irgendwas stimmt noch nicht. Quak.") # und dann entweder nochmal versuchen, oder neu starten...



