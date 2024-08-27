n = input()
ip_list = input().split()

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
indexOfList = []
result = []


for i in ip_list:
   indexOfList.append(alphabets.rfind(i[:1].upper()))

print(indexOfList)


for i in range(len(indexOfList)):
   for j in range(0,len(indexOfList)-i-1):
      if indexOfList[j] > indexOfList[j + 1]:
        indexOfList[j], indexOfList[j + 1] = indexOfList[j + 1], indexOfList[j]
        ip_list[j],ip_list[j+1] = ip_list[j+1],ip_list[j]

res = ""
for i in ip_list:
   res = res + " " + i
        
print(res.strip())
