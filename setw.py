import i3ipc
import sys

targetwidth = float(sys.argv[1])

i3 = i3ipc.Connection()
t = i3.get_tree()

# get currently focused window
current = t.find_focused()
currentsize = current.percent * 100;

diff = targetwidth - currentsize
if diff == 0:
	exit()

command = "shrink"
if diff > 0:
	command = "grow"

command = "resize {} width 1 px or {} ppt".format(command, round(abs(diff)))
print(command)
current.command(command)