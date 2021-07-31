# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os
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