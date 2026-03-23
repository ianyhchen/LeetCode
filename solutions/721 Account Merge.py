from collections import defaultdict
class DSU:
    def __init__(self):
        # Using a dict to handle dynamic elements (like email strings)
        self.parent = {}

    def find(self, i):
        # If the element is new, it's its own parent
        if i not in self.parent:
            self.parent[i] = i
        # Path Compression: make the node point directly to the root
        # 遞迴會停在 self.parent[i] == i -> parent find
        if self.parent[i] != i:
            #往上遞迴尋找root
            self.parent[i] = self.find(self.parent[i])
        #往下回傳，讓路徑上的子節點都設定同樣的parent
        return self.parent[i] 

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union the two components
            self.parent[root_i] = root_j

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                # Map each email to its corresponding name
                if email not in email_to_name:
                    email_to_name[email] = name
                # Union all emails in the same account to the first email
                dsu.union(first_email, email)

        # Group emails by their root representative
        relationMap = defaultdict(list)       

        # Note: We must iterate through all keys in email_to_name 
        # because those are all the unique emails we've encountered
        for mail in email_to_name:
            root = dsu.find(mail)
            relationMap[root].append(mail)
        
        res = []
        for root, emails in relationMap.items():            
            name = email_to_name[root]
            # Sort emails alphabetically as required by the problem            
            emails.sort()
            # Combine name with the sorted list of emails
            res.append([name] + emails)
        
        return res

                    

            

