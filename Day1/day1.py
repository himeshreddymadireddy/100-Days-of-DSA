#finding 2duplicates

class solution(self,l):
    def find_duplicates(self,l):
        return [i for i in l if l.count(i)>1]
    
solution([1,2,3,3])