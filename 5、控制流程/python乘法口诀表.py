print('--------------乘法口诀表--------------')
print('  ',end = ' ')
for i in range(1,10):
    print(' ',i,end = ' ')
print()
print('--------------------------------------')
for j in range(1,10):
    print(j,'|',end = '')
    for i in range(1,10):
        print(format(i*j,'3d'),end = ' ')
    print()

for s in range(1,3):
    print( )
    
print('***************************乘法口诀表******************************')
for i in range(1,10):
    for k in range(1,10):
        if i <= k:
            print('%dx%d=%2d'%(i,k,i*k),end=' ')
    print()
print('****************************乘法口诀表*****************************')

for m in range(1,3):
    print( )
