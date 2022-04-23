import matplotlib.pyplot as plt

fi=open("./flow_dg/inputs/monero_full_outgoing_novpn.txt");

counter=0
sizeArray=[]
sizeArray_filtered=[]
for oneRow in fi:
    cell=int(oneRow.split(',')[1].strip())
    if cell != 54 and cell != 60 and cell != 74 and cell != 66 and cell != 78:
        sizeArray.append(cell)
        sizeArray_filtered.append(None)
    else:
        sizeArray.append(None)
        sizeArray_filtered.append(cell)
    counter+=1


plt.figure()
plt.title('monero full node wireless output traffic')
plt.xlabel('order')
plt.ylabel('packet size')
plt.plot(sizeArray, 'ro')
plt.plot(sizeArray_filtered, 'yo')
plt.show()