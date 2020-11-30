s = input()
if s == s[::-1]:
	print(1)
else :
	count =0
	sub_s =""
	
	for i in range(len(s)):
		sub_s += s[i]
		if sub_s == sub_s[::-1] and len(sub_s) >= 2:
			count+= 1
			sub_s = ""

	if len(sub_s) == 1 :
		print(count)
	else :
		print(count+ 1)
