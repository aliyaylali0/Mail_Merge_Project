with open("./Input/Names/invited_names.txt", "r") as data:
    name = data.read()
    new_name = name.replace('\n', ',').split(",")
    namelist = list(new_name)

    for name in namelist:
        with open("./Input/Letters/starting_letter.txt") as data2:
            letter = data2.read()
            name_letter = letter.replace("[name]", name)
            print(name_letter)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as send:
                send.write(name_letter)
