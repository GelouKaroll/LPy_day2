def hello_user(user_answer):

    counter = 0
    answers       = [ 'how are you?', 
                    'how are you?', 
                    'how are you, pal?', 
                    'c`mon pal you know what I want to hear. How. Are. You?', 
                    'you know, we can do it all day', 
                    'okey than']
    right_answers = ['good', 'very well', 'ok']

    while True:
        
        if user_answer in right_answers:
            print('Happy to hear it! ^.^ ')
            break
        else:
            user_answer = input(answers[counter] + " : ")
            if counter < (len(answers)-1):
                counter+=1
            else:
                counter = 0

user_answer = input('how are you?' + " : ").lower()
hello_user(user_answer)