# Sample Input
  # 3
  # lara@hackerrank.com
  # brian-23@hackerrank.com
  # britts_54@hackerrank.com

# Sample Output
  # ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
  
  
import re 
def fun(s):
        # only 7/10 test passed
    # regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        # only 7/10 test passed
    # regex = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9\.]+)\.([a-zA-Z]{2,5})$"
        # full test pass 
    
        #SOLUTION 1
    # regex = "^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$"
    # if re.search(regex,s):
    #     return True
    # else:
    #     return False
    
        #SOLUTION 2
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
