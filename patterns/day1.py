#finding 2duplicates
def find_duplicates(l):
        n=set(l)
        if len(l)==len(n):
                return 0
        else:
                return 1
     
find_duplicates(l=[1,2,3,3])