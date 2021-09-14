#!/usr/bin/python3
# toto
age = input("Quel age avez-vous ? ")
age_int=int(age)
if age_int < 18:
	print("Vous avez",age_int,"ans, vous êtes donc mineur")
else:
	print("Vous avez",age_int,"ans, vous êtes donc majeur")

