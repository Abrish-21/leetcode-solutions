class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_dict = defaultdict(list)
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            transaction_dict[name].append([time, amount, city])
        invalid = []
    
        def isValid(name, time, amount, city):
            if int(amount) > 1000:
                return False
            for otime, oamount, ocity in transaction_dict[name]:
                if abs(int(otime) - int(time)) <= 60  and city != ocity:
                    return False
            return True
        
        for transaction in transactions:
            name, time, amount, city  = transaction.split(',')
            if not isValid(name, time, amount, city):
                invalid.append(transaction)
        return invalid

        






        