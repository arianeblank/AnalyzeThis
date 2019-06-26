print('Hello Worm')


##bike shop thing
Broken_Bikes = 2
while Broken_Bikes >0 :
	User_Input = input('Can we fix the next bike?')
	if User_Input.lower() == 'Yes'.lower():
		Broken_Bikes = Broken_Bikes -1
		print('Fixed that bike')
	else:
		print("Didn't fix the bike")
	print('Numeber of Bikes is now')
	print(Broken_Bikes)
	if Broken_Bikes ==0:
		print("all done")
		break

##ask the student if they have done anything 
print('I am your new academic advisor/PI')

Counter = 0
while True: 
	User_Input = input('Anything new in the last hour?')
	GelOrMassSpec = False
	if 'gel' in User_Input.lower():
		print("Let's look at that gel")
		GelOrMassSpec = True
	if 'mass spec' in User_Input.lower():
		print("Let's look at the spectra")
		GelOrMassSpec = True
	elif 'enough' in User_Input.lower():
		print("Let's go home")
		break
	if not(GelOrMassSpec):
		print("why haven't you run a gel or mass spec?")
	Counter = Counter + 1
	if Counter > 20:
		print('Enough on my end')
		break

print('See ya')







