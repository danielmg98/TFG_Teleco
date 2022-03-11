import sys, os

if os.path.isfile('./lexicon_new.txt'):
	os.remove('./lexicon_new.txt')

original = open('lexicon2.txt','rb')
nuevo = open('lexicon_new.txt','wb')

while 1:
	
	char = original.read(1)
	if not char:
		break
	if char == b'\t':
		nuevo.write(char)
		char2 = original.read(1)
		if char2 == b'.':
			nuevo.write(char2)
	elif char == b'.':
		pass
	elif char == b'+':
		pass
	else:
		nuevo.write(char)

original.close()
nuevo.close()
