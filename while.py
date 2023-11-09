number = 1
secondNumber = 1
thirdNumber = 1
lastNumber = 1

while number < 6:
  print(number)
  number += 1

while secondNumber < 6:
  print(secondNumber)
  if secondNumber == 3: break
  secondNumber += 1

while thirdNumber < 6:
  thirdNumber += 1
  if thirdNumber == 3: continue
  print(thirdNumber)

while lastNumber < 6:
  print(lastNumber)
  lastNumber += 1
else:
  print("lastNumber var is no longer less than 6.")