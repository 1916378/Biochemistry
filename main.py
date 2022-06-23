# Variables
item_list_kgmol = []
item_list_mgml = []
unitconv = 1000

# Overall concentration and volume
print("Molar ratio: 1:1:1:...")

mgmlA = float(input("Overall concentration (mg/ml): "))
ul = float(input("Overall volume (ul): "))

items = int(input("How many items?: "))

# Molecular Weight and concentration
for i in range(items):
  answer = float(input("Molecular Weight of Item " + str(i + 1) + " (kg/mol): "))
  item_list_kgmol.append(answer)

for i in range(items):
  answer = float(input("Concentration of Item " + str(i + 1) + " (kg/mol): "))
  item_list_mgml.append(answer)

# Calculating umol/L
item_list_umolL_temp = [i / j for i, j in zip(item_list_mgml,item_list_kgmol)]
item_list_umolL = [i * 1000 for i in item_list_umolL_temp]

# Solving ul1
item_list_ultemp = []  
item_list_ul = []

i = 1
while i < items:
  ultemp = (item_list_umolL[0] / (item_list_umolL[i]) * item_list_mgml[i])
  item_list_ultemp.append(ultemp)
  i += 1

ul1 = ul * mgmlA / (item_list_mgml[0] + sum(item_list_ultemp))
item_list_ul.append(ul1)

# Solving ul >1
i = 1
while i < items:
  item_list_ul.append(ul1 * item_list_umolL[0] / item_list_umolL[i])
  i += 1

# Print results
num = 1
for item in item_list_ul:
  print("Item", num, "amount (ul): " , round(item, 2))
  num += 1

# Print buffer
Buffer = ul - sum(item_list_ul)
print("Buffer amount (ul): " , round(Buffer, 2))