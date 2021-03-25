def revword(word):
    word = word.lower() 
    new_word=word[::-1]
    return str(new_word)



def countword():
    file = open('text.txt')
    file = file.read()

    f= file.find('\n')
    word= file[:f].lower()
    file=revword(file[f:])
    count=1
    for i in file.rsplit():
        if word == i:
            count= count+1
    return count

