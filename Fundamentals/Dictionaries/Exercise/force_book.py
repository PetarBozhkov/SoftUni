#11. *Force Book

#The force users struggle to remember which side is the different force users from because they switch them too often. 
#So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.

#You will receive several input lines in one of the following formats:

#"{force_side} | {force_user}"

#"{force_user} -> {force_side}"

#The "force_user" and "force_side" are strings, containing any character.

#If you receive "force_side | force_user":

#· If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.

#· Only if there is no such force user in any force side -> add the force user to the corresponding side.

#· If there is such force user already -> skip the command and continue to the next operation.

#If you receive a "force_user -> force_side":

#· If there is such force user already -> change their side.

#· If there is no such force user in any force side -> add the force user to the corresponding force side.

#· If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.

#· Then you should print on the console: "{force_user} joins the {force_side} side!".

#You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. 
#For each side, print the force users.

#In case there are no force users on a side, you shouldn't print the side information


users_input = input()
forces = dict()
while users_input != "Lumpawaroo":
    if " | " in users_input:
        users_input = users_input.split(" | ")
        force_side = users_input[0]
        force_user = users_input[1]
        if force_side not in forces.keys():
            forces[force_side] = list()
        is_name_in_a_side = False
        for side in forces.keys():
            if force_user in forces[side]:
                is_name_in_a_side = True
        if not is_name_in_a_side:
            forces[force_side].append(force_user)
    elif " -> " in users_input:
        users_input = users_input.split(" -> ")
        force_user = users_input[0]
        force_side = users_input[1]
        if force_side not in forces.keys():
            forces[force_side] = list()
        is_user_in_force = False
        for side in forces.keys():
            if force_user in forces[side]:
                is_user_in_force = True
        if is_user_in_force:
            for side in forces.keys():
                if force_user in forces[side]:
                    forces[side].remove(force_user)
        forces[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    users_input = input()


for force, users in forces.items():
    if users:
        force_users_count = len(users)
        print(f"Side: {force}, Members: {force_users_count}")
        for user in users:
            print(f"! {user}")
