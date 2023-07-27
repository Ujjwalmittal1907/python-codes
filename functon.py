
# function for eliminating a special character from given string

def elimination_fun  (string,char_to_delete):

    '''TODO: docotests go here!
    >>>elimination_fun  ("ujjwal mittal",'a')
    'ujjwl mittl'''

    result=""
    for i in range(len(string)):
        if string[i]!=char_to_delete:
            result+=string[i]
    return result


