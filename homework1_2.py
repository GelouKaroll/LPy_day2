def str_compare(str1, str2):

    if type(str1)!=str or type(str2)!=str or str1.isdigit() or str2.isdigit():
        return 0
    elif str1==str2:
        return 1
    elif len(str1)>len(str2): 
        return 2
    elif str1!=str2 and str2=='learn':
        return 3

val1 = input("Input first string: ")
val2 = input("Input secind string: ")

msg = str_compare(val1, val2)

print(msg)
