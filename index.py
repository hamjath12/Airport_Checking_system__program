def main ():
    print("***welcome airport***")
    print("1)ticket checking\n2)covid-19 ckecking\n3)imigration checking\n4)bag weight checking\n5)boarding pass ")
main ()

def air_port ():
    your_ticket = int(input("type your ticket date :"))
    if your_ticket==10:
        print(f"-> your date {your_ticket} is valid go to inside the airport")
        
        print("-> you go to covid-19 checking")
        your_opinion=input("enter go to covid checking yes/no :") 
        if your_opinion=="yes":
            print("go to take covid-19 test")
            your_result=input("enter your covid-19 result positive/negative :")
            if your_result=="positive" :
                print(f"your result {your_result} eligible for flying")
                print("-> go to imigration ckecking")
                
                print("-> imigration -> give your 3 document's")
                my_document=["ticket","passport","visa"]
                i=1
                while i<4:
                    your_document=input("enter your doument's "+str(i+0))
                    if your_document in my_document :
                        print(f"your {your_document} are identify ")
                        i=i+1
                
                print("-> go to bag weight checking <=25 kg only allow")
                your_bag=int(input("enter your bag weight:"))        
                if your_bag<=25 :
                    print(f"your luggage is {your_bag} kg ,so allow")
                    
                    print("-> go to next boarding pass")
                    print("-> name , age , seat no")
                    t_ticket=("ham", "23" , "6a")            
                    i=1
                    while i<4   :            
                        your_t=input(f"enter ticket deatil :"+str(i+0))
                        if your_t in t_ticket :
                            print(f"correct your {your_t} detail,"+str(i+0))
                            i=i+1
                        else :
                            print(f"check the detail,"+str(i+0))
                    print("***finish your verification***")    
            else:
                print("go to hospital....!!!")
        else:
            print("not enter in aeroplane...!")
    else :
        print(f"your ticket date is invalid pls check date : {your_ticket} ")
air_port()
