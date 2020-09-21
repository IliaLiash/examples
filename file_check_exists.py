import os.path
file_name = input()

if os.path.isfile(file_name):
    with open (file_name) as f:
        text = f.read()
        print("CONTENT:")
        print(text)
        
elif os.path.exists(file_name) == True and os.path.isfile(file_name) == False:
    print("ERROR:")
    print("Это каталог, а не файл")  
        
elif os.path.isfile(file_name) == False:
    print("ERROR:")
    print("Файл не существует")  