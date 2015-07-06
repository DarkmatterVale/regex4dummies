# Using the get_sentence_information() method

This method is very useful and allows you to get additional information from a pattern. Although the name of this method implies it relates to sentences, it in fact relates to only patterns. There are multiple key values that are returned when you call this method.

```
from regex4dummies import regex4dummies

regex = regex4dummies()

# Displaying all of the "meaning" in these sentences
regex.compare_strings( False, [ "the cat is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat" ] )
sentence_information = regex.get_sentence_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str( sentence.reliability_score )
```

In the above code, a number of commands are run. First, the library is imported and an object instantiated. Next, a number of sentences are used to identify patterns. Finally, the information regarding those sentences (also patterns) is printed out. This information, however, can not only be printed out. All of the information is either integers or strings, so it can be further manipulated and changed. This information can be used for a range of different tasks, some of which including:

- Use of relations/POS values
- Getting reliability score and using that to process data
