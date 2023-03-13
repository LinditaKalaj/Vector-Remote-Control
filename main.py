import anki_vector
from anki_vector import util
from anki_vector.exceptions import VectorConnectionException, VectorNotFoundException

import gui

if __name__ == "__main__":
    args = util.parse_command_args()
    try:
        with anki_vector.AsyncRobot(args.serial) as robot:
            root = gui.Window(robot)
            root.mainloop()
    except VectorNotFoundException as v:
        print("A connection error occurred: %s" % v)
    except VectorConnectionException as e:
        print("A connection error occurred: %s" % e)


