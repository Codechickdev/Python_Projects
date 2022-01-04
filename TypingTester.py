import time
import curses
from curses import wrapper

def start_screen(stdscr): # Logic function to start the screen
    stdscr.clear() #clears the screen
    stdscr.addstr("Welcome to Typing Test")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh() #refresh the screen

    stdscr.getkey() #get the key that user typed


def display_text(stdscr, target, current, wpm=0): # Logic function to display the overlaying text and see user typed correct
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):

        correct_text = target[i]
        color = curses.color_pair(1)
        if char != correct_text:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


def wpm_test(stdscr): # Logic function to add the text that user typed
    target_text = "Hello World, This is some Typing test"
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr): # Main function
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed, Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)