def age_detector(in_age):

    if in_age.isdigit():
        
        in_age = int(in_age)
        
        if in_age <= 0:
            return "Please insert your reale age"
        elif 0 < in_age <=  7: 
            return "go to the kindergarten!" 
        elif 7 < in_age <= 18:
            return "you are only schoolchild"
        elif 18 < in_age <= 24:
            return "enjoy your best time in university!"
        elif in_age > 24:
            return "you have entered a difficult time ..."

    else:
        return "Please insert your reale age"


age = input("Please insert your age: ")

msg = age_detector(age)

print(msg)

