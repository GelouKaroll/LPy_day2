def ask_user():

    qa_dict = {
        'who are you?' : 'you little stupide program. Blip-blop',
        'what are you?' : 'your little stupide program. Blip-blop',
        'what are you doing?' : 'only what you did in my code. Blip-blop',
        'how old are you?' : 'are you serious? .-.',
        }

    qa_exit = ['exit', 'end', 'close']

    while True:

        user_question = input('Ask me about anything!\n')
        user_question = user_question.lower()

        if user_question in qa_exit:
            print('_________________________________')
            print('{} you man!'.format(user_question))

            break
        elif user_question in qa_dict:
            print('_________________________________')
            print('user : {}'.format(user_question))
            print('machine : {}'.format(qa_dict[user_question]))
            print('_________________________________')
        elif user_question not in qa_dict:
            print('_________________________________')
            print('user : {}'.format(user_question))
            print('machine : sorry, my creator is too junior for complete ai code')    
            print('_________________________________')      

ask_user()