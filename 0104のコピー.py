'''

cubed_project=open('/Users/hiroyuki/Documents/tstp/cubed_project','w',encoding='utf-8')
cubed_project.write('いけるかなー？どうだろう' *100)
cubed_project.close()



with open('謎ファイル','w',encoding='utf-8')as a:
    a.write('かんたんだけど組み合わせが難しいーーー')


with open('謎ファイル','r',encoding='utf-8')as a:
    print(a.read()*10)




list=[]
with open('謎ファイル','r',encoding='utf-8')as a:
    list.append(a.read())

print(list)





#うごかない　意味不明 うごいた

import csv
with open('謎ファイル２.csv','w',newline='')as a:
    w = csv.writer(a,delimiter=',')
    w.writerow(['one','two','three'])
    w.writerow(['four','five','six'])


import csv
with open('謎ファイル２.csv','r')as a:
    r= csv.reader(a,delimiter=',')
    for row in r:
        print(','.join(row))


'''
import csv
with open('/Users/hiroyuki/Documents/tstp/cubed_project謎ファイル４','w',encoding='utf-8')as a:
    w = csv.writer(a,delimiter='|')
    w.writerow(['〈連番〉','〈不満の内容〉','〈対応〉'])
    w.writerow([1,'求められていない状況がつらい','高給なバイトだと割り切ろう'])
    w.writerow([2,'プログラミングで転職できるか不安','もし無理でも勉強は必要'])
    w.writerow([3,'奥さんも不安だろうこと','俺が頑張るしかない'])
    w.writerow([4,'このペースでどこまで行けるだろうか','限界など考えずひたすら進もう'])


import csv
with open('/Users/hiroyuki/Documents/tstp/cubed_project謎ファイル４.csv','r')as f:
    yomutamenohensuu=csv.reader(f,delimiter='|')
    for uekarasitamade in yomutamenohensuu:
        print(','.join(uekarasitamade))
    
#動いたけど未習得↑






