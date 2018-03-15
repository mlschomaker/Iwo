import sys

def main():
	file = sys.argv[1]
	user_word = str(sys.argv[2])
	cnt = 0
	with open(file) as inputfile:
		for line in inputfile:
			words = []
			words = line.split()
			for word in words:
				if word == user_word:
					cnt=cnt+1

	inputfile.close()
	print("The word '{0}' occurs '{1}' times in document '{2}'".format(user_word,cnt,file))
if __name__ == '__main__':
	main()