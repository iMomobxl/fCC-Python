def arithmetic_arranger(problems, result=False):
  # check number of problems
  if len(problems) > 5:
      return "Error: Too many problems."

  # create list of problems
  first_operand = list()
  operator = list()
  second_operand = list()
  
  # split() all the problems in first_operand, second_operand, operator
  for problem in problems:
      pieces = problem.split()
      first_operand.append(pieces[0])
      operator.append(pieces[1])
      second_operand.append(pieces[2])
    
  # check the operator only + or -
  if "*" in operator or "/" in operator:
      return "Error: Operator must be '+' or '-'."

  # check if problems only digit (isdigit())
  for index in range(len(first_operand)):
      if not (first_operand[index].isdigit() and second_operand[index].isdigit()):
          return "Error: Numbers must only contain digits."
        
  # check the length of the number (max 4 digits)
  for index in range(len(first_operand)):
      if len(first_operand[index]) > 4 or len(second_operand[index]) > 4:
          return "Error: Numbers cannot be more than four digits."

  first_line = list()
  second_line = list()
  third_line = list()
  fourth_line = list()

  # add all the first_operand in first_line with the necessary space
  for i in range(len(first_operand)):
    if len(first_operand[i]) > len(second_operand[i]):
        first_line.append("  " + first_operand[i])
    else:
        first_line.append(" "*(len(second_operand[i]) - len(first_operand[i])) + "  " + first_operand[i])
      
  # add all the operator + second_operand in second_line with the necessary space
  for i in range(len(second_operand)):
    if len(second_operand[i]) > len(first_operand[i]):
        second_line.append(operator[i] + " " + second_operand[i])
    else:
        second_line.append(operator[i] + " "*(len(first_operand[i]) - len(second_operand[i])) + " " + second_operand[i])

  # add the necessary amount of - in the tird_line
  for i in range(len(first_operand)):
      third_line.append("-"*(max(len(first_operand[i]), len(second_operand[i]))) + "--")
  # if result=True make the calculation
  space = "    "
  if result:
      for i in range(len(first_operand)):
          if operator[i] == "+":
              answer = str(int(first_operand[i]) + int(second_operand[i]))
          elif operator[i] == "-":
              answer = str(int(first_operand[i]) - int(second_operand[i]))
          # check the len() of answer and add the necessary space
          if len(answer) > max(len(first_operand[i]), len(second_operand[i])):
              fourth_line.append(" " + answer)
          else:
              fourth_line.append(" "*(max(len(first_operand[i]), len(second_operand[i])) - len(answer) + 2) + answer)
      # put all the 4 lines in arranged_problems (string) with join()
      arranged_problems = space.join(first_line) + "\n" + space.join(second_line) + "\n" + space.join(third_line) + "\n" + space.join(fourth_line)
  # put all the 3 lines in arranged_problems (string) with join()
  else:
      arranged_problems = space.join(first_line) + "\n" + space.join(second_line) + "\n" + space.join(third_line)
  return arranged_problems