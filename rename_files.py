import os

def rename_files():
    # (1) Browse all the file in target folder
    file_list = os.listdir(r"C:\Users\AshwaMegh\Downloads\prank")
    print(file_list)
    working_directory=os.getcwd()
    print("Current working directory"+working_directory)
    os.chdir(r"C:\Users\AshwaMegh\Downloads\prank")
    
    #(2) for each file rename filename
    for file_name in file_list:
        print("Old Filename"+file_name)
        print("New Filename"+file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))
        

    os.chdir(working_directory)    
rename_files()
    
