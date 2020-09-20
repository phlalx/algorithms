#TAGS sort

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(log):
            ident, *tokens = log.split()
            if tokens[0].isdigit():
                return (1,)
            else:
                return (0, tokens, ident)
        logs.sort(key=key)
        return logs
        
