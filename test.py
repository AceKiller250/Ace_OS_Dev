import dropbox


dbx = dropbox.Dropbox('sl.BNXrKBZspW5v1uVCqDNkWQzjKmimdqucR4bYSlCZPDem26-50TRxPBjXpzEEqj0LUPfZh8GAFbX2yImKGUpd39SAqykI4lpdeQvR1sKqfvfMS3VdARYIHHJfaotgWT6spUfHLOk')


for entry in dbx.files_list_folder('').entries:
    print(entry.name)

dbx.files_upload("TestFiles", "/Users/peytonfollosco/Documents/GitHub/Ace_OS_Dev/hello.txt")

