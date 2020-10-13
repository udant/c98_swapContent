def swapContents1(content, filename):
    file=open(filename,"w")
    file.writelines(content)
   
def getContents():
    filename1=input("enter the file ")
    file1=open(filename1,"r")
    cnt=file1.readlines()
    return cnt,filename1

content1,filename1 = getContents()
content2,filename2 = getContents()    

swapContents1(content1,filename2)
swapContents1(content2,filename1)
