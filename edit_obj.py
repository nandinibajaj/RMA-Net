from io import StringIO
import os
  
cnt=0
arr=[]

fp=open('/home/nandini/Downloads/RMA-Net-main/lander/centered_farthestObj_surface2055_vertices.obj','r')#take ply or obj input
lines = fp.readlines()
n=len(lines)
arr
for i in range(0,len(lines)):
    lines[i] = lines[i].strip()
    if(len(lines[i]) !=0):
        #if(lines[i][0]=='v' and lines[i][1]==' '): #to extract only vertices
        cnt+=1
        arr.append('v '+lines[i]+" 0 0 1\n") #format the vertices
        #arr.append(lines[i][2:-6]+"\n") ## remove formatting

print(cnt) #no. of vertices
f=open('/home/nandini/Downloads/RMA-Net-main/lander/centered_farthestObj_surface2055_vertices.obj','w') #edited file path

f.writelines(arr) #save edited file
f.close()

