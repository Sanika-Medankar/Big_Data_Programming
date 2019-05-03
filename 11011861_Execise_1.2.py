# Approach 2

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


def populateMatrix(s1, s2):
    
    len1 = len(s1)
    len2 = len(s2)
    
    path = [].append([])
    matrix = [].append([])
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            path[i][j] = 0
            matrix[i][j] = 0

    for i in range(len1):
        for j in range(len2):
            if s1[i] == s2[j]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                path[i][j] = -1
            elif matrix[i-1][j] >= matrix[i][j - 1]:
                matrix[i][j] = matrix[i - 1][j]
                path[i][j] = -2
            else:
                matrix[i][j] = matrix[i][j - 1]
                path[i][j] = -3
    return path


def lcs(path, s1, i, j, substring):
    if i == 0 or j == 0:
        return substring

    if path[i][j] == -1:
        lcs(path, s1, i - 1, j - 1, substring)
        substring = s1[i] + substring
    elif path[i][j] == -2:
        lcs(path, s1, i - 1, j, substring)
    else:
        path(path, s1, i, j - 1, substring)
        
    return substring
        

def main():
    
    s1 = inputStrings("first")
    s2 = inputStrings("second")
    
    path = populateMatrix(s1, s2)
    sub = lcs(path, s1, len(s1), len(s2), "")
    print(sub)
    print(len(sub))
    

if __name__ == "__main__":
    main()