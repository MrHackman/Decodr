


def permute(permuteMe, dothis, frontEnd=False):
    '''
    Does dothis() to all versions of of possible orderings of the string permuteMe.
    frontEnd is used for recursion, and will do dothis with frontEnd attached to the front of strings passed to dothis.
    Will eventually be updated for using lists as well.
    >>> permute("123",print)
    123
    132
    213
    231
    312
    321
    '''
    #Im an idiot:
    #https://docs.python.org/3.3/library/itertools.html
    #ctrl-F "permutations"
    # rule 1 of coding complex shit; check to see if someone else has written it before you
    if frontEnd==False:
        if type(permuteMe)==list:
            frontEnd=[]
        elif type(permuteMe)==str:
            frontEnd=""
        else:
            return
    if len(permuteMe)<=1:
        dothis(frontEnd+permuteMe)
    else:
        for item in permuteMe:
            if type(frontEnd)==list:
                pass    #the problem is most things that work with lists will modify the original
                print("Ung tricky scope issues here. needs retooling")#I need it to return a modified value instead
                break
            else:   #if anything other than a string ends up here, something broke.
                permute(permuteMe.replace(item, ""), dothis, frontEnd+item)





if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)		#note that verbose=True helps you see the actual output
