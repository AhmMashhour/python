 number = 5
 line = [" "," "," ", " ", " "]
 for i in range(1, number+1):
     line[-i] = "*"
     print(line)

 for i in range(5):
     print(" "(5 -i)+'' * i)

 for i in range(6):
     print(" "(6 -i)+'' * i)
