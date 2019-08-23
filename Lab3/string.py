
sentence = input("Enter the sentence")

lis =[]
for ch in sentence:
	lis.append(ch)

for i in range(len(lis)-1,0,-1):
	print(lis[i],end="")

