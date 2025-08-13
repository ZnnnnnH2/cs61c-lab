def get_airspeed_velocity_of(unladen_swallow):
	if unladen_swallow.type == "african":
		return  # redacted
	elif unladen_swallow.type == "european":
		return  # redacted


# pretend there's code here...

def fizzbuzz(num):
	flag1 = False
	flag2 = False

	if num % 3 == 0:  # edit this line
		flag1 = True# print(f"{num}: fizz")
	if num % 5 == 0:  # edit this line
		flag2 = True# print(f"{num}: buzz")

	if flag1 and flag2:
		print(f"{num}: fizzbuzz")
	elif flag1:
		print(f"{num}: fizz")
	elif flag2:
		print(f"{num}: buzz")

for i in range(1, 20):
	fizzbuzz(i)

# pretend there's code here...
