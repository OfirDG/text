def revword(word):
    word = word.lower() 
    new_word=word[::-1]
    return str(new_word)



def countword():
    file = open('text.txt')
    file = file.read()

    f= file.find('\n')
    word= file[:f]
    file1=' '+ file[f+1:]
    file1=revword(file1)
    count=0
    for i in file1.rsplit():
        if word == i:
            count= count+1
    return count

 