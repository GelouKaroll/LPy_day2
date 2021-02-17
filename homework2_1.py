school = [
    {'school_class': '2a', 'scores':[3,5,4,2,3]},
    {'school_class': '2b', 'scores':[5,4,3,5,3]},
    {'school_class': '2c', 'scores':[2,3,5,3,4]}
]

av_score = 0
quanity  = 0

for score in range(len(school)):
    list_score = school[score]['scores']
    av_score += sum(list_score)
    quanity  += len(list_score)

av_score /= quanity

print("Average grade: {}".format(av_score))