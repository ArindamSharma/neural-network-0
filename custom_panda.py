def is_a_number(string):
    try:
        temp=int(string)
        return temp
    except (ValueError):
        try:
            temp=float(string)
            return temp
        except (ValueError):
            return string
def panda(fname):
    fopener=True
    try:
        fptr=open(fname,"r")
        data=[]
        fopener=fptr.readline().strip("\n")
        data_Lable=fopener.split(",")
        for i in range(len(data_Lable)):
            data.append([])
        while(fopener):
            fopener=fptr.readline().strip("\n")
            if(len(fopener)!=0):
                j=fopener.split(",")
                for i in range(len(data_Lable)):
                    data[i].append(is_a_number(j[i].strip(" ")))
        fptr.close()
        fopener=True
    except (FileNotFoundError):
        fopener=False
    if(fopener):
        return (data_Lable,data)
    else:
        return False

def print1(data):
    for j in range(len(data[1][0])):
        for i in range(len(data[0])):
            print(data[0][i],":-",data[1][i][j]," ",end="")
        print("")
def print_table(data):
    spacing=15
    for i in data[0]:
        print( i.ljust(spacing),end="")
    print("")
    for j in range(len(data[1][0])):# 150
        # print(j,end=" ")
        for i in range(len(data[1])):# 5
            print(str(data[1][i][j]).ljust(spacing),end="")
        print("")

if __name__ == "__main__":
    print("Only for testing Pourpose :-",is_a_number("2.3")
    ,is_a_number("2")
    ,is_a_number("hello"))