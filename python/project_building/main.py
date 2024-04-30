from ticketbooking import movie_ticket

class main:
    def execute(self, choice):
        if choice == 1:
            print('SHow the Seats*******')
            movie_ticket_obj.show_seats()
        if choice == 2:
            print('SHow the tickets*******')
            movie_ticket_obj.buy_tickets()
        if choice == 3:
            print('**Statistics*******')
            movie_ticket_obj.statistics()
        if choice == 4:
            print('***Show the booked tickets*******')
            movie_ticket_obj.user_info()
        if choice == 0:
            print('** Thanks visit again*******')
            exit()

if __name__ == '__main__':
    rows = int(input("\nEnter the number of rows : "))
    columns = int(input("Enter the number of seats in each row : "))
    movie_ticket_obj = movie_ticket(rows,columns)
    obj = main()
    while True:
        print("\n1. Show the seats")
        print("2. Buy the ticket")
        print("3. Statistics")
        print("4. Show booked Tickets User Info")
        print("0. Exit\n")
        choice = int(input("Enter the choice : "))
        li = [1,2,3,4,0]
        if choice not in li:
            print("Invalid choice")
            continue
        obj.execute(choice)
    


