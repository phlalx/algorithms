#TAGS trie, data structure

#  Everything happens in the `insert` function, which has to be recursive
#  in order to update the hot_sentences when returning
#
# Take away: store full sentences in trie, and take advantage of isomorphism
# between nodes and sentences
#
# In particular, store nodes in set of hot sentences instead of strings
#

def add(hot_sentences, trie):
    if trie not in hot_sentences:
        hot_sentences.append(trie)
    hot_sentences.sort(key = lambda node: (-node['count'], node['sentence']))
    if len(hot_sentences) == 4:
        hot_sentences.pop()

def insert(trie, sentence, incr_count):
    
    n = len(sentence)
    
    def f(trie, i):
        if i == n:
            count = trie.setdefault('coun   t', 0)
            trie['count'] = count + incr_count
            trie['sentence'] = sentence
            hot_sentences = trie.setdefault('hot_sentences', [])
            add(hot_sentences, trie)
            return hot_sentences
        else:
            trie = trie.setdefault(sentence[i], {})
            hotter_sentences = f(trie, i+1)
            hot_sentences = trie.setdefault('hot_sentences', [])
            for node in hotter_sentences:
                add(hot_sentences, node)
            return hot_sentences

    f(trie, 0)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        trie = {}
        self.trie = trie
        for sentence, count in zip(sentences, times):
            insert(trie, sentence, count)
            
        self.user_sentence = []
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            insert(self.trie, ''.join(self.user_sentence), 1)
            self.user_sentence = []
            return []
        
        self.user_sentence.append(c)
        
        trie = self.trie
        for c in self.user_sentence:
            trie = trie.get(c)
            if trie is None:
                return []
        
        return [ node['sentence'] for node in trie['hot_sentences'] ]
