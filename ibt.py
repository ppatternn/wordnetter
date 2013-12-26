"""
In-Between Thesaurus
Robert Florance 1.4.2012 - []
"""

import requests, simplejson
import operator, sys

class IBT:
    def __init__(self, api_ver, api_key, api_frmt, query1, query2):
        self.api_ver = api_ver
        self.api_key = api_key
        self.api_frmt = api_frmt
        self.query1 = query1
        self.query2 = query2

    def query_bht(self, word):
        url = "http://words.bighugelabs.com/api/" + self.api_ver + "/" + self.api_key +"/" + word + "/" + self.api_frmt
        r = requests.get(url)
        c = r.content
        data = simplejson.loads(c)
        print "\n ---------------Begin Raw JSON-----------------"
        print simplejson.dumps((data), indent=2)
        print "\n ---------------End Raw JSON-------------------"
        return data

    def parse_adj_synonyms(self, data):
            syn = []
            sim = []
            adj = []
            if "adjective" in data: adj = data["adjective"]
            if "syn" in adj: syn = adj["syn"]
            if "sim" in adj: sim = adj["sim"]
            e = syn + sim #Return a combined list of similars + synonyms
            return e
            
    def find_matches(self, set1, set2):
        matches = []
        for item in set1:
            if item in set2:
                if item not in matches:
                    matches.append(item)
        return matches

    def search_deeper(self, set1, set2):
        bigger_result_set1 = []
        bigger_result_set2 = []
        
        #Find all syn/sims for every result in first search's set
        for item in set1:
            r = self.query_bht(item)
            s = self.parse_adj_synonyms(r)
            bigger_result_set1 += s

        for item in set2:
            r = self.query_bht(item)
            s = self.parse_adj_synonyms(r)
            bigger_result_set2 += s
        
        #look for matches again within this larger set
        matches = self.find_matches(bigger_result_set1, bigger_result_set2)
        return matches

if __name__ == "__main__":
    version = "2"
    api_key = open("apikey.txt", "r").readline().strip()
    print api_key
    result_format = "json" 
    search1 = sys.argv[1]
    search2 = sys.argv[2]

    ibt = IBT(version, api_key, result_format, search1, search2)

    #Get full JSON response from big huge thesaurus
    try:
        results1 = ibt.query_bht(search1)
    except:
        print "error getting matches"
    results2 = ibt.query_bht(search2)
    #Filter out only adjective synonyms
    syns1 = ibt.parse_adj_synonyms(results1)
    syns2 = ibt.parse_adj_synonyms(results2)
    #Find matches between the two filtered lists
    matches = ibt.find_matches(syns1, syns2)
    #Go deeper
    further_matches = ibt.search_deeper(syns1, syns2)
    
    print matches
    print further_matches
    #if len(matches) > 0: print matches, len(matches)
    #else: print "No relations found."














