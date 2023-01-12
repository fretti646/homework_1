import os

while True:
    command = input()
    command = command.split() 
    
    if command[0] == "ls" and len(command) == 1:
        print(os.listdir())
    elif command[0] == "ls" and len(command) > 1:
        print(os.listdir(command[1]))
    elif command[0] == "cd" and len(command) > 1:
        os.chdir(command[1])
    elif command[0] == "cd" and len(command) == 1:
        print("Введите путь")
    elif command[0] == "pwd":
        print(os.getcwd())
    elif command[0] == "mkdir" and len(command) > 1:
         os.mkdir(command[1])
    elif command[0] == "mkdir" and len(command) == 1:
        print("Введите название создаваемой директории")
    elif command[0] == "touch" and len(command) > 1:
        open(command[1], "w")
    elif command[0] == "touch" and len(command) == 1:
        print("Введите имя создаваемого файла")
    elif command[0] == "rm" and len(command) > 1:
        if os.path.isfile(command[1]):
            os.remove(command[1])
        elif os.path.isdir(command[1]):
            for root, dirs, files in os.walk(command[1], topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
            for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(command[1])
    elif command[0] == "rm" and len(command) == 1:
        print("Введите имя файла или директории, которую требуется удалить")
    else:
        print("Введена некорректная команда")
        

