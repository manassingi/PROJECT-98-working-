def swapFileData():
    file1 = input("Enter the first file")
    file2 = input("Enter the second file")
    with open (file1,'r') as a:
        data_a = a.read()
    with open (file2,'r') as b:
        data_b = b.read()      
    with open (file2,'w') as b:
        a.write(data_a)
    with open (file1,'w') as a:
        b.write(data_b)
       
swapFileData()             
