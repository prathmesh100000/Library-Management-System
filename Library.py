class Library:
    l = [{"Name" : "Sapiens","Author" : "Yuval Noah Harari","Price" : 500,"ISBN" : 9780099590088},
        {"Name" : "Atomic Habits","Author" : "James Clear","Price" : 400,"ISBN" : 9781847941831},
        {"Name" : "The Alchemist","Author" : "Paulo coelho","Price" : 300,"ISBN" : 9780062315007},
        {"Name" : "Ikigai","Author" : "Hector Garcia","Price" : 350,"ISBN" : 9780143130727},
        {"Name" : "The Power of Now","Author" : "Eckhart Tolle","Price" : 400,"ISBN" : 9781577314806},
        {"Name" : "The Subtle Art of Not Giving Up","Author" : "Mark Manson","Price" : 350,"ISBN" : 9780062457714},
        {"Name" : "Thinking Fast and Slow","Author" : "Daniel Kahneman","Price" : 500,"ISBN" : 9780374533557},
        {"Name" : "Becoming","Author" : "Michelle Obama","Price" : 600,"ISBN" : 9781524763138},
        {"Name" : "Educated","Author" : "Tara Westover","Price" : 400,"ISBN" : 9780399590504},
        {"Name" : "The Four Agreements","Author" : "Don Miguel Ruiz","Price" : 300,"ISBN" : 9781878424310}]

    def __init__(self,name="",id=0,phno=0,email=""):
        self.name = name
        self.id = id
        self.phno = phno
        self.email = email

    def disp(see):
        print("\n----------------------------------")
        print(f"\nName of the Student : {see.name}")
        print(f"\nId of the Student : {see.id}")
        print(f"\nPhone No. of the Student : {see.phno}")
        print(f"\nMail of the Student : {see.email}")
        print("\n----------------------------------")

    @classmethod
    def books(see):
        print()
        print(f"These are some books present in my library")
        i = 0
        while i < len(see.l):
            print()
            print("Book Name - Author's Name - Price - ISBN Code")
            print(f"{i+1}) {see.l[i]["Name"]} - {see.l[i]["Author"]}  {see.l[i]["Price"]}/-  {see.l[i]["ISBN"]}")
            i+=1

    def cart(acc):
        cart = {}
        i = 0
        while i >= 0:
            a = int(input("\n1. Add\n2. Remove\n3. Back\nEnter the no. from above :  "))
            if a == 1:
                j = 0
                while j >= 0:
                    h = 0
                    while h < len(acc.l):
                        print()
                        print(f"{h+1}) {acc.l[h]["Name"]}")
                        h+=1
                    b = int(input("\nEnter book no. which you want to add to your cart : "))
                    cart[b] = acc.l[b-1]["Name"]
                    print(cart)
                    j+=1
                    break
            elif a == 2:
                print(cart)
                c = int(input("\nEnter the Book no. you want to Remove : "))
                if c in cart:
                    cart.pop(c)
                    print(cart)
                else:
                    print("\nYour Book is not in the cart")
            elif a == 3:
                print("Bye Bye _____ (: ")
                break
            else:
                print("\n------Please enter the correct number")
                i+=1
                
        
O1 = Library(name=input("Enter your name : "),id=int(input("Enter your id no. : ")),phno=int(input("Enter your phone no. : ")),email=input("Enter your email-id : "))
O1.disp()
O1.books()
O1.cart()