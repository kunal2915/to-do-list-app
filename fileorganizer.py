import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"file  {filename} created")
    except FileExistsError:
        print(f"file {filename} already exists")
    except Exception as E:
        print("An error occurred")

def view_all_files():
    files=os.listdir()
    if not files:
        print("No files in the directory")
    else:
        print("files in the directory")
        for file in files:
            print(files)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as E:
        print("an error occured")

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
        print(f"content of '{filename}':{content}")
    except FileNotFoundError:
        print(f"{filename} not found")
    except Exception as E:
        print(" an error occured")

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content=input("enter thing you want to add")
            f.write(content+"\n")
            print(f"content of '{filename}':{content}")
            print(f"content added to {filename} sucessfully")
    except FileNotFoundError:
        print("file not exist")
    except Exception as e:
        print("an error occured") 

def main():
    while True:
        print("1.create file")
        print("2.view all files")
        print("3.delete file")
        print("4.read file")
        print("5.edit file")
        print("6.exit")

        choice =int(input("enter your choice(1-6):"))

        if choice==1:
            filename=input("enter file name you want to create:")
            create_file(filename)
        elif choice==2:
            view_all_files()
        elif choice==3:
            filename=input("enter file name you want to delete:")
            delete_file(filename)
        elif choice==4:
            filename=input("enter file name you want to read:")
            read_file(filename)
        elif choice==5:
            filename=input("enter file name you want to edit:")
            edit_file(filename)
        elif choice==6:
            print("good bye --- closing the program---!")
            break
        else:
            print("invalid input")

if __name__ == "__main__":
    main()
