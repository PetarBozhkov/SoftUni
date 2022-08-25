#10. Company Users

#Write a program that keeps the information about companies and their employees.

#You will be receiving company names and an employees' id until you receive the command "End" command. Add each employee to the given company. 
#Keep in mind that a company cannot have two employees with the same id.

#Print the company name and each employee's id in the following format:

#"{company_name}

#-- {id1}

#-- {id2}

#…

#-- {idN}"

force_side_dict = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        splitted_command = command.split(" | ")
        force_side, force_user = splitted_command
        present = False
        for value in force_side_dict.values():
            if force_user in value:
                present = True
                break
        if not present:
            if force_side not in force_side_dict.keys():  # not in force_side_dict
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)
    else:  # elif "->" in command:
        splitted_command = command.split(" -> ")
        force_user, force_side = splitted_command
        for key, value in force_side_dict.items():
            if force_user in value:
                force_side_dict[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = [force_user]
        else:
            force_side_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side in force_side_dict.keys():
    if len(force_side_dict[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(force_side_dict[force_side])}")
        [print(f"! {user}") for user in force_side_dict[force_side]]
