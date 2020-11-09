import numpy as np

def main():
    instancePath = 'Dataset/ShortestPathInstance_100x500.txt'
    dataPath = '100x500.dat'
    paramString = "param D :"
    
    instanceFile = open(instancePath, 'r')
    finalFile = open(dataPath,'w')
    nodesfile = open("nodes.dat",'w')
    counterRow = 1

    dataToExport = None
    nodes = None
    

    for line in instanceFile.readlines():
        line = line.strip().split(" ")
        if(counterRow == 1):
            size = line[1].strip().split("x")
            nodes = int(size[0])
            dataToExport = np.zeros((nodes,nodes), dtype=float)

        elif(counterRow >= 7 and len(line) == 3):
            origin = int(line[0])-1
            destiny = int(line[1])-1
            weight = float(line[2])
            
            dataToExport[origin][destiny] = weight
            dataToExport[destiny][origin] = weight

        counterRow +=1

    #Primera linea con listado de variables
    counterRow = 0
    for i in range(nodes):
        paramString += str(i) + " \t "

    finalFile.write(paramString + ":= \n")

    #Lineas Siguientes con datos
    for i in range(nodes):
        row = str(i)+" \t "
        for j in range(nodes):
            row += str(dataToExport[i][j]) +" \t "
        row += "\n"
        finalFile.write(row)
    
    varFile = "var x "+"{0 .. "+str(nodes-1)+"}; \n"
    nodes = "param nodes := "+str(nodes)+"\n"

    nodesfile.write(nodes)
    finalFile.write(varFile)
    
    instanceFile.close()
    finalFile.close()
    nodesfile.close()
main()