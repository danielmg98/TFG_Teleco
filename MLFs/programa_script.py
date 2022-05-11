import sys, os

script = open('codetr.scp','w')

i = 1

while i < 373:

	script.write('./mavir02_'+str(i)+'.wav\t./mavir02_'+str(i)+'.mfc\n')
	i = i+1


