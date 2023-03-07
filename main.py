import threading

import anki_vector
from anki_vector import util

import gui

if __name__ == "__main__":
    args = util.parse_command_args()
    with anki_vector.AsyncRobot(args.serial) as robot:
        root = gui.Window(robot)
        root.mainloop()
