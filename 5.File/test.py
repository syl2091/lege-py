file = open('test.txt','r',encoding='utf-8')
print(file.read())


file = open('test.txt','a',encoding='utf-8')
file.write('\n乐哥')
file.close()


