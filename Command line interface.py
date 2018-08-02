import shutil as util


def helper():
    helper_dict = {}
    helper_dict["cp"] = "source  [destinations...] \n\n"
    helper_dict["mv"] = "source  [destinations...] \n\n"
    helper_dict["diff"] = "source  [destinations...] \n\n"
    helper_dict["ls"] = "source  [destinations...] \n\n"
    helper_dict["cd"] = "source  [destinations...] \n\n"
    for command in helper_dict:
        print("Command  " + command + " ---> " + command + "  " + helper_dict[command])


def copy(*args):
    source = args[0][1]
    destinations = args[0][2:]
    for place in range(0, len(destinations)):               # multiple destinations
        util.copy(source, destinations[place])
    return True


def move(*args):
    source = args[0][1]
    destinations = args[0][2:]
    for place in range(0, len(destinations)):
        if place == len(destinations):                      # util.move just for the last one destination
            util.move(source, destinations[place])
        else:
            util.copy(source, destinations[place])
    return True


def main():
    print(welcome)
    choice = input("Launch command: \n\n")
    if choice.split()[0] == "cp":
        params = choice[1:]
        copy(params.split())
    elif choice.split()[0] == "mv":
        params = choice[1:]
        move(params.split())
    elif choice.split()[0] == "diff":
        return True
    elif choice.split()[0] == "ls":
        return True
    elif choice.split()[0] == "cd":
        return True
    else:
        helper()


welcome = ("Unix-like Python Script Implementation \n"
           "Type 'help' for commands usage"
           "You can launch the following commands: \n\n"
           "- cp\n"
           "- mv\n"
           "- diff\n"
           "- ls\n"
           "- cd\n\n")


main()

# C:/Users/Giacomo/PycharmProjects/Unix-Commands/ciao.txt C:/Users/Giacomo/PycharmProjects/Unix-Commands/dest/bella.txt

