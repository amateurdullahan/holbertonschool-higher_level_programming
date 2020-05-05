#!/usr/bin/python3
def no_c(my_string):
    my_strlist = list(my_string)
    for a in range(len(my_strlist)):
        if my_strlist[a] == 'c' or my_strlist[a] == 'C':
            my_strlist[a] = ''
    my_string = ''.join(my_strlist)
    return my_string
