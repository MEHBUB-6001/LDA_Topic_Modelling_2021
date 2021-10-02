list_a=[0,0,2,2,3,3,8,2,7]
d={} # initializing dictionary
def CountMaxFrequencyElement(ele):
    count=0
    for index in range(len(list_a)):
        if list_a[index]==ele:
            count+=1
    return count
def RemoveMaxFrequencyFromLeft(ele):
    index=list_a.index(ele) # return index of max frequency element
    new_list=list_a.pop(index)
    print("Original List :")
    print(list_a)
    print("After Removing max frequency element new list become :")
    print(list_a)
if __name__=="__main__":
    for ele in list_a:
        d[ele]=CountMaxFrequencyElement(ele)
    max_freq_value=max(sorted(d.values()))
    print("Maximum frequency is :",max_freq_value)
    for key in d:
        if d[key]==max_freq_value:
            print("Max frequency element in list is :" ,key)
            RemoveMaxFrequencyFromLeft(key)



    
