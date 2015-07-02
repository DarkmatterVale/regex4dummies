# Importing the regex4dummies library
from regex4dummies import regex4dummies

# Identifying test strings
strings = [ "This is the first string.", "This is the second test string." ]

# Creating regex object & test strings
regex = regex4dummies()

# Display the version of regex4dummies you are using
print regex.__version__

# Identifying literal patterns in strings
print regex.compare_strings( '', True, strings )

# Identifying semantic patterns in strings using the nltk parser
print regex.compare_strings( 'nltk', False, strings )

# To use the other parsers, replace the above line of code with either of the following:
# print regex.compare_strings( 'pattern', False, strings )
# print regex.compare_strings( 'nlpnet', False, strings )

# Printing pattern information
pattern_information = regex.get_sentence_information()
  for objects in pattern_information:
      print "[ Pattern ]          : " + objects.pattern
      print "[ Subject ]          : " + objects.subject
      print "[ Verb ]             : " + objects.verb
      print "[ Object ]           : " + objects.object[0]
      print "[ Reliability Score ]: " + str( objects.reliability_score )
