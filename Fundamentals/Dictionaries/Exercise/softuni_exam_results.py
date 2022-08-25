#12. *SoftUni Exam Results

#Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the task of taking all the submissions and analyzing them properly. 
#You should collect all the submissions and print the final results and statistics about each language in which the participants submitted their solutions.

#You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". 
#You should store each username and their submissions and points. If a student has two or more submissions for the same language, save only his maximum points.

#You can receive a command to ban a user for cheating in the following format: "{username}-banned". 
#In that case, you should remove the user from the contest but preserve his submissions in the total count of submissions for each language.

#After receiving "exam finished", print each of the participants in the following format:

#"Results:

#{username1} | {points}

#{username2} | {points}

#…

#{usernameN} | {points}"

#After that, print each language used in the exam in the following format:

#"Submissions:

#{language1} - {submissions_count}

#{language2} - {submissions_count}

#…

#{language3} - {submissions_count}"


results = input()
users_score = dict()
languages = dict()

while results != "exam finished":
    results = results.split("-")
    username = results[0]
    if "banned" in results:
        is_banned = True
        users_score[username]["is_banned"] = is_banned
    else:
        language = results[1]
        if language not in languages.keys():
            languages[language] = 0
        languages[language] += 1
        score = int(results[2])
        is_banned = False
        if username not in users_score.keys():
           users_score[username] = {"score": score, "is_banned": False}
        else:
            if score > users_score[username].get("score"):
                users_score[username]["score"] = score

    results = input()
print("Results:")
for user in users_score.keys():
    score = users_score[user].get("score")
    is_banned = users_score[user].get("is_banned")
    if not is_banned:
        print(f"{user} | {score}")
print("Submissions:")
for language in languages.keys():
    print(f"{language} - {languages[language]}")
