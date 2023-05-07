import curses
from curses import wrapper 
# initialize curses module
# take over terminal
# allows to run commands
# restore terminal to previous state once done


def start_screen(stdscr):
	# access stdscr method in order to be able to write to the screen
	stdscr.clear() # clears screen
	stdscr.addstr('Welcome to the Speed Typing Test!') # add text to screen
	stdscr.addstr('\nPress any key to begin') # add text to screen
	stdscr.refresh() # refresh screen	
	stdscr.getkey() # wait for user to press something

def display_text(stdscr, target, current, wpm=0):
	# display text in separate func

	stdscr.addstr(target) # add text to screen

	# element of current_text and it's index
	for i, char in enumerate(current):
			stdscr.addstr(0, i, char, curses.color_pair(2)) # overlay on top of target_text


def wpm_test(stdscr):
	target_text = 'hello world, this is some test text for this app!'
	current_text = []

	# ea key user types, overlay in a dif color on top of the original text
	while True:
		stdscr.clear() 
		display_text(stdscr, target_text, current_text)

		# refresh screen at every stroke to prevent target_text from being displayed over and over underneath ea other
		stdscr.refresh() # refresh screen	

		key = stdscr.getkey()
		
		# exit when escape key is hit
		# esc key ASCII code is 27
		if ord(key) == 27:
			break

		# backspace: pop off last element of current text
		# backspace key on different OS represented by different key codes
		if key in ("KEY_BACKSPACE", '\b', '\x7f'):
			if len(current_text) > 0:
				current_text.pop() # remove last element from list
		else:
			current_text.append(key) # fetch every key stroke


def main(stdscr): # define main func, pass in var
	# std = standard output (terminal) 
	# scr = layers the terminal, second screen (virtual terminal?)

	# color pair: foreground and background coloring when printing out text in terminal
	# above: foreground color red, background color white represented by id #1
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

	'''
	stdscr.clear() # clears screen
	# stdscr.addstr('hello world') # add text to screen
	# stdscr.addstr('hello word', curses.color_pair(1)) # add text to screen
	# one line down, at 0 character to the left (1,0)
	stdscr.addstr(1,6, 'hello world', curses.color_pair(1)) # add text to screen
	stdscr.refresh() # refresh screen
	key = stdscr.getkey() # wait for user to type
	print(key)
	'''

	start_screen(stdscr) 
	wpm_test(stdscr)

# calls main function at intialization of the things related to curses module
wrapper(main)
