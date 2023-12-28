n = int(input())
for i in range(n):
    dummy = input()
    arr = input()
    arr = list(arr)
    ans = ""

    vowels = set(['a','e'])
    consonents = set(['b','c','d'])

    string = ""
    for j in arr:
        if j in vowels:
            string+="V"
        else:
            string+="C"

    string = string.replace("CC","C.C")
    string = string.replace("VCV","V.CV")
    string = string.replace("VCV","V.CV")

    counter = 0
    for j in range(len(string)):
        if string[j] == ".":
            ans+='.'
        else:
            ans+=arr[counter]
            counter+=1
    
    print(ans)





        

        
        

        
        








