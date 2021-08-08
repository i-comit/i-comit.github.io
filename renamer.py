# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os


print("This program replaces the name of all files in a folder and append the iterative value of it at the end. \n")
print("Enter the path of the folder (not the actual file), then enter a name, the program will then change the \nfile name to the one you entered with the order number. \n")
print("BY: Khiem G Luong \n")
path = input("Enter the directory path: ")
name = input("Enter the name for the files: ")
# Function to rename multiple files
def main():

    for count, filename in enumerate(os.listdir(path)):
        dst = name + str(count) + ".jpg"
        srcPath =path + '\\' + filename
        dstPath =path + '\\'  + dst

        # rename() function will
        # rename all the files
        os.rename(srcPath, dstPath)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()