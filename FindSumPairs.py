#Given array list, find all the pairs of numbers whose sum equal to given sum
# Time Complext- O(n)
# Space Complexity- O(n) 

import sys
def FindSumPairs(Numbers, requiredSum):
	tmpbuffer=[]
	thePairs={}
	counter=0
	flg=0
	complement=0
	for number in Numbers:
		complement = requiredSum - number
		tmplist=[]
		tmplist.append(number)
		if(number in tmpbuffer):
			tmplist.append(complement)
			thePairs[counter]=tmplist
			flg=1
			counter += 1
		tmpbuffer.append(complement)
		if(flg==1):
			tmpbuffer.remove(complement)
		flg=0
	return thePairs


Numbers=[3,6,2,5,7,4,3] 
requiredSum = 9
print(FindSumPairs(Numbers,requiredSum))
print("Hello there.")
