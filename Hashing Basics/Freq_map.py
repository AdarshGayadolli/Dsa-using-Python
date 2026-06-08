num=[5,6,7,8,9,10,3,3,4,1,5,6,7,2]
def fp(num):
    freq_map={}
    for i in range(0,len(num)):
        if num[i] in freq_map:
            freq_map[num[i]]+=1
        else:
            freq_map[num[i]]=1
    return freq_map
result=fp(num)
print(result)