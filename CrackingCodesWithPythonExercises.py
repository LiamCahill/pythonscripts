#print('Hello World!')

message = 'Three can keep a secret, if two of them are dead.'
translated = ''


i = len(message) - 1
while i >= 0:
	translated = translated + message[i]
	i = i - 1

print(translated)

#print(len("Hello")+len('Hello'))

j = 0
spam = "Hello"
while j < 5: 
	spam = spam + spam[j]
	j = j + 1
print(spam)