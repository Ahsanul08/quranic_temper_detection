# your code goes here

s1 = "DIXON"
s2 = "DICKSONX"
m=0
t=0
list_ex = []
dist = max(len(s1),len(s2))/2 - 1

for i in range(len(s1)):  									#These 2 nested loops are to
	for j in range(max(0,i-dist),min(i+dist,len(s2)-1)+1):	#calculate m
		if s1[i]==s2[j]:
			m+=1
			list_ex.append(j)
			break

list_ne = list_ex[:]
list_ne.sort()

for i in range(len(list_ne)):   #comparing these two lists calculates t
	if list_ne[i]!=list_ex[i]:
		t+=1

t=t/2
dj=0
if m!=0:
	dj = (0.33333333333333) * ( 1.0 * ( (1.0*m) 	/ (1..0*len(s1) ) ) + \
								1.0 * ( (1.0*m) 	/ (1.0*len(s2) ) ) + \
								1.0 * ( (1.0*(m-t)) / (1.0*m) ) )
#print dj
#Jaro Similarity Code Ends Here4

p=0.1
bt=0.7
l=min(len(s1),len(s2))
for i in range(l):      #calculating l
	if s1[i]!=s2[i]:
		l=i
		break

dw = dj
if dj >= bt:
	dw = dj + l*p*(1-dj)   #Calculating winkler distance

print "dw -> " , dw




