
class Ledger:
    def __init__(self):
        self.deposit = 0
        self.withdrawal = 0

    def deposit(self, amount, description):
        self.deposit += amount

    def withdraw(self, amount, description):
        self.withdrawal += amount

    def get_balance(self):
        return self.deposit - self.withdrawal

    def transfer(self, amount, description):
        if amount <= self.deposit:
            self.withdraw(amount, "Transfer to " + description)
            self.deposit(amount, "Transfer from " + description)
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

ledger_obj = Ledger()

ledger_operations = [
    ("deposit", ledger_obj.deposit),
    ("withdraw", ledger_obj.withdraw),
    ("get_balance", ledger_obj.get_balance),
    ("transfer", ledger_obj.transfer),
    ("check_funds", ledger_obj.check_funds)
] 

print(********* Welcome to the Ledger *********\n)
 #create a spend chart

def create_spend_chart(categories):
    ans = []
    title = 'Percentage spent by category'
    ans.append(title)
    #print(title)
    y_axis = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|',
              '  0|']
    totalwithdraws = 0
    percentagelist = []
    numlist = []
    bars = []
    for i in categories[0].masterledger:
        totalwithdraws = abs(i) + totalwithdraws # total spent over all categories
    #print(totalwithdraws)
    for i in range(len(categories)):
        total_per_category = int((abs(categories[i].withdraw_amount) / totalwithdraws)* 100)
        if total_per_category < 10:
            total_per_category = 0
        total_per_category = str(total_per_category)
        try:
            if total_per_category[1] != '0':
                total_per_category = int(total_per_category[0] + '0')
        except:
            pass
        percentagelist.append(totalpercategory)
        
    for i in percentagelist:
        num = round(int(i) / 10)
        numlist.append(num) 

    strlen = 3

    for i in range(100, -10, -10): # making the graph y-axis & bars
        if len(str(i)) < strlen:
            diff = strlen - len(str(i))
            line = diff * ' ' + str(i) + '| '
        else:
            line = str(i) + '| '
        #print(line)
        for item in percentagelist:
            percent = int(item)
            if i <= percent:
                line = line + 'o' + '  '
            else:
                line = line + ' '*3
        print(line)
        ans.append(line)


if len(percentagelist) == 1:
    dash = '    ----'
    ans.append(dash)
    #print(dash)
if len(percentagelist) == 2:
    dash = '    -------'
    ans.append(dash)
    #print(dash)
if len(percentagelist) == 3:
    dash = '    ----------'
    ans.append(dash)
    #print(dash)
else:
    dash = '    -------------'
    ans.append(dash)
    #print(dash)

maxlength = 0
verticalprint = []
for i in categories:
    words = i.name
    verticalprint.append(words)
    if len(words) > maxlength:
        maxlength = len(words)
for n, j in enumerate(verticalprint): #finding and replacing list items to make them the same length
    if len(j) < maxlength:
        addspace = maxlength - len(j)
        j = j + ' ' * addspace
        #print(j, len(j))
        verticalprint[n] = j
#print(verticalprint)

for x, y, z in zip(*verticalprint): #vertically prints list on x - axis
    x_axis = x.rjust(6) + y.rjust(3) + z.rjust(3) + '  '
    ans.append(x_axis)
    #print(x.rjust(6), y.rjust(2), z.rjust(2))
    #print(x_axis)

finalsolution = ''
for i in ans:
    finalsolution = finalsolution + '\n' + i
#print(finalsolution.lstrip())
finalsolution = finalsolution.lstrip()
print(finalsolution)
return(finalsolution)   
