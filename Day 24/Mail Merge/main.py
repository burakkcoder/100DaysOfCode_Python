with open("../Mail Merge/Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open("../Mail Merge/Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()
    for x in name_list:
        strip_name = x.strip()
        new_letter = letter.replace("[name]", strip_name)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", "w") as final_letter:
            final_letter.write(new_letter)