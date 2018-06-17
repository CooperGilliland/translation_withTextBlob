from textblob import TextBlob

'''
This function takes in a string and translates it to english
If english is already the language, the original is returned 
'''


def Translate(text):
    analysis = TextBlob(text)  # create text blob of input
    langCode = analysis.detect_language()  # attempt to detect the language
    if langCode != 'en':  # avoid an exception being raised by checking for a mismatch between languages
        transText = analysis.translate(from_lang=langCode, to='en')  # translate the input to english
        return transText
    else:  # if the text is already the target language, return it unchanged
        return text


'''
This function allows multiple line to be input at once, the purpose for this is so that 
multiple lines of input can be cut from a source and pasted into this program as a single set
'''


def GetInput():
    inputList = []
    print("Awaiting Input ->")
    while True:  # loop until a break is triggered
        inp = input()  # collect a line of user input
        if not inp:  # break if the input is empty
            break
        inputList.append(inp)  # add the line of user input to the list
    return inputList  # return the list of user inputs


if __name__ == '__main__':
    try:
        print("This simple translator will take any number of lines and translate them to English "
              "\nOnce you have finished inputting the lines for translation, press the enter key twice.")
        i = 0
        inList = GetInput()  # Get the user input
        while i < len(inList):  # iterate through each object in the input list
            output = Translate(inList[i])  # translate the current list object to english
            print(output)  # output the translated text
            i += 1  # move the list index forward
    except Exception as e:
        print("Terminating program")