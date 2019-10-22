#Kathryn Marini 10/4/19
#This function runs a game of scrambler, where the user is given words to unscramble until they admit they are not not having fun. 
def jumble():
	import random
	wordList =['macaroni','opulent','ostentatious','bramble','nocturnal','counterfeit','momentous','yay']
	print('Hi there pal, are you looking for some fun and you want to retire from your good game of sudoku that you have spent hours at?' 'Well you came to the right place. This is the Scrambler game. Create the right words until you are having fun!')
	havingFun= input('Are you having fun yet?')
#While the user says no to 'having fun?' they will have to unscramble new words from the list. 
		while havingFun=='no':
		word=random.choice(wordList)
		answer=word
		jumble=''
		while word:
			order=random.randrange(len(word))
			jumble+=word[order]
			word=word[:order] + word[(order+1):]
		print('Word:', jumble)
		guess = input('Answer?')
#The user guesses what the correct word is until they get the right answer. 
		while guess != answer:
			print('Nope,try again. ')
			guess = input('New guess?')
		if guess == answer:
			print('Noice.')
			havingFun=input('Having fun yet?')
	print('Nice work, now, be free.')

jumble()
