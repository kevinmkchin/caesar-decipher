# Caesar Cipher Decrypter
# by Kevin Chin 11/11/2018
# Decipher Caesar ciphers by using 1000 most common English words
# Only single letter words in English are "a" and "I". Narrow down
# possible answers to 2 by using this rule.

# English Alphabet ASCII Values are [97, 122]
# ASCII values for uppercase letters are 32 less than ASCII values for lowercase


# the TEXT to DECIPHER
with open('cipher.txt', mode='r') as raw_cipher:
    cipher = list(raw_cipher.read())



# words is a list containing 1000 most common English words
with open('1-1000.txt', mode='r') as raw_words:
    words = raw_words.read().split("\n")


# turn uppercase letters to lowercase
for c, value in enumerate(cipher):
    if ord(value) in range(65,91): # i.e. uppercase letters
        cipher[c] = chr(ord(value) + 32)


# empty list for outcomes/answers
outcomes = []
# boolean for whether cipher contains single letters
singles = False
# narrow down to 2 possible keys if single letters exist
for i in "".join(cipher).split(" "):
    if len(i) is 1 and 97 <= ord(i) <= 122: # if a word is only 1 letter and between a-z
        key1 = ord(i) - 97
        key2 = ord(i) - 105
        singleKeys = [key1, key2]
        singles = True
        break


# function to map each character with shift in ascii value
def shift(char):
    if 97 <= ord(char) <= 122:        # only decrypt if character is a letter
        newChar = ord(char) - key
        if newChar < 97:
            return chr(newChar + 26)  # clamp newChar to >= 97
        elif newChar > 122:
            return chr(newChar - 26)  # clamp newChar to <= 122
        return chr(newChar)
    else:
        return char

def tryKeys():
    # can't include for loop in the tryKeys() function because of shift()'s reference to key
    potentialAnswer = "".join(list(map(shift, cipher))).split(" ")
    outcomes.append(potentialAnswer)

# create a list of possible answers
if singles is True:
    for key in singleKeys:
        tryKeys()
else:
    for key in range(1,26):
        tryKeys()


# empty list for frequency of common words for each outcome/answer
frequencies = []
# find the frequency of common words for each outcome/answer
for oc in outcomes:
    count = 0
    for w in oc:
        if w in words:
            count += 1
    frequencies.append(count)


# find index of answer with most common words
goodAnswerValue = max(frequencies)
goodAnswerIndex = frequencies.index(goodAnswerValue)
# pick the answer with most common words
rightOutcome = outcomes[goodAnswerIndex]
# turn into one string
decryptedMessage = " ".join(rightOutcome)

# Print the decrypted Message
print(decryptedMessage)