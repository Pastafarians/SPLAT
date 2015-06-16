#################################################################
# File Name: nltk_main.py										#
# Date Created: 06-16-2015										#
# Date Revised: 06-16-2015										#
# Author: Benjamin S. Meyers									#
# Email: bsm9339@rit.edu										#
# 	Advisor: Emily Prud'hommeaux								#
# 	Email: emilypx@rit.edu										#
# 	Advisor: Cissi Ovesdotter-Alm								#
# 	Email: coagla@rit.edu										#
#################################################################
from nltk_functions import *
from nltk_tests import run_tests

##### MAIN ######################################################
def main():
	print(startup_info)
	while(True):
		user_command = raw_input('Please provide a command: ')
		command = word_tokenize(user_command)
		#print(command)
		if command[0] == 't' and len(command) == 2:
			get_tokens(command[1])
		elif command[0] == 'f' and len(command) == 3:
			get_freqs(command[1], int(command[2]))
		elif command[0] == 'h' and len(command) == 1:
			display_command_list()
		elif command[0] == '!' and len(command) == 1:
			run_tests()
		elif command[0] == '~' and len(command) == 1:
			print(more_info)
		elif len(command) == 1 and command[0] == '42':
			print(douglas)
		elif command[0] == 'q' and len(command) == 1:
			print('\n' + random.choice(exit_messages) + '\n')
			break
		else:
			print('Invalid Command.\nFor Help, type \'h\'.')

if __name__ == "__main__":
    main()
