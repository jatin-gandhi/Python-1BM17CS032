def even(li):
	return [x for x in li if x%2==0]

lis = list(map(int,input("Enter the elements of the list").split()))
new_list = even(lis)
print(new_list)
