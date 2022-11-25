import random 
import time
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def game_run():
    Name,Gen,DOB=data_user()
    time_fun()
    opt_con_check
    f_score=game_ans_working()
    print('\n',"Name of Participant/User is: ",Name,sep="")
    print("Gender : ",Gen)
    print("DOB : ",DOB)
    print("Final Score is : ",f_score,'\n')
    print("Thank You For Playing")
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def data_user():
    name=input("Enter your Name: ")
    name=name.title()
    while True:
        try:
            reg=input("Enter Your Registration Number: ")
            if len(reg)==8 and reg.isnumeric():
                break
            else:
                print("Enter Correct Registration Number")
        except ValueError:

            continue 
    while True:
        try:
            gen=input("Enter Your Gender(Male(M)/Female(F)/Other(O) : ")
            gen=gen.capitalize()
            if gen=='M' or gen=='Male':
                gen='Male'
                break
            elif gen=='F' or gen=='Female':
                gen='Female'
                break
            elif gen=='O' or gen=='Other':
                gen='Other'
            else:
                print("Enter Correct Gender")
        except ValueError:
            continue 
    while True:
        try:
            print("Enter Your Date Of Birth")
            date=int(input("Enter Date: "))
            month=int(input("Enter Month(in Numbers): "))
            year=int(input("Enter year of Birth (from 1995 to 2022): "))
            if 1<=date<=31 and 1<=month<=12 and 1995<=year<=2022:
                dob=str(date)+'/'+str(month)+'/'+str(year)
                break
            else:
                print("Enter Correct DOB")
        except ValueError:
            continue
    return name,gen,dob
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def time_fun():
    global ti
    ti=time.localtime()
    cur_date=time.strftime("%d/%m/%Y",ti)
    cti=time.strftime("%H:%M:%S %p",ti)
    print('\n'"Today's Date is:",cur_date,sep="")
    print("Current Time is:",cti,'\n')
    second=6
    print("Please Wait , Your Quiz Will Start in: ",end="\n")
    for i in range(6):
        if second==6:
            pass
        else:
            print(second,)
            time.sleep(1)
        if second==1:
            print('\n'," "*15+"--->Get Ready<----"+" "*15,'\n')
            time.sleep(3)
        second=second-1
    
    print('-'*50)
    print(" "*22+"Start"+" "*25)
    print('-'*50,'\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def game_ans_working():
    score=0
    t_round=len(questions)
    for r in range(1,6):
        print('-'*50)
        print(' '*19,'ROUND -->',r,' '*10)
        print('-'*50,'\n')
        que=1
        t_score=0
        for i in range(0,t_round):
            key=random.choice(list(questions.keys()))
        #output question no and questions
            if que<=5:
                print(que,key,sep=" : ")
                opt_con_check()
                if guess==questions.get(key):
                    print('-'*50)
                    print(' '*10+'--> Congratulations <-- '+' '*10)
                    print('-'*50,'\n')
                    t_score=t_score+1
                else:
                    print('-'*50)
                    print(" "*4,'Good Luck Next Time')
                    print('-'*50,'\n')
                if que<5:
                    print("Wait For Next Question , Question Will appear Soon: ","\n")
                    time.sleep(1)
                que+=1
            else:
                print('\n',"Your Score in this Round is:",t_score,'\n')
                break
            score=t_score+score
        if r<5:    
            print("Next Round Will Start in 5sec")
        time.sleep(5)
    return score
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def opt_con_check():
    u_ans=[]
    while True:
        try:
            global guess
            guess=input("Enter the Answer(True(T)/False(F):")
            guess=guess.upper()
            if guess=='T' or guess=='TRUE':
                guess='TRUE'
                break
            elif guess=='F' or guess=='FALSE':
                guess='FALSE'
                break
            else:
                print("Enter Correct option")
        except guess.isalpha():
            print("Enter Alphabets")
            continue
#--------------------------------------------------------------------------------------------------------------------------------------------------------
questions={'The Big Apple is a nickname given to Washington D.C in 1971.':'FALSE',
'Copyrights depreciate over time.':'TRUE',
'People may sneeze or cough while sleeping deeply.':'FALSE',
'Electrons move faster than the speed of light.':'FALSE',
'Light travels in a straight line.':'TRUE',
'Vitamin C is also known by the chemical name of Ascorbic Acid.':'TRUE',
'The Nobel prize-winning novel ‘The Old Man and the Sea’ was written by the American author John Steinbeck.':'FALSE',
'In theory, it takes over 5,000 helium balloons to lift an average-sized human from the ground.':'TRUE',
'The National Sport of India is Hockey.':'TRUE',
'The National fruit of India is Mango.':'TRUE',
'Gandhi was the first Prime Minister of India.':'FALSE',
'No Indian has ever won the Nobel Peace Prize.':'FALSE',
'Andaman and Nicobar islands are closer to Thailand than to mainland India.':'TRUE',
'Christianity is the third biggest religion in India.':'TRUE',
'India does not have any Active Volcanoes.':'FALSE',
'India is larger than Argentina by land area.':'TRUE',
'India is the largest producer of bananas in World.':'TRUE',
'The River Indus originates in India.':'FALSE',
'India has Qualified for the FIFA World Cup.':'TRUE',
'The largest ocean in the world is the Atlantic Ocean':'FALSE',
'The world’s largest island is Greenland.':'TRUE',
'South America has more nations than Africa has?':'FALSE',
'There are 4 lungs in the human body.':'FALSE',
'The human skin regenerates once in two weeks.':'FALSE',
'The liver is the largest internal organ in the human body.':'TRUE',
'The tongue is the only part of the human body with taste buds.':'FALSE'}
#--------------------------------------------------------------------------------------------------------------------------------------------------------
game_run()
