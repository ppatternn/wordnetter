"""
wordlink
Robert Florance 12.26.13
"""

import requests
import simplejson
import operator
import sys


class BHTQuery:
    def __init__(self, api_ver, api_key, api_frmt):
        self.api_ver = api_ver
        self.api_key = api_key
        self.api_frmt = api_frmt
        self.base_url = "http://words.bighugelabs.com/api"

    def query_word(self, word):
        url = self.base_url + "/" + self.api_ver + "/" + self.api_key + "/" + word + "/" + self.api_frmt
        resp = requests.get(url).content
        if resp:
            json = simplejson.loads(resp)
            return json
        else:
            return None

    @staticmethod
    def clean_results(jsonresult):
        result = []
        #TODO: disambiguate nouns, adjectives, and verbs
        if "adjective" in jsonresult:
            adj_result = jsonresult["adjective"]
        if "syn" in adj_result:
            result += adj_result["syn"]
        if "sim" in adj_result:
            result += adj_result["sim"]
        if "rel" in adj_result:
            result += adj_result["rel"]
        return result


class WordLink:
    @staticmethod
    def find_matches(set1, set2):
        matches = []
        for item in set1:
            if item in set2:
                if item not in matches:
                    matches.append(item)
        return matches

if __name__ == "__main__":
    api_ver = "2"
    api_key = open("apikey.txt", "r").readline().strip()
    api_frmt = "json"
    bq = BHTQuery(api_ver, api_key, api_frmt)

    print "Find common links between two words:"
    word1 = raw_input("Enter first word:")
    word2 = raw_input("Enter second word:")

    jsonresult1 = bq.query_word(word1)
    jsonresult2 = bq.query_word(word2)

    if jsonresult1 is not None and jsonresult2 is not None:
        #print simplejson.dumps(jsonresult1, indent=2)
        res1 = BHTQuery.clean_results(jsonresult1)
        res2 = BHTQuery.clean_results(jsonresult2)

        links = WordLink.find_matches(res1, res2)
        print "First word siblings: " + res1
        print "Second word siblings: " + res2
        print "Links: " + links
    else:
        print "Error finding matches... words may be too dissimilar, not found in thesaurus, or misspelled."





