with open ('dataset_24465_4.txt') as f, open('output.txt','w') as w:
    x = f.read()
    x = x.splitlines()[::-1]
    for element in x:
        w.write(element + '\n')
