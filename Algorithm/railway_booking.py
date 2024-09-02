import pandas as p 

def book(df,l,seats_list):
    ans=input("Do you want to book a seat (y/n): ")

    if ans == 'y' or ans == 'Y':
        seat_1=str(input("Enter the seat number you wish to Book: "))
        
        if seat_1 in l:
            print("Procedding to book..")
            l.remove(seat_1)
            seats_list.append(seat_1)
            df = df.replace(seat_1, 'Booked')
            print("you have successfully booked seat no:",seat_1)
            
        else:
            print("The seat is already booked or unavaliable")
            book(df,l,seats_list)

        print(df)
        book(df,l,seats_list)
        
    elif ans == 'n' or ans == 'N':
        print("thank you")
        print("you have booked seat no",seats_list)

    else:
        print("invalid input")
        book(df,l,seats_list)


df = p.DataFrame([['01','02','03','04'],
                   ['05','06','07','08']],
                  columns=['lower', 'middle', 'upper', 'side'],
                  index = ["left", "right"])
print(df)

book(df,['01','02','03','04','05','06','07','08'],[])