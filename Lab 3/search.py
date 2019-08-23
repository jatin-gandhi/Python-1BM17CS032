def search(li,key):
	if key in li:
		return True
	else:
		return False

lis = list(map(int,input("Enter the elements in increasing order").split()))
num = int(input("Enter the number to search"))
print(search(lis,num))
