class Category:
    
    def __init__(self, name : str):
        
        # Building the constructor...
        self.ledger = []
        self.name = name
        self.__budget = 0.0
    
    # Methods...
    
    def get_balance(self):
        
        return self.__budget
    
    def check_funds(self, amount):

        if self.__budget >= amount:
            return True

        return False
    
    def deposit(self, amount, description = ""):

        self.__budget += amount

        self.ledger.append({"amount" : amount, "description" : description})
    
    def withdraw(self, amount, description = ""):
        
        if self.check_funds(amount):
            self.ledger.append({ "amount": amount * -1, "description" : description})
            self.__budget -= amount
            return True
        return False
    
    def transfer(self, amount, another):
        
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {another.name}")
            another.deposit(amount, f"Transfer from {self.name}")
            
            return True

        return False
    
    def __str__(self):

        title = f"{self.name:*^30}" + "\n"
        body = ""
        
        for items in self.ledger:
            body += f"{items['description'][0:23]:23}" + f"{items['amount']:>7.2f}" + "\n"

        out = title + body + "Total: " + str(self.__budget)
        
        return out
    
def create_spend_chart(lcats):
    
    # Initializing variables
    amts = list()
    title = "Percentage spent by category\n"
    layer = ""
    lenLcats = len(lcats) * 3
    names = ""
    midline = f"    {'-' + '-' * lenLcats}\n"
    
    # Obtaining the amounts
    for cat in lcats:
        amt = 0
        for items in cat.ledger:
            if items["amount"] < 0:
                amt += items["amount"]
        amts.append(amt)
    
    # Rounding the amount
    for i,amount in enumerate(amts):
        a = amount * -1
        b = a - int(a)
        if b >= 0.5:
            amts[i] = int(a+1)
            
        else:
            amts[i] = int(a)
    
    for i,amount in enumerate(amts):
        
        lent = len(str(amount))-1
        amount = str(amount)
        
        if amount[lent:] != 0:
            amts[i] = int(amount) - int(amount[lent:])
        else: 
            amts[i] = int(amount)

    # Making the graph
    for i in range(100,-10,-10):
        layer += f"{i:>3}|"
        for amount in amts:
            if amount > i:
                layer += " o "
            else:
                layer += "   "
        layer += "\n"
    
    descs = [cat.name for cat in lcats]
    max_len = max([len(desc) for desc in descs])
    final = ""
    for i in range(max_len-1):
        final += "     "
        for j in range(len(descs)):
            final += f"{descs[j][i:i+1]:<3}"
        final += "\n"
            
    
    return title + layer + midline + final