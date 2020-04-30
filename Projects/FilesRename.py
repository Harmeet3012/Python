from os import *

# Taking Path from the user as input
folder_path = input("Enter Path :") # Dummy Path -> "E:\Python"

# Checking if the path exists or not -> path.isdir(folder_path)
if not path.isdir(folder_path):
    print("The path is Invalid")
    exit(0)

# using listdir(folder_path) function, listing all the files and assigning it to anime_list
anime_list=listdir(folder_path)

# Enter the format you want to convert your files to
formatting = input("Enter the format you want to convert it to :")
if formatting not in ("jpg","jpeg","pdf","mp4","mp3"):
    print("Invalid Format")
    exit(0)

# Enterring Starting and Ending episode and converting it into a numerical list format
i=int(input("Enter the starting Episode"))
n=int(input("Enter the ending Episode"))
all = []
for i in range(i,n+1):
    all.append(i)

# print(all)

# Logic for the episodes that needs to be excluded
drop = []
ch = input("Want to drop any episodes(y/n)")
if ch == 'y':
    while ch=='y':
        drop_ep = int(input("Enter Episode Number"))
        if drop_ep < 0:
            print("Invalid Episode to be dropped")
            exit(0)
        drop.append(drop_ep)
        ch = input("Want to drop more episodes(y/n)")

#print(drop)

#keeping only those episodes that needs to be included in the naming process
keep = list(set(all) - set(drop))
#print(keep)

# logic for renaming
ind=0
for e in keep:
    source = folder_path+"\\"+anime_list[ind]
    print(source)
    destination = folder_path+"\\"+str(e)+"."+formatting
    print(destination)
    rename(source,destination)
    print("File Renamed Successfully\n------------------------------")
    ind+=1

print("OPERATION COMPLETE")







