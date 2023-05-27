
def fc(elem="☕️", lipsa=""):
    rating_choice = []
    for i in range(0, 6):
        if lipsa != "" and i == 0:
          rating_choice += [lipsa]
        else:
            rating = ""
            for j in range(i):
                rating += elem
            rating_choice += [rating]

    print(rating_choice)

fc()
["☕️", "☕️☕️", "☕️☕️☕️",  "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"]