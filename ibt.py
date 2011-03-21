"""
The In-Between Thesaurus

Robert Florance 3.21.2011
"""

import urllib2, operator, os, sys


#Basic search function gets synonyms for a single word
#Currently not using the optional 'format' argument, because it defaults to text
def query_bighugethesaurus(version, api_key, word, result_format):

    #Generates a url based on arguments
    url = "http://words.bighugelabs.com/api/" + version + "/" + api_key +"/" + word + "/"
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
        data = response.read()
    except urllib2.HTTPError, e:
        data = e.read()

    return data


#This method takes a string delimited by newlines and pipes, and turns them into a list
def parse_txt_results(data):
    synonyms = []
    
    entries = data.split("\n")
    entries.remove("")          #need to remove the last empty entry
    
    for entry in entries:
        elements = entry.split("|")
        if elements[1] == "syn":            #ignore the antonyms
            word = elements[2]
            synonyms.append(word)          #add the word to the list of synonyms
            
    return synonyms

#This method takes two lists and looks for common entries in each one
def compare_results(list1, list2):
    common_results = []

    for entry in list1:
        if entry in list2:
            print "Found a common entry!"
            common_results.append(entry)

    return common_results


## TESTING ##
version = "2"
api_key = "507ab364c2e364a21c82d0ea6118f4c9"
#word = "fail"
r_format = None

#Get input from the command line
word1 = sys.argv[1]
word2 = sys.argv[2]

print "Searching for words that '" + word1 + "' and '" + word2 + "' have in common..."

results1 = query_bighugethesaurus(version, api_key, word1, r_format)
results2 = query_bighugethesaurus(version, api_key, word2, r_format)

output1 = parse_txt_results(results1)
output2 = parse_txt_results(results2)

common_results = compare_results(output1, output2)

print "Results: "
for result in common_results:
    print result
