import argparse
import time

def pattern_match(text, pattern):
	# TODO
	# hint: Use dynamic programming to achieve O(T*P)
	tlen = len(text)
	plen = len(pattern)
	textList = [0] * (tlen+1)
	patternList = [0] * (plen+1)
	count_star = 0
	if pattern == '':
		if text == '':
			return True
		else:
			return False
	if text == '':
		if plen % 2 != 0:
			return False
		else:
			for i in range(2, plen, 2):
				if pattern[i-1] == '*':
					count_star += 1
					if count_star == plen // 2:
						return True
				else:
					return False
	for i in range(1,tlen+1):
		textList[i] = text[i-1]
	for j in range(1,plen+1):
		patternList[j] = pattern[j-1]

	match = {}
	for i in range(tlen+1):
		match[i,0] = False
	for j in range(1,plen+1):
		match[(0,j)] = False
	for k in range(1,plen+1):
		if k == 2 and patternList[2] == '*':
			while patternList[k] == '*':
				match[(0,k)] = True
				k = k + 2
				if k > plen:
					break
	match[(0,0)] = True
	for i in range(1,tlen+1):
		for j in range(1,plen+1):
			if (textList[i] == patternList[j]) or (patternList[j] == '.'):
				match[(i,j)] = match[(i-1, j-1)]
			elif patternList[j] == '*':
				if match[(i,j-2)] == True:                                                      # (b) and (b,c,*) is the same
					match[(i,j)] = True
				elif (patternList[j-1] == textList[i]) or (patternList[j-1] =='.'):             # (b,c,c) and (b,c,*) is the same
					match[(i,j)] = match[(i-1,j)]
				else:
					match[(i,j)] = False
			else:
				match[(i,j)] = False
	return match[(tlen, plen)]
	#return False

def main(input_path, output_path):
	# DO NOT MODIFY CODES HERE
	# DO NOT MODIFY CODES HERE
	# DO NOT MODIFY CODES HERE
	# It's important and repeat three times
	output = open(output_path, 'w')
	with open(input_path) as f:
		for line in f.readlines():
			line = line.strip().split()
			text, pattern = line[0], line[1]
			if pattern_match(text, pattern):
				print('1', file=output)
			else:
				print('0', file=output)
		output.close()

if __name__ == '__main__':
	# DO NOT MODIFY CODES HERE
	# DO NOT MODIFY CODES HERE
	# DO NOT MODIFY CODES HERE
	# It's important and repeat three times
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', default='./input')
	parser.add_argument('--output', default='./output')
	args = parser.parse_args()

	ts = time.time()
	main(args.input, args.output)
	te = time.time()
	print('Run Time: {:.5f}s'.format(te-ts))

