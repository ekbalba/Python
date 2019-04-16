# AUTHOR: ekbalba
# DESCRIPTION: A simple script which checks if a given phrase is a Palindrome
# PALINDROME: A word, phrase, or sequence that reads the same backward as forward

sample_phrase = "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!"
# givenPhrase = ""
# phrase = ""

given_phrase = input("\nPlease input a phrase:(Press ENTER to use the sample phrase) ")

def Remove_Special_Characters(phrase):
    string = ''.join(e for e in phrase.lower() if e.isalnum())
    return string

if given_phrase == "" or not given_phrase.strip():
    print("\nThe sample phrase is: {0}".format(sample_phrase))
    string = Remove_Special_Characters(sample_phrase)
else:
    string = Remove_Special_Characters(given_phrase)

if string == string[::-1]:
    print("\nWow!, The phrase is a Palindrome!")
else:
    print("\nSorry, The given phrase is not a Palindrome.")

