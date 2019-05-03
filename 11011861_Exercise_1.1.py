#Approach 1

def inputStrings(numberOf):
    enteredString = input("Enter " + numberOf + " string : ")
    validatedString = enteredString.strip().upper().replace(" ","").replace("\n","")
    # s2 = s2.strip().upper().replace(" ","")
    if validatedString.isalnum() == False:
        print("Incorrect string format. Please enter only alphanumerics")
        inputStrings(numberOf)
    # if s2.isalnum() == False:
    #     print("Incorrect string format. Please enter only alphanumerics")
    return validatedString

def findAllCommonSubstrings(s1, s2):
    i = 0
    j = 0
    substring_array = []
    substring = ""
    last_index_of_substring = 0
    start_point = 1
    while True:
        while (i <= len(s1)):
            while (j <= len(s2)):
                if (j < len(s2) and i < len(s1)):
                    if(s1[i] == s2[j]):
                        substring += s1[i]
                        i += 1
                        j += 1
                        last_index_of_substring = j
                        break
                    else:
                        j += 1
                        continue
                    if (j > len(s2)):
                        substring_array.append(substring)
                        substring = ""
                        i += 1
                        j = 0
                        last_index_of_substring = 0
                        continue
                    # if (i > len(s1)):
                    #     i = start_point
                    #     start_point += 1
                    #     break
                elif(i < len(s1)):
                    i += 1
                    j = last_index_of_substring
                    break
                
                else:
                    i += 1
                    j = last_index_of_substring + 1
                    break
        
        if substring != "":
            substring_array.append(substring)    
        substring = ""
        i = start_point
        start_point += 1
        j = 0
        if (i < len(s1)):
            continue
        else:
            break

    # print(substring_array)
    return(substring_array)


def lcs(substring_array):
    longestSubstring = ""
    longestEqualSubstrings = []
    # i = 0
    for i in range(len(substring_array)):
        if (len(substring_array[i]) > len(longestSubstring)):
            longestSubstring = substring_array[i]
        elif (len(substring_array[i]) == len(longestSubstring)):
            longestEqualSubstrings.append(longestSubstring)
            longestEqualSubstrings.append(substring_array[i])
        else:
            i += 1

    return longestSubstring

def main():
    
    s1 = inputStrings("first")
    s2 = inputStrings("second")

    l_c_s = lcs(findAllCommonSubstrings(s1, s2) + findAllCommonSubstrings(s2, s1))
    print("A longest subsequence is : " + l_c_s)
    print("The length of LCS is : " + str(len(l_c_s)))
   


if __name__ == "__main__":
    main()