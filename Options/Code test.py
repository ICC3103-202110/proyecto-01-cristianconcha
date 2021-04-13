def main():

    def Print_Menu_V2(Turn):
        print("0. Player",Turn+1, "If you whant to defy or counterattack")
        print("1. No action ")
        return int(input())


    

    def Turn():
        pass

    x=0
    while x==0:
        Number_of_Players=int(input("Enter the number of players: "))
        r=1
        List_Players=[]
        while r<Number_of_Players+1:
            List_Players.append(r)
            r+=1
        #print(List_Players)
        if Number_of_Players<3 or Number_of_Players>4:
            print("The number of players must be between 3 and 4")
            continue
        else: 
            x=1
            while True:
                Turn=1
                while Turn<Number_of_Players+1:
                    print("Player ", Turn, " plays \n")
                    print("Player ",Turn, " plays one of his cards\n")
                    #Action=Print_Menu(Number_of_Players,Turn)
                    y=0
                    while y<len(List_Players):
                        Action2=Print_Menu_V2(Turn)
                        if Action2==0:
                            print("Here is suppossed to go the action\n")
                            Turn+=1
                        else:
                            continue
                        y+=1

                    print("player ",Turn," makes action\n")
                 


                Turn+=1
            break
            Turn=0







if __name__=="__main__":
    main()