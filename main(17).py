data=[]
suma=0

data_file=open("Data.txt","r")

while True:
    data_read=data_file.readline()
    if len(data_read)==0:
        break
    data.append(int(data_read))

for i in range (len(data)):
  suma=suma+data[i]
promedio=suma/len(data)
  
resultado_file=open("Resultados.txt","w")
resultado_file.write(str(promedio))
resultado_file.close()

data_file.close()