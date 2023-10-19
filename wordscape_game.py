'''
Introduction

=>In this project we will create the console-based simulator of the
wordscapes games,
where the user is given some letters and the user has to guess the
words from those letters.
=>This game is designed for only 5 levels. 
=>At each level the user will be given some letters and the
user has to guess 3 words to move to the next level.
=>If the user guesses the wrong word at any chance,
the user will lose one live point and will be asked to give another word. 
=>The user will get 5 lives which means the user can make 5 wrong guesses. 
=>After 5 wrong guesses the game will automatically get over and the user will get the final score. 
=>But if the user makes correct 3 guesses, they will move to the next level. 
=>At the end of each level the user will be asked if the user wants to continue or not.
=>If the user selects yes, the game will continue but
if the user selects no then the game will stop at that level and the final score will be displayed.

h,o,l,i,d,a,y =>day,oil,hay
'''

letters = [['h','o','l','i','d','a','y'],
           ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm','i','n','g'],
           ['b','o','o','t','c','a','m','p'],
           ['f','l','o','w','c','h','a','r','t'],
           ['w', 'o', 'r', 'd', 's', 'c', 'a','p','e','s']]

words = [["hi","hay","oil","day","had","lay","dal","lad","lid","hold","lady","hail"],
         ["go","an","in","no","on","map","mom","gap","gag","pig","man","ping",
          "pong","pram","prom","ramp"],
         ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","camp",
          "comb","boom","pact","atom"],
         ["of","at","or","to","caw","cow","how","who","calf","claw","flaw","flow",
          "fowl","wolf","crow","half"],
         ["we","do","as","cap","caw","cop","cow","paw","cod","dew","pad","cape",
          "cope","crap","crew","crop","pace"]];

lives=5
level=0
score=0

while level<5:
    print("\n Level :",level+1)
    #print("level {}".format(level+1))
    print("\n----****----Guess 3 words using given letters : ----****----")
    print()
    print(letters[level])
    print("\n ")

    wordcount=0
    match=False
    word=""
    oldword=""

    while wordcount==0 or wordcount<3:
        match=False
        word=input("Word : ")
        if not(word.lower()==oldword.lower()):
            for w in words[level]:
                if(word.lower()==w):
                    wordcount+=1
                    score+=1
                    oldword=word
                    match=True
                    break

        if not match:
            print("\n\t Wrong Guess !!")
            lives-=1

        if lives==0:
            print("\n Game Over! Better Luck Next Time!")
            print("\n Score is :",score)

    wordcount=0
    match=False
    word=""

    if lives==0:
        break
    if level==4:
        print("\n Thanks for playing the game!")
        print("\n Your score is :",score)
        level+=1
    else:
        choice=input("\n \tIf you want to continue or end. Type y/n :--")
        if(choice.lower()=="y"):
            level+=1
        else:
            print("\n Thanks for playing the game!")
            print("\n Your score is :",score)
            break



        
