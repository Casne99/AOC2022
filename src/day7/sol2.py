class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name


class Directory:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.entryList = set()

    def get_name(self):
        return self.name

    def addEntry(self, entry):
        if entry not in self.entryList:
            self.entryList.add(entry)

    def __iter__(self):
        for attr in self.entryList:
            yield attr

    def get_size(self):
        return sum(entry.get_size() for entry in self.entryList)


def isCommand(string):
    return string.startswith("$")


def whatCommand(string):
    return string.split()[0]


def isDirectory(string):
    return string.startswith("dir")


def directoryName(string):
    return string.split()[1]


input = open("src/day7/input.txt").readlines()
startDirectory = Directory('/', None)
currentDirectory = startDirectory
directories = set()
directories.add(startDirectory)

for line in input:
    if isCommand(line):
        command = whatCommand(line[1:])
        if command == "cd":
            target = line.split()[2]
            if target == "/":
                currentDirectory = startDirectory
            elif target == "..":
                currentDirectory = currentDirectory.parent
            else:
                newDir = Directory(target, currentDirectory)
                directories.add(newDir)
                currentDirectory.addEntry(newDir)
                currentDirectory = newDir
    else:
        if line.startswith("dir"):
            newDir = Directory(line.split()[1], currentDirectory)
            currentDirectory.addEntry(newDir)
        else:
            params = line.split()
            currentDirectory.addEntry(File(params[1], int(params[0])))


available = 70000000
used = [dir.get_size() for dir in directories if dir.get_name() == "/"][0]
unused = available - used
required = 30000000
ans = min(dir.get_size()
          for dir in directories if unused + dir.get_size() >= required)
print(ans)
