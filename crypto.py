#! /usr/bin/python3
import operator
import sys
filename = sys.argv[1:][0]
print(filename)
fp = open(filename)
lines = []
line = fp.readline()
while line :
	words = line.split(' ')
	rline = "".join(words)
	lines.append(rline)
	line = fp.readline()
text = "".join(lines)
text = "".join(text.split('\n'))



def IC(r):
	n = len(text)
	icval = []	
	for k in range(r):
		alphabet = {'Α' : 0, 'Β': 0, 'Γ': 0,'Δ' :0,'Ε':0,'Ζ':0,'Η':0,'Θ':0,'Ι':0,'Κ':0,'Λ':0,'Μ':0,'Ν':0,'Ξ':0,'Ο':0,'Π':0,'Ρ':0,'Σ':0,'Τ':0,'Υ':0,'Φ':0,'Χ':0,'Ψ':0,'Ζ':0}
		l = k 
		i = 0
		while(l < n):
			i += 1
			alphabet[text[l]] += 1
			l += r
		res = 0
		#print(alphabet.values())
		for x in alphabet.values():
			res += x * (x - 1) 
		res /= (i * (i-1))
		icval.append(res)
	return icval

periods = []
for r in range(24):
	if(r == 0): continue
	icvals = IC(r+1)
	flag = False
	for x in icvals:
		if x < 0.065: flag = True
	if(flag): continue
	periods.append(r+1)	

#Only period = 6 was valid
print("First method: ", periods)

#second way
def givep():
	alphabet = {'Α' : 0, 'Β': 0, 'Γ': 0,'Δ' :0,'Ε':0,'Ζ':0,'Η':0,'Θ':0,'Ι':0,'Κ':0,'Λ':0,'Μ':0,'Ν':0,'Ξ':0,'Ο':0,'Π':0,'Ρ':0,'Σ':0,'Τ':0,'Υ':0,'Φ':0,'Χ':0,'Ψ':0,'Ζ':0}
	for x in text:
		alphabet[x] += 1
	res = 0
	for x in alphabet.values():
		res += x * (x - 1) 
	n = len(text)	
	res /= (n * (n-1))
	return abs(((0.065 - 0.0435) / (res - 0.0435)))

print("Second method: ", givep()) # returns 5.7 near 6.

# So period is 6

def findkey(r):
	n = len(text)
	firstmax = []
	secondmax = []	
	for k in range(r):
		alphabet = {'Α' : 0, 'Β': 0, 'Γ': 0,'Δ' :0,'Ε':0,'Ζ':0,'Η':0,'Θ':0,'Ι':0,'Κ':0,'Λ':0,'Μ':0,'Ν':0,'Ξ':0,'Ο':0,'Π':0,'Ρ':0,'Σ':0,'Τ':0,'Υ':0,'Φ':0,'Χ':0,'Ψ':0}
		l = k 
		while(l < n):
			alphabet[text[l]] += 1
			l += r
		
		firstmax.append(max(alphabet.items(), key=operator.itemgetter(1))[0])
		alphabet[firstmax[len(firstmax) -1]] = 0
		secondmax.append(max(alphabet.items(), key=operator.itemgetter(1))[0])
		
	print(firstmax)
	print(secondmax)
findkey(6)

# So key is ΕΛΥΤΗΣ
key = "ΕΛΥΤΗΣ"

print("Key = ", key)

al = []
for i in range(25):
	if(i == 17): continue
	al.append(chr(ord('Α') + i))
i = 0
dic = {}
dic2 = []
for x in al:
	dic[x] = i
	i += 1
	dic2.append(x)

def rotate(x, y):
	if(dic[x] - dic[y] < 0): return dic2[(dic[x] - dic[y]) + 23]
	return dic2[(dic[x] - dic[y]) % 23]

def decrypt(key):
	r = len(key)
	dec = []
	for i in range(len(text)):
		real = rotate(text[i], key[i % r])
		dec.append(real)
	print("".join(dec))

decrypt("ΕΛΥΤΗΣ")


	

	

