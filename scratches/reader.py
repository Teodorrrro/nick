f = open('example.txt', 'r')
line = f.readline()

'''
Fedya\nKak delaa?\n- ni che tak
'''

while line != '':
    without_n = line.replace('\n', '')
    print(without_n)
    line = f.readline()
f.close()


f = open('example2.txt', 'a')
for i in range(1,10):
    f.write('Normas\n')
f.close()