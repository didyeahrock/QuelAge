#!/usr/bin/python3
age = input("Quel age avez-vous ? ")
age_int=int(age)
if age_int < 18:
	print("Vous avez",age_int,"ans, vous êtes donc mineur")
else:
	print("Vous avez",age_int,"ans, vous êtes donc majeur")

