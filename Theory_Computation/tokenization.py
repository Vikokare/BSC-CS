## -------------------------------------------------------------Tokenization without nltk
paragraph = "This is a sample text for testing of program / script . We can get a brief understanding of how tokenization is done through a real world example"

sentence = paragraph.split('.')
print(sentence)

word = paragraph.split()
print(word)


## -------------------------------------------------------------Regular expression
import re

for phone in ['958687345', '7598783526', '9183649554', '6764345637', '91783693'] :
    valid = re.findall('(^(\+91)?((75)|(95)|(91))\d{8}$)', phone)
    result = f'{phone} : Accepted' if valid else f'{phone} : Error'
    print(result)

for email in ['vaibhav@gmail.com', 'kokare@gmailcom', 'vaibhavAPI123@outlook.com', 'kad1239gmail.com'] :
    valid = re.findall('(^([\w\d]+)(\@)((gmail)|(outlook)|(hotmail))(\.com)$)', email)
    result = f'{email} : Accepted' if valid else f'{email} : Error'
    print(result)
