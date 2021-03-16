class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        ruleKeys=["type","color","name"]
        ruleKeyIndex=ruleKeys.index(ruleKey)
        
        c=0

        for i in range(len(items)):
            if items[i][ruleKeyIndex]==ruleValue:
                c+=1
        return c