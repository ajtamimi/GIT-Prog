'''

Done by: Eng. Alaa Jalal Al Tamimi

STD number: 196206

Teacher name: Dr. Zein Salah

IS601: Programming and Algorithms for Intelligent Systems

'''


Paragraph1 = """
One day a rabbit was boasting about,how fast he could run.
He was laughing at the turtle for being so slow. Much to the
rabbit’s surprise, the turtle challenged him to a race. The rabbit
thought this was a good joke and accepted the challenge. The fox
was to be the umpire of the race. As the race began, the rabbit
raced way ahead of the turtle, just like everyone thought.
The rabbit got to the halfway point and could not see the turtle
anywhere. He was hot and tired and decided to stop and take a short
nap. Even if the turtle passed him, he would be able to race to the
finish line ahead of him. All this time the turtle kept walking step
by step by step. He never quit no matter how hot or tired he got.
He just kept going.
However, the rabbit slept longer than he had thought and woke up.
He could not see the turtle anywhere! He went at full speed to
the finish line but found the turtle there waiting for him.
""".lower()

Paragraph2 = """
Flights resumed Thursday at an Istanbul airport after a Pegasus Airline
passenger jet skidded off a runway, killing three people and injuring 180 others.
Sabiha Gokcen Airport restarted operations at around 4 am though delays and
cancellations continued.
On Wednesday evening, a Boeing 737 operated by the low-cost airline landed 
from Izmir on Turkey's western coast during strong winds and heavy rain and 
overshot the runway. It skidded about 50 to 60 meters before it dropped into 
the ditch from a height of about 30 meters, according to the city's governor, 
Ali Yerlikaya.
The plane, carrying 177 passengers and six crew members, broke up into three 
parts upon impact. The plane was 11 years old, according to flight tracking 
website Flightradar24.
Live images broadcast on Turkish television showed several people climbing 
through a large crack in the severed aircraft and escaping onto one of the 
wings at the rear.
Yerlikaya, speaking early Thursday, said all those injured were stable and 
four people had significant injuries, but he didn't give details on how severe 
they were.
The passengers included 22 people from 12 countries.
Pegasus Airlines changed its logo on Twitter to a blackened version in a sign 
of mourning, and said its "priority is to support the relatives and friends 
who have lost loved ones.” Its fleet of 83 planes fly to more than 100 
destinations.
Police guarded the wreckage Thursday morning.
Another Pegasus Airlines plane skidded off the runway at the same airport 
in Istanbul on Jan. 7, causing the temporary closure of the airport. 
There were no injuries.
In January 2018, another Boeing 737 in the Pegasus fleet slid off a runway
at Trabzon Airport in northeastern Turkey. The plane came to rest in the 
dirt above the Black Sea with its nose pointed toward the water.
No one was injured. 
""".lower()
 
Paragraph3 = """
Three people were killed and 179 others injured after a plane skidded off a 
runway and crashed at Istanbul's Sabiha Gökçen Airport during landing on 
Wednesday, according to the Turkish Minister of Health.
Firefighters, medics and police teams raced to the scene, where the nose of the 
plane appeared to have separated from the rest of the aircraft, according to 
video from local television stations. Some parts of the plane appeared to be on 
fire.
The passenger plane is a Pegasus Airlines flight that was arriving from Izmir, 
on Turkey’s west coast.
Rescue members evacuate an injured person from the wreckage of a plane after it 
skidded off the runway at Istanbul's Sabiha Gokcen Airport, in Istanbul, 
Wednesday, Feb. 5, 2020.
There were 183 passengers and six crew members on board, according to Istanbul 
Gov. Ali Yelikaya.
The condition of those injured was not immediately clear.
Pegasus Airlines shares in the profound sorrow of all the people affected by 
this tragic accident, the company said in a statement. "Above all, we would 
like to express our profound sympathy and heartfelt condolences to those families 
and friends who have lost loved ones and extend our thoughts to them at this 
difficult time. Our injured passengers continue to be treated in hospital and 
we wish them all a swift recovery."
A Pegasus airlines Boeing 737 plane lies in pieces after it skidded off the 
runway at Istanbul's Sabiha Gokcen airport, Feb. 5, 2020.
The exact cause of the crash is still unknown, although Yelikaya said the 
plane overshot the runway and then dropped about 98 to 131 feet.
It is the second time in recent years a Pegasus flight skidded off a runway in 
Turkey.
A commercial jet carrying 168 people overshot an icy airstrip at Ankara-Tabzon 
Airport in January 2018, although all 162 passengers and six crew members were 
unharmed.
""".lower()

# Start of Function Area

def user_wellcome():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    print("There are three stored paragraphs in the program:\n")
    print("Number 1 is about Rabbit and turtle,\n")
    print("Number 2 and 3 are about Pegasus plane that skided in Istanbul in 2020,\n")
    print("Number 4 for your new paragraph.\n")


def data_entered():
    user_input= int(input ("Please enter paragraph number: 1 or 2 or 3 or 4: \n"))
    
    if(user_input==1):
       input_text= Paragraph1
    elif (user_input==2):
        input_text= Paragraph2
    elif (user_input==3):
        input_text= Paragraph3
    else:
        input_text= (input ("Please enter the first paragraph:")).lower()
    return input_text   


def Preposition():
    p = {" of "," with "," at "," from "," into "," during "," including "," until "," against "," among "," throughout "," despite "," towards "," upon "," concerning "," to "," in "," for "," on "," by "," about "," like "," through "," over "," before "," between "," after "," since "," without "," under "," within "," along "," following "," across "," behind "," beyond "," plus "," except "," but "," up "," out "," around "," down "," off "," above "," near "}
    return p


def irrelevant_word():
    irr =  {". ", ", " , "\n", " a ",   " ourselves ", " thought " ," hers ",  " between ",  " yourself ",  " but ",  " again ",  " there ",  " about ",  " once ",  " during ",  " out ",  " very ",  " having ",  " with ",  " they ",  " own ",  " an ",  " be ",  " some ",  " for ",  " do ",  " its ",  " yours ",  " such ",  " into ",  " of ",  " most ",  " itself ",  " other ",  " off ",  " is ",  " s ",  " am ",  " or ",  " who ",  " as ",  " from ",  " him ",  " each ", " the",  " themselves ",  " until ",  " below ",  " are ",  " we ",  " these ",  " your ",  " his ",  " through ",  " don ",  " nor ",  " me ",  " were ",  " her ",  " more ",  " himself ",  " this ",  " down ",  " should ",  " our ",  " their ",  " while ",  " above ",  " both ",  " up ",  " to ",  " ours ",  " had ",  " she ",  " all ",  " no ",  " when ",  " at ",  " any ",  " before ",  " them ",  " same ",  " and ",  " been ",  " have ",  " in ",  " will ",  " on ",  " does ",  " yourselves ",  " then ",  " that ",  " because ",  " what ",  " over ",  " why ",  " so ",  " can ",  " did ",  " not ",  " now ",  " under ", " he ",  " you ",  " herself ",  " has ",  " just ",  " where ",  " too ",  " only ",  " myself ",  " which ",  " those ",  " i ",  " after ",  " few ",  " whom ",  " t ",  " being ",  " if ",  " theirs ",  " my ",  " against ",  " a ",  " by ",  " doing ",  " it ",  " how ",  " further ",  " was ",  " here ",  " than"}
    return irr


def text_cleaning(input_text):
    for prep in Prepositions:                       # Remove Prepositions
       input_text = input_text.replace(prep, " ")
    for iw in irrelevant_words:                     # Remove irrelevant_words
       input_text = input_text.replace(iw, " ")
       word_list = input_text.split(" ")            # Convert text to list of unique words
    return word_list

 
def count_iterative(word_list):
    word_histogram = {} # empty dictionary
    for word in word_list:    # adding dictionary keys
        if word not in word_histogram.keys():
            word_histogram[word] = 1
        else:
            word_histogram[word] = word_histogram[word] + 1
    word_histogram.pop("")   # remove empty keys
    return word_histogram
     

def mostly_used_word(word_hist):
    import operator 
    Repeted_word=set()    # empty set
    i=0
    while( i<6) :       # 6 Is the number of mostly used word in paragraph.
        Word= max(word_hist.items(), key=operator.itemgetter(1))
        word_hist.pop(Word[0])
        Repeted_word.add(Word[0])
        i+=1    
    return Repeted_word

def Result(Repeted_word1, Repeted_word2):
    Number_of_repeted_word=0 # see global option note
    
    def Paragraph_maping(Repeted_word1, Repeted_word2): 
        for word in Repeted_word1:
            if (word in Repeted_word2):
                print(word)
                nonlocal Number_of_repeted_word
               # global Number_of_repeted_word
                Number_of_repeted_word+=1
        #return Number_of_repeted_word
    
    print ("\n******************************************************")
    print ("The repeted words in the first paragraph are: ")
    print (Repeted_word1)
    print ("\nThe repeted words in the second paragraph are: ")
    print (Repeted_word2)
    print ("\nThe common repeted words in the two paragraphs are: \n")
  
    Paragraph_maping(Repeted_word1, Repeted_word2)  # inner function
           
    print ("\nNumber of repeted words are: " , Number_of_repeted_word)
    if (Number_of_repeted_word>2):   # number of overlap words
        print ("\n The two paragraphs are relevant.")
    else:
       print ("\nThe two paragraphs are not relevant.")
    print ("******************************************************")

# End of Function Area


