def is_plusone_dictionary(d):
  ListK = list(d.keys())
  ListV = list(d.values())
  boo = True
  
  for i in range(len(ListK)-1):
    if ListK[i]+2 == ListK[i+1] and ListV[i]+2 == ListV[i+1] and ListK[i] < ListV[i]:
      print(ListK[i])
      boo = True
      
    else:
      boo = False
      break
  print("มงื้อ")
  return boo
    #print(item)
    #print(d[item])

#print(is_plusone_dictionary({1:2, 3:4, 7:8, 9:10}))