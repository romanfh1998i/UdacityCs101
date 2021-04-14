word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###
is_palindrome =word.find(word[::-1])

# TESTING
print is_palindrome
# >>> 0  # outcome if word == "madam"