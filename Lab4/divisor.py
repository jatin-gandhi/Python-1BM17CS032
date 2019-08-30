def divisor(num):
	return [x for x in range(1,num+1,1) if num%x ==0 ]


number = int(input("Enter the number\n"))
print(divisor(number))
