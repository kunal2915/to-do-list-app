#empty dictionary
contacts={}

while True:
    print("\ncontact book app")
    print("1.create contact")
    print("2.view contact")
    print("3.update contact")
    print("4.delete contact")
    print("5.search contact")
    print("6.count contact")
    print("7.exit")

    Choice=int(input("enter your choice:"))

    if Choice==1:
         name=input("enter your new contact :")
         if name in contacts:
              print(f" contact name {name} is already exist!")
         else:
              age=input("enter age:") 
              email=input("enter email:")
              mobile=input("enter mobile:")
              contacts[name]={'age':int(age),'email':email,'mobile':mobile}
              print(f"contact name { name} has been created successfully")

    elif Choice==2:
         name=input("enter contact name you want to view:")
         if name in contacts:
              contact=contacts[name]
              print(f"Name:{name},Age:{age},Mobile:{mobile}")
         else:
              print("contact not found")
    
    elif Choice==3:
         name=input("enter name to update contact:")
         if name in contacts:
              age=input("enter updated age:") 
              email=input("enter updated email:")
              mobile=input("enter updated mobile")
              contacts[name]={'age':int(age),'email':email,'mobile':mobile}
              print(f"Name:{name},Age:{age},Mobile:{mobile}")
              print("name has updated")
         else:
              print("contact not found")
    
    elif Choice==4:
         name=input("enter name you want to delete:")
         if name in contacts:
              del contacts[name]
              print(f"contact name {name} has been deleted successfully")
         else:
              print(f"contact name {name} not found")
    
    elif Choice==5:
         search=input("enter contact you want to search:")
         found=False
         for name , contact in contacts.items():
              if search.lower() in name.lower():
                   print(f"found -- name:{name}, age:{age},mobile:{mobile}")
                   found=True
         if not found:
              print("no contact found with this name")
    
    elif Choice==6:
         print(f"total contacts in your book:{len(contacts)}")

    elif Choice==7:
         print("good bye --------------closing the app ------------")
         break     
    else:
         print("invalid input")        

    
