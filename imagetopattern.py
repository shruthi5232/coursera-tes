from PIL import Image
import numpy
import random

def multiple_uniform(s):
    p=['!','@','#','$','%','^','&','*','(',')','-','+','=']#your pattern is filled with this
    for i in range(s+1):
        p.append(p[i])
    return p
def multiple_random(s):
    p=['!','@','#','$','%','^','&','*','(',')','-','+','=']#your pattern is filled with this
    for i in range(s):
        p.append(p[i])
    return random.choice(p)
def single_uniform(s,c):
    p=f'{c}'#your pattern is filled with this
    return p

def imgtoptn(imgpath,filepath,index,resolution,c='❤️',l=0,u=200):
    ind=int(index)
    lct,uct=int(l),int(u)
    li=[single_uniform,multiple_uniform,multiple_random]
    img=Image.open(imgpath)#your png image location
    s=int(resolution)#output pattern's size
    r=img.resize((s,s)).convert('LA')

    a=numpy.asarray(r)
    #print(a[10][10])
    with open(filepath,'w',encoding='utf-8') as f:
        for i in range(s):
             print('\n',file=f)
             for j in range(s):       
                if lct<a[i][j][0]<uct:
                    if ind==0:
                        print(li[ind](s,c),end='    ',file=f)
                    elif ind==1:
                        print(li[ind](s)[i],end='    ',file=f)
                    else:
                
                        print(li[ind](s),end='    ',file=f)#call your desired function here
                else:
                    print('     ',end='',file=f)
                j+=1
#imgtoptn(r'C:\Users\Home\Pictures\heart.png',r'E:\djangoproject\blog\words.txt')
#imgtoptn(img,r'E:\djangoproject\blog\words.txt')
# if you call multiple_uniform(), use multiple_uniform()[j] for vertical orientation, and use multiple_uniform()[i] for horizotal orientation
#  u can use unicode to print pattern with emoji