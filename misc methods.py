####
# Miscelaneous codebreaking methods.
# Morgan Grant
####

import string

#TODOLIST
#I seem to remember having an idea for a method that I think was called Abrupt_Decay but I don't recall just what the method did. was it a faster version of Ceaser Shift? somthing to do with Rot.
#Rotmeister <done>
#update it so the default alphabet is chosen at start of code, so you can change what the default alphabet is at a later date

def rotmeister(rot=False, alphabet=string.ascii_uppercase):     #"I'm good at fixing rot. Call me the Rotmeister. No, I'm the Doctor, don't call me the Rotmeister."
    '''
    >>> rotmeister("b")
    1

    >>> rotmeister(alphabet="1234567890")
    5
    '''
    ## gives you the proper rotation number given either a single char from in the alphabet(for values of A=That number), or gives the default for a given alphabet
    #  if you don't specify a rot, or you try to set the rot key as a letter that is not in the alphabet you gave it, it will return 0 so no rotation at all.
    if rot==False:    #if the user doesn't specify an input,
        if len(alphabet) % 2 == 0:  #and if the alphabet is an even number of letters long.
            rot=len(alphabet)//2    #it sets the default rotation to half of the alphabet length (so the encode is also the decode)
        else:       #hmmm.... what should the rotation defualt to when using a non-standard alphabet?
            rot = 0 #yea if you give a nonstandard alphabet and you DON'T supply a rot, you're gonna have a bad time.
    elif (type(rot) == str and (len(rot)==1)):
        if alphabet.count(rot.upper())==1:
            rot=alphabet.find(rot.upper())   #if you pass a 1 character string as rot and that string is inside alphabet, it will auto treat the first letter of alphabet as that for encoding purposes.
        else:
            return 0
    elif (type(rot) == int) and (int<=len(alphabet)):
        return rot
    else:
        return 0
    return rot

def caesarShift(plaintext, rot=False, encode=True, alphabet=string.ascii_uppercase):
    '''
    >>> caesarShift("the quick brown fox jumps over the lazy dog", 10)
    'dro aesmu lbygx pyh tewzc yfob dro vkji nyq'

    >>> caesarShift("twas brillig and the slythy toves did gyre and gimble in the wabe")
    'gjnf oevyyvt naq gur fylgul gbirf qvq tler naq tvzoyr va gur jnor'
    '''
    ##  Applies a Ceasar Shift to a recieved string.
    #   @param  (str)       plaintext is the text to be de/encoded
    #   @param  (int/char)  rot is the amount the alphabet was/will be shifted by to ENCODE the data. defaults to False so the first thing the method does is determine the default rotation. If you pass it a 1 digit string, it will determine rotation with that.
    #   @param  (bool)      encode controls whether you are encoding or decoding the data, defaults to encode
    #   @param  (str)       alphabet is included for future proofing in case of nonstandard alphabets, but it defaults to uppercase ASCII
    #   @return (str/int)   returns the result of the encoding process, or -1 if you fuck up the inputs
    #   current progress:UPDATING
    if rot==False:
        rot=rotmeister(rot,alphabet)
    if encode:
        ciphertext=""
        for char in plaintext:
            if alphabet.count(char.upper())>0:
                if char.isupper():
                    ciphertext += alphabet[( alphabet.find(char.upper())+rot )%len(alphabet)].upper()
                else:
                    ciphertext += alphabet[( alphabet.find(char.upper())+rot )%len(alphabet)].lower()
            else:
                ciphertext += char
        return ciphertext
            
    else:
        return caesarShift(plaintext, -rot, True, alphabet)
    

def abruptDecay(char, rot, alphabet=string.ascii_uppercase):    #a quicker, dirtier, one char at a time version of caesarShift
    '''
    >>> abruptDecay("Q", 13)
    'D'

    >>> abruptDecay("T", 20)
    'N'
    '''
    #note:if you pass a number as rot make sure it's a "start counting at 0" number
    char=char.upper()
    if type(rot) is str and (len(rot)==1):
        rot=rotmeister(rot)
    elif not (type(rot) is int and 0<=rot<=len(alphabet)):
        return rot        
    return alphabet[(alphabet.find(char)+rot)%len(alphabet)]


# Vigenere
def vigenere(plaintext, key, encode=True, alphabet=string.ascii_uppercase):
    #note that key is just a keyword, for example apple, and ciperkey will end up being appleappleappleap etc until it's the length of the keyword
    cipherkey=""
    key=key.upper()
    while len(cipherkey)<len(plaintext):
        pass
    #first set cipherkey to repeated key until it is the same length as the plaintext
    #then, call caesar(plainchar,cipherchar, encode, alphabet) for each plainchar,cipherchar in zip(plaintext,cipherkey)
    #appending each letter as you get it

def keymaker(keyword, alphabet=string.ascii_uppercase):
    key=""
    keyword=keyword.upper()
    for char in keyword:
        if key.count(char)<=0:
            key+=char
        if alphabet.count(char)<=0:     #if you put in a keyword with letters not in the alphabet
            return alphabet             #it will just return the alphabet itself
    for char in alphabet:
        if key.count(char)<=0:
            key+=char
    return key
    
# atbash
def atbash(plaintext, alphabet=string.ascii_uppercase):
    '''
    >>> atbash(string.ascii_uppercase)
    'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    >>> atbash("The Quick Brown Fox Jumped Over The Lazy Dog")
    'Gsv Jfrxp Yildm Ulc Qfnkvw Levi Gsv Ozab Wlt'
    '''
# z=a b=y etc
#DONE (I think)
    codekey=alphabet[::-1]
    ciphertext=""
    for char in plaintext:
        #print("Char:",char)
        if alphabet.count(char.upper())>0:
            if char.isupper():
                ciphertext += codekey[alphabet.find(char.upper())].upper()
                #print("Codeletter",codekey[alphabet.find(char.upper())].upper(),"AT",alphabet.find(char.upper()))
            else:
                ciphertext += codekey[alphabet.find(char.upper())].lower()
                #print("codeletter",codekey[alphabet.find(char.upper())].upper(),"AT",alphabet.find(char.upper()))
        else:
            ciphertext+=char
    return ciphertext


# playfair?
# use grids (list of lists)
def playfair(plaintext,key):
    pass

# polybius
#  12345
# 1abcde
# 2fghik
# 3lmnop
# 4qrstu
# 5vwxyz
#test= 44 15 43 44
def polybius(plaintext,alphabet=string.ascii_uppercase):
    pass

# rail fence
# A   C   D
#  T A K T A N
#   T   A   W
#acdtaktantaw
def railFence(plaintext, encode=True, rows=3):
    pass
    

# Scytale
#Acd
#tka
#taw
#atn
#Acdtkatawatn
#   ugh, this needs to be double checked to make sure i did it right...
def scytale(plaintext, diameter, encode=True):
    '''
    >>> scytale("THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG", 4)
    'TUBNJSRLDHIRFUOTAOECOOMVHZGQKWXPEEY'
    '''
    indx=0
    ciphertext=""
    if encode:
        workspace=[]
        for x in range(0,diameter):
            workspace.append([])
            for y in range(0,(len(plaintext)//diameter)+1):
                if not indx>=len(plaintext):
                    #ciphertext+=plaintext[indx]
                    workspace[x].append(plaintext[indx])
                    indx+=1
                    #print(workspace[x][y])
                else:
                    workspace[x].append("")
        for x in range(len(workspace)):
            for y in range(len(workspace[x])):
                ciphertext+=workspace[x][y]
    return ciphertext
                
                
                
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose = True)
