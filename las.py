# from ZGX
import os
import sys

fpath ='./Track_D_pts_xyzrgbi.txt'
npath ='./New_Track_D_pts_xyzrgbi.txt'
f = open(fpath,'r')
n = open(npath,'a')

txt = f.read()
list = txt.splitlines()
datanumbe = len(list)

xdata,ydata,zdata,newdata,linexyzrgbi = [],[],[],[], []

#find the max data of x/y/z
for d in range(len(list)):
    strd = list[d]
    # print(list[d])
    linexyzrgbi = strd.split(' ')
    # print(linexyzrgbi)
    xdata.append(linexyzrgbi[0])
    ydata.append(linexyzrgbi[1])
    zdata.append(linexyzrgbi[2])
    print("\r Calculate Center point coordinates Progress: {:>3} %".format(d * 100 / len(list)))
    sys.stdout.flush()

xmax,xmin = max(xdata),min(xdata)
ymax,ymin = max(ydata),min(ydata)
zmax,zmin = max(zdata),min(zdata)
xmid = float(xmin) + (float(xmax) - float(xmin))/2
ymid = float(ymin) + (float(ymax) - float(ymin))/2
zmid = float(zmin) + (float(zmax) - float(zmin))/2 #修改

for i in range(len(list)):
    Str = list[i]
    linedata = Str.split(',')
    linedata[0],linedata[1],linedata[2] = round(float(linedata[0])-float(xmid),3),round(float(linedata[1]) -float(ymid),3), round(float(linedata[2]) -float(zmid),3)
    linedata[0] = str(linedata[0])
    linedata[1] = str(linedata[1])
    linedata[2] = str(linedata[2])
    linedata[3],linedata[4],linedata[5],linedata[6] = linedata[6],linedata[3],linedata[4],linedata[5]
    newline = ','.join(linedata) + '\n'
    #print(newline)
    newdata.append(newline)
    print("\rRewrite Newdata to txt Progress: {:>3} %".format( i * 100 / len(list)))
    sys.stdout.flush()

n.writelines(newdata)
f.close()
n.close()
print("\r work done")
