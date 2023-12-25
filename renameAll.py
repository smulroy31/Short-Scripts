# Function to replace words in files names in a folder
import os, re
def main():
    i = 0

    # Ask user where the PDFs are
    dirname = os.path.dirname(__file__)
    path1 = input('Folder path to files: ')
    path = os.path.join(dirname, path1)
    # Sets the scripts working directory to the location of the PDFs
    os.chdir(path)
    
    filetype = input('Enter file extention here: ')
    remove = input('Enter word to remove: ')
    if remove == "":
        remove = "\[.*?\]|\(.*?\)|\".*?\"|.*/.| "
    replace = input('Enter word to replace: ')

    filenames = []
    filenamesOld = []
    for filename in os.listdir(path):
        if filetype not in filename:
            continue
        filenamesOld.append(filename)
        filename = re.sub(remove, replace, filename)
        filenames.append(filename)
        print(filename)
    make_change = input("Accept renaming method? ([y]/n): ")
    if(make_change == "" or make_change == "y"):
        for fi, filename in enumerate(filenames):
            os.rename(filenamesOld[fi], filenames[fi])

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()