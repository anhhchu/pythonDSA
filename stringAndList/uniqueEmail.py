'''
https://leetcode.com/explore/featured/card/google/67/sql-2/3044/

Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
'''

class Solution(object): #only beats 11%
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for email in emails:
            main, domain = email.split('@')
            if '+' in main:
                main = main[:main.index('+')]

            seen.add(main.replace('.','')+'@'+domain)
        
        return len(seen)

sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(sol.numUniqueEmails(emails))



####
class Solution_suboptimal(object): #only beats 11%
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        hashMap = {}
        for email in emails:
            main, domain = email.split('@')
            # process main
            main = [char for char in main]
            i= 0
            while i < len(main):
                if main[i] == '.':
                    main.pop(i)
                elif main[i] == '+':
                    main = main[:i]
                    break
                else:
                    i+=1
            main = ''.join(char for char in main)

            # add main to hashMap
            if main not in hashMap:
                hashMap[main]  = [domain]
            else:
                if domain not in hashMap[main]: 
                    hashMap[main].append(domain)

        output = 0
        for domains in hashMap.values():
            output += len(domains)

        return output


