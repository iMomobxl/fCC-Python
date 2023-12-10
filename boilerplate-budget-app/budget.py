class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    text = self.name.center(30, "*") + "\n"
    for item in self.ledger:
      text += item['description'][:23]
      text += " " * (30 - len(item['description'][:23]) - len(str("{:.2f}".format(item['amount'])[:7])))
      text += "{:.2f}".format(item['amount'])[:7]
      text += "\n"
    text += "Total: " + str(self.get_balance())
    return text

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    #print(self.ledger)

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      #print(self.ledger)
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_category.name)
      budget_category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False


  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else : 
      return True


def create_spend_chart(categories):
  # result is our output string
  result = "Percentage spent by category"

  # sum of all widthdraws in each category
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  #print(spend)

  # total sum of all widthdraws
  total = sum(spend)
  #print(total)

  # percentage of each category
  percentage = []
  for i in spend:
    percentage.append(i / total * 100)
  #print(percentage)
  #print(sum(percentage))

  # create the percentage chart
  for i in range(100, -1, -10):
    result += "\n" + str(i).rjust(3," ") + "|"
    for j in percentage:
      if j > i:
        result += " o "
      else:
        result += "   "
    result += " "

  # add the dashes line
  result += "\n" + "    " + "-" * (1 + len(categories) * 3)

  # check the max length of the category name
  len_cat = []
  for category in categories:
    len_cat.append(len(category.name))
  len_max = max(len_cat)
  #print(len_max)

  # add the category name
  for i in range(len_max):
    result += "\n" + "    "
    for category in categories:
      if len(category.name) > i:
        result += " " + category.name[i] + " "
      else:
        result += "   "
    result += " "

  return result