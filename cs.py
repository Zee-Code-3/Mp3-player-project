import curses
import pygame
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(False)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CY_BL = curses.color_pair(3)
    RD_BL = curses.color_pair(2)
    GR_BL = curses.color_pair(1)

    height, width = stdscr.getmaxyx()
    msg = "Press SPACE to toggle music. Press 'q' to quit"
    msg3 = "Song is playing..."
    msg4 = "Song is paused..."
    msg5 = "Song is not playing..."
    msg6 = "Welcome to the MP3 Player!"
    msg7 = ""
    msg8 = ""
    msg9 = ""
    center = width // 2

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/amy/Coding-with-C++/Python-mp3-project/free-bird-solo.mp3")

    is_playing = False
    is_paused = False

    while True:
        height, width = stdscr.getmaxyx()
        center_x = width // 2

        # Set window size message based on current size
        if height == 10 and width == 46:
            msg2 = f"Window size: {height} rows x {width} cols (minimum)"
        elif height == 72 and width == 262:
            msg2 = f"Window size: {height} rows x {width} cols (maximum)"
        else:
            msg2 = f"Window size: {height} rows x {width} cols"
        if not height == 10 and width == 46:
            msg8 = "minimum width has been reached";
        elif height == 10 and not width == 46:
            msg8 = "minimum height has been reached";
        else:
            msg8 = "";
        if not height == 72 and width == 262:
            msg9 = "maximum width has been reached";
        elif height == 72 and not width == 262:
            msg9 = "maximum height has been reached";
        else:
            msg9 = "";

        # List of messages to display, in order
        lines = [
            (msg7, CY_BL),  # Blank line, blue (or use RD_BL or GR_BL)
            (msg6, RD_BL),  # Title, blue
            (msg7, CY_BL),  # Blank line, blue (or use RD_BL or GR_BL)
            (msg, RD_BL),
            (msg7, CY_BL),
            (msg3 if is_playing else msg4 if is_paused else msg5, GR_BL if is_playing else RD_BL),
            (msg7, CY_BL),
            (msg2, RD_BL),
            (msg8, RD_BL),
            (msg9, RD_BL)  # Blank line, blue
        ]

        stdscr.clear()
        # Calculate starting y so all lines are vertically centered
        start_y = (height // 2) - (len(lines) // 2)
        for i, (text, color) in enumerate(lines):
            stdscr.addstr(start_y + i, center_x - len(text)//2, text, color)

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord('q'):
            pygame.mixer.music.stop()
            break
        elif key == ord(' '):
            if not is_playing and not is_paused:
                pygame.mixer.music.play(-1)
                is_playing = True
                is_paused = False
            elif is_playing and not is_paused:
                pygame.mixer.music.pause()
                is_paused = True
                is_playing = False
            elif not is_playing and is_paused:
                pygame.mixer.music.unpause()
                is_paused = False
                is_playing = True

        time.sleep(0.05)

curses.wrapper(main)

#minimum window size is 7 row X 46 cols