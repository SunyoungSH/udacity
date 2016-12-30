# IPND Stage 2 Final Project

text_easy = '''
<b>text</b> makes the text (___1___).
<em>text</em> makes the text (___2___).
<strong>text</strong> makes the text (___3___).
<br> makes a line (___4___).
<p>text</p> defines text as a (___5___).
'''
answer_easy = ["bold", "italic", "strong", "break", "paragraph"]
text_medium='''
A (___1___) is created with the def keyword. You specify the inputs a (___1___) takes by
adding (___2___) separated by commas between the parentheses. (___1___)s by default return (___3___) if you
don't specify the value to return. (___2___) can be standard data types such as string, number, dictionary,
tuple, and (___4___) or can be more complicated such as objects and lambda functions.
'''
answer_medium=["function", "parameters", "nothing", "list"]
text_hard='''
Schreibt die richtige Adjektivform in die Luecken.
Bitte benutzt die aufgeloeste Umlaute. z.B. ae, ue, oe.

Die (___1___) (privat) und (___2___) (beruflich) Nutzung eines Smartphones ist heutzutage normal.
Das (___3___) (staendig) Online-Sein kann zu (___4___) (suechtig) Verhalten fuehren.
Man kann die (___5___) (koerperlich) Auswirkungen der Sucht messen.
Man kann bei Mediensuechtigen (___6___) (aehnlich) Wirkungen beobachten wie bei Alkoholsuechtigen.
Pauly erklaert, wie Jugendliche (___7___) (ungesund) Verhalten vermeiden koennen.
Er glaubt, dass man mit (___8___) (haeufig) Aktivitaeten, fuer die man kein Smartphone und keine Medien braucht, die Suchtgefahr senken kann.
'''
answer_hard=["private","berufliche","staendige","suechtigem","koerperlichen","aehnliche","ungesundes","haeufigen"]

# User selects a difficulty level. Depending on which difficulty level the user chose, the quiz with corresponding level is loaded.
# User is also given a choice to exit the game.
def select_difficulty():
    user_input = raw_input('''Please select a difficulty level for the quiz.
Press 1 for easy, 2 for medium and 3 for hard. Press 4 to exit game.:  ''')
    if user_input == "1":
        return play_quiz(text_easy, answer_easy)
    elif user_input == "2":
        return play_quiz(text_medium, answer_medium)
    elif user_input == "3":
        return play_quiz(text_hard, answer_hard)
    elif user_input == "4":
        return exit()
    else:
        print "What you selected was not valid."
        return select_difficulty()

# When a user gives a correct answer, the blank for the answer is filled.
def print_answer(n, text, answer):
    while n >= 0:
        text = text.replace("___"+str(n)+"___", answer[n-1])
        n = n - 1
    print text

def play_quiz(text, answer):
    print "Here we go!"
    i = 0
    error_count = 0
    print text
    while i < len(answer):
        user_input = raw_input("Enter the answer for blank "+str(i+1)+": ")
        if user_input == answer[i]:
            i = i + 1
            error_count = 0
            print_answer(i, text, answer)
        else:
            error_count = error_count + 1
            print "You have " + str(5 - error_count) + " tries left."
            if error_count == 5:
                break
    # Depending on how the while loop ended, the game shows appropriate text and brings the user to the beginning of the game.
    if error_count == 5:
        print "You have failed. Please try again."
    else:
        print "Congratulations! You've won. Try the next level!"
    return select_difficulty()

# Runs the game.
select_difficulty()
