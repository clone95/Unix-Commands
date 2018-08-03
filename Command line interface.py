import shutil as util


def clean_words(rows_list):
    clean_rows = []
    for index in range(0, len(rows_list)):
        if index != (len(rows_list)-1):
            clean_rows.append(rows_list[index][:-1])
        else:
            clean_rows.append(rows_list[index])
    return clean_rows


def helper():
    helper_dict = {}
    helper_dict["cp"] = "source  [destinations...] \n\n"
    helper_dict["mv"] = "source  [destinations...] \n\n"
    helper_dict["diff"] = "source  [destinations...] \n\n"
    helper_dict["ls"] = "source  [destinations...] \n\n"
    helper_dict["cd"] = "source  [destinations...] \n\n"
    for command in helper_dict:
        print("Command  " + command + " ---> " + command + "  " + helper_dict[command])


def diff (file1, file2):
    file1 = open(file1, "r")
    file2 = open(file2, "r")
    words_1 = clean_words(file1.readlines())
    words_2 = clean_words(file2.readlines())
    differences = []
    all_words_1 = " ".join(words_1).split()
    all_words_2 = " ".join(words_2).split()
    for el in all_words_2:
        if (el in all_words_1) and (el not in differences):
            differences.append(el)
    return differences


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
    params = choice.split()[1:]
    if choice.split()[0] == "cp":
        copy(params.split())
    elif choice.split()[0] == "mv":
        move(params.split())
    elif choice.split()[0] == "diff":
        print(diff(params[0], params[1]))
    elif choice.split()[0] == "ls":
        return True
    elif choice.split()[0] == "cd":
        return True
    else:
        helper()


welcome = ("\nUnix-like Python Script Implementation \n"
           "Type 'help' for commands usage\n"
           "You can launch the following commands: \n\n"
           "- cp\n"
           "- mv\n"
           "- diff\n"
           "- ls\n"
           "- cd\n\n")


main()


# C:/Users/Giacomo/PycharmProjects/Unix-Commands/file1.txt C:/Users/Giacomo/PycharmProjects/Unix-Commands/file2.txt
