import math
with open("text1.txt") as file:
	data = file.readline()
	word = data.split()


with open("text2.txt") as file:
	data = file.readline()
	word2 = data.split()


for x,y in zip(word,word2):
	print(x[:(math.ceil(len(x)/2))] + y[:(math.ceil(len(y)/2))],end = " ")


if len(word) >len(word2):
	for i in range(len(word2)-1,len(word),1):
		x = word[i]
		print(x[:(math.ceil(len(x)/2))],end =" ")

else:
	for i in range(len(word)-1,len(word2),1):
		x = word2[i]
		print(x[:(math.ceil(len(x)/2))],end =" ")
	
		
		



