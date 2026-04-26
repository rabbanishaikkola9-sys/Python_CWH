for i  in range(0,20):
    if(i==18):
        break  # exit the loop abruptly or right now
    print(i)
for j in range(0,20):
    if(j<20 and j!=2):
        continue  # skip this iteration
    print(j)