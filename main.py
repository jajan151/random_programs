import random

min_value = int(input("Zadej spodní hranici: "))
max_value = int(input("Zadej horní hranici: "))

hadej = random.randint(min_value, max_value)
nespravna_cisla = []
pocet_pokusu = 1

while True:
	tip = int(input("Tipni číslo: "))
	if tip in nespravna_cisla:
		pocet_pokusu += 1
		print("Zadal jsi už jednou zadané číslo!")
	else:
		if tip == hadej:
			print(f"Uhádl jsi na {pocet_pokusu}. pokus.")
			break

		elif tip > hadej:
			nespravna_cisla.append(tip)
			print("Hádané číslo je menší.")
			pocet_pokusu += 1

		elif tip < hadej:
			nespravna_cisla.append(tip)
			print("Hádané číslo je větší.")
			pocet_pokusu += 1

		print(f"Tebou zadaná čísla: {nespravna_cisla}")
