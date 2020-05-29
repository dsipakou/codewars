def smallestSubstringContaining(bigString, smallString):
	count = 0
	d = {}
	for i in smallString:
		if i not in d:
			count += 1
			d[i] = 1
		else:
			d[i] += 1
	left = right = current = 0
	output = ''
	while right < len(bigString) and left < len(bigString):
		if current == count or right >= len(bigString):
			cur_ch = bigString[left]
			if cur_ch in d:
				d[cur_ch] += 1
				if d[cur_ch] == 1:
					current -= 1
				if current == count and (right - left < len(output)):
					output = bigString[left + 1: right + 1]
			left += 1
		else:
			cur_ch = bigString[right]
			if cur_ch in d:
				d[cur_ch] -= 1
				if d[cur_ch] == 0:
					current += 1
				if current == count:
					print(output)
					if len(output) == 0 or (right + 1 - left < len(output)):
						output = bigString[left: right + 1]
			right += 1
	return output
		
