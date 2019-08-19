# Game 1 NEW GAME 

print('''
                    .u:o. -c:o.  ex::u.    .czeez* .edB$ e@$$eu
                    e$MMMMMNu^$MMMb.#BMMM$c $MMM8P.d$RM$F4RMMMMMMRb
                    A$MMMMMMMMRb^$MMMMb^$MMMP MMMMF4$MMM8"dRMMMMMMMMMN
                    zMM8M***M$8M$.#8MMM$.$8M&J$M$%$RMM8*.$R8$#"""""BMM
                    $$".e@Rmu. "*M"    '    ^^             .o$$RMM$c'$
                    $.$RMMMMMM$$$$ dRRRRRRRRRR$$MMMMMMRL'$$RMMMMMMMM$.
                    .$MMMMMMMMM$" $RMMMMMMMMMMMMMMMMMMMMb ^4$MMMMMMMM$
                    JMMMM$$**" ..$MMMMMMMMMMMMMMMMMMMMMMM$.:c  "***$MM
                    $M"..oenR$".$MMMMMMMMMMMMMMMMMMMMMMMMM$.*$$MMMRc.*
                    * d$MMMM$"u$MMMMMMMMMMMMMMMMMMMMMMMMM8MRc"$MMMMM$b
                    .$RMMM$# J$MF       "MMMMMMMMM   .....4M$b "$MMMM$
                    dMM8P"  dMMM$ $M8P4 4MMMMMMMMM 'L"$M$ JMMMF  "*88M
                    $$P\d$$ $MMMM$L..d$r4MMMMMMMMM <$$u.e$RMMMF $M$c"$
                    $ zRMM& ^8MMMMMMMMMF'MMMMMMMMM 4MMMMMMMMMG  $MMM$r
                     $RMMMF$f)MMMMMMMMMF'MMMMMMMMM 4MMMMMMMMMF.$'$MMMM
                    'MMM$FJR$ $MMMMMMMMF4MMMMMMMMM 4MMMMMMMM$ $Rh^$MMM
                    AMM8\dRMMF RMMMMMMM 4MMMMMMMMM  MMMMMMM$".MMMRb$MM
                    AM$.$MMMMF.3MMMM$P*-'*********- "*NMMMM*..RMMMM$'$
                    AP.$RMMM$:$ $M$".oM$.'$RRRRR$".d$5u'*M$ $$?RMMMM$'
                    $ $MMMM$\$Rb'P eMMMMM$c"$M8# dRMMMMRc"F4MMb^$MMMMb
                     $RMMMPzRMM!  eRMMMMMMR$c" dRMMMMMMMR  'MMMR.?$MM$
                     $M8$ $MMMM"x $MMMMMMMMMM ?MMMMMMMMM$ 3'$MMM$b'$MM
                    ARM$.$RMMMP $$'BMMMMMMMMM 4MMMMMMMM8P4$$ $MMMM$.$M
                    A$F4RMMMMf $RM  *88MMM88M J8MM888$$\ @MMMr5MMMM$.$
                     $ $RMM8P.$MMMF?b.                z$F$MMMMc3BMMM$'
                      4MMMM$-$RMM8F4MM$ '8MMMMMMMM$ dRMM$#8MMM$r#8MMM.
                      4MMM$.$MMMM$ RMMM$ 3MMMM$ 8MMM
                       $MM$'MMMMP zRMMM$ .'**4P*".$ $MMMM$'$MMMM $MM$
                       4MMC'MMMM$:$MMMMPoM$b   .@$M$$MMMMRL^$MMMF$M8
                        "$$'MMM$\$MMMM$ MMMM$.4RMMM$r$MMMMRr*MMMN$$"
                         'N'$MM$4$MMMMF$MMMMM$$RMMMM$4$MMMM$$MMM @
                            #$MN4MMMMMF$MMMMM$#MMMMMM RMMMM$$M$F
                             ?$$.$MMMMF$MMMMMF RMMMMM $MMMM\$MP
                               *$'$MMMb3MMMMM  RMMMMNJRMMNFJ*
                                     #88$L#8MMMr RMMM$z$M8$"
                                     ^*$P/*B8$$R8M"zP*" ''')
import sys
def text_printer(text, delay=0.03):
 
    """ Function that prints text to the terminal in a cool way!
 
        The function takes two arguments, the text to be printed in a string
        format and the delay, which is by default 0.03 seconds."""
 
    for character in text:
        print(character, end = '')
    else:
        time.sleep(delay) 
#add timer
#choice of a gamble of weather you can advance or not eg you can jump Ahead
#start_time()
#end_time()

Mydict = {'1': 'what is your name?'}
import time

Name = input(Mydict['1'])
print('Welcome', Name, 'your quest  will now begin!')

def Question1():
    Confidence = int(input('How confident are you on a scale of 1-10?', ))
    return Confidence

Confidence = Question1() #why is this needed?
loop = 'yes'
while loop == 'yes':
    if Confidence < 3:
        print('HAHA Pathetic, start again and get some confidence')
        time.sleep(1)
        Confidence = Question1()
    elif Confidence < 8:
        print('Being Humble is a top quality, your next stop awaits')
        loop = 'no'
    elif Confidence < 11 :
        print('Wrong answer, start again and be humble')
        time.sleep(1)
        loop = 'yes'
        Confidence = Question1()
    elif Confidence > 10:
        print('1-10!, YOU IDIOT!')
        time.sleep(1)
        loop ='yes'
        Confidence = Question1()

import string

def QuestionX():
    Alphabet = list(string.ascii_lowercase)
    AnswerLetter = input('choose any letter/symbol:', ).lower()
    while AnswerLetter not in Alphabet:
        print('Letter please')
        AnswerLetter = input('choose any letter/symbol:', ).lower()
    AnswerNumber = int(input('choose any number:', ))
    while AnswerNumber not in range(-1000000,10000000):   # why numbers not working any numbers in range should move on to nect step
        print('Number please')
        AnswerNumber = input('choose any number:', )
    else:
        AnswerX = AnswerLetter + str(AnswerNumber)
    print('your name now is', AnswerX)
    return AnswerX

AnswerX = QuestionX()

def Question2():
    NoWater = int(input('how many days can an average human last without water?', ))
    return NoWater

NoWater = Question2()
if NoWater == 3:
    print('This quest could last quite sometime')
elif NoWater == 4:
    print('This quest could last quite sometime')
else:
    print('start again, hint: your 3-4 days is running out') #start whole quiz again
    sys.exit()

import random

def QuestionW():
    RandomNumber = random.randint(1,10000)
    print(RandomNumber, 'this is key')
    time.sleep(3)
    return RandomNumber
RandomNumber = QuestionW()
    
def Question3():

    while True:

        Answer3 = input('I am an odd number.Take away a letter and I become even. What number am I?', )

        if Answer3 == 7 or 'seven':

            print('Impressive, proceed')

            break

        else:

            print('Try again')
        
    return Answer3

Answer3 = Question3()
     
def Question4(): 
    trys = 3
    answer4 = ' no answer! !'
    while trys > 0 and answer4 != 2 or 'b':
        print('what is 9+10?')
        answer4 = input('A:19 \nB:20\nC:21\n', )
        if answer4 == 'C' or 21:
            print('well done, on to the next question')
            break
        else:
            print(':(, try again')
            trys = trys -1
    return answer4

answer4 = Question4()


def Question55(): 
    trys = 3
    answer4 = ' no answer! !'
    while trys > 0 and answer4 != 2 or 'b':
        print('what Series are Mike Ross and Harvey spector from?', )
        answer4 = input('A:Suits \nB:Sherlock\nC:The Wire\n', )
        if answer4.upper() == 'A':
            print('well done, on to the next question')
            break
        else:
            print(':(, try again')
            trys = trys -1
    return answer4

Question55()

def Question66(): 
    trys = 3
    answer4 = ' no answer! !'
    while trys > 0 and answer4 != 2 or 'b':
        print('what Series are Rio and Tokyo from?', )
        answer4 = input('A:Game of thrones \nB:The Punisher\nC:Money Heist\n', )
        if answer4.upper() == 'C':
            print('well done, on to the next question')
            break
        else:
            print(':(, try again')
            trys = trys -1
    return answer4

Question66()

def Question77(): 
    trys = 3
    answer4 = ' no answer! !'
    while trys > 0 and answer4 != 2 or 'b':
        print('what colour of visible light travels fastest?', )
        answer4 = input('A:Blue \nB:Red \nC:None of the above\n', )
        if answer4.upper() == 'C':
            text_printer('well done, all light travels at the same speed,  on to the next question')
            break
        else:
            print(':(, try again')
            trys = trys -1
    return answer4

Question77()

time.sleep(2)

text_printer('''
                                          
                                                        | | |  /
                                                         \|_|_/
                                                       ,--/.__/--'
                       _.-/   _   \-._                    .'|
                     .'::(_,-' `-._)::`.                  |:|
                    (:::::::::::::::::::)                .':|
                     \_:::;;;::::;;;:::/    /            |::|
             \        ,---'..\::/..`-.'    /             |::|
              \       \_;:....|'...:_ )   /             .'=||
               \.       )---. )_.--< (   /'             ||=||
                \\     //|:: /--\:::\\\ //             _||= |
                 \\   ||::\:|----|:/:||/--.______,--==' \ - /
          -._     \`.  \\:|:|-- -|:\:/-.,,\\  .----'//'_.`-'
      \.     `-.   \ \ _|:|:|-- -|::||::\,,||-'////---' |/'
       \\       `._)\ / |\/:|-/|--\:/|. :\_,'---'       /
        \\_      /,,\/:.'\\/-.'`-.-//  \ |
        /`\-    //,,,' |-.\-'\--/|-/ ./| |             /
         /||-   ||, /| |\. |.-==-.| . /| |            | /
 __  |    /||-  ||,,\- | .  \;;;;/ .  .':/         _,-=/-'
/  \//    /||-  ' `,-|::\ . \,..,/   /: /         /.-'
,--||      /||-/.-.'  \  `._ `--' _.' .'|        //
.--||`.    /||//\ '   |-'.___`___' _,'|//       /;
  /\| \     ///\ /     \\_`-.`--`-'_==|'       /;'
 / |'\ \.   //\ /       \_\__)\`==-_'_|       / /
  .'  \.=`./|\ /          \`-- \--._/_/------( /
       \.=| `_/|-          |\`-| -/| `--------'
        \\` ./|-/-         |\`-| |-|     ________
         `--\ |=|'        _|\`-| |-|----'.-._ ..\`-.
             -|-|-     .-':`-;-| |./.-.-( | ||..|=-\\
             `'= /'   / ,--.:|-| ||_|_|_|_|-'__ .`-._)
              /|-|- .' /\ \ \|-` \\ ____,---'  `-. ..|
               /\=\/..'\ \_>-'`-\ \'              \ .|
               `,-':/\`.>' |\/ \/\ \              `- |
               //::/\ \/_/|-' \/| \ `.            / ||
              / (:|\ \/) \ \|.'-'  `-\\          |;:|\_
             || |:`-/:.'-|-' \|       \\          `;_\-`-._
             \\=/:_/::/\| \|          |\\            `-._ =`-._
              \_)' |:|                | //               `--.__`-.
                   |:|                                         )\|
                   /;/                                         / (\_
                  / /                                         |\\;;_`-.
                _/ /                                          ' `---\.-\
               /::||
              /:::/
             //;;'             
             `-'

''')
      
print('Lets Test your Memory')

def LastQuestion():
    AnswerLastQuestion = input('what is your name?', )
    if AnswerLastQuestion != AnswerX:
        print('''
             YOU
             HAVE
             FAILED''')
    else:
        print('''
                    CONGRATULATIONS
                    YOU
                    HAVE
                    PASSED''')

AnswerLastQuestion = LastQuestion()
    
text_printer('''
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__ 
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__
\ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / _
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \__

    ''') 
#def Question4():
    
#trys = 3

#def walkintheforest():''''
   # pass

def QuestionW1():
    AnswerW1 = int(input('Whats key?', ))
    while AnswerW1 == RandomNumber:

            print('You have secured the W')

            break
    while AnswerW1 != RandomNumber:
        print('TRY AGAIN or take the L')
        AnswerW1 = int(input('thats it ...', ))
    return AnswerW1

AnswerW1 = QuestionW1()


text_printer('GAME OVER!')
sys.exit()



