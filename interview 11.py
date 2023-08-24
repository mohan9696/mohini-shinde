#input='India 0123 is my 456 country 12345'
#output='IndiAA `0123 iSS mYY 456 countrYY 12345'

str = 'India 0123 is my 456 country 12345'
def capitalize_last_char(str):
    words = str.split()
    capitalized_words = []
    for word in words:
       if len(word) > 0:
            last_char =word[-1].upper()
            capitalized_word = word[:-1]+last_char+last_char
            capitalized_words.append(capitalized_word)
    else:
            capitalized_words.append(word)
            capitalized_sentence=' '.join(capitalized_words)
    return capitalized_sentence
result=capitalize_last_char(str)
print(result)