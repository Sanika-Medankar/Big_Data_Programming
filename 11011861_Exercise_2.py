# not fully validated, some loop holes are there
def inputStrings(numberOf):
   enteredString = input("Enter " + str(numberOf) + "st string : ").strip().lower().replace(" ","").replace("\n","")
   if numberOf == 1:
       if enteredString.isalnum() == False:
           print("Incorrect string format. Please enter only alphanumeric characters.")
           inputStrings(numberOf)
       else:
           return enteredString
   elif numberOf == 2:
       if enteredString.isalpha() or '*' in enteredString or '.' in enteredString:
           return enteredString
       else:
           print("Incorrect string format. Please enter only alphabetic ,* or . characters.")
           inputStrings(numberOf)
  
 
def match(s1, s2):
   specialFlag = False
   i = 0
   j = 0
   string_from_regex = ""
   while (i < len(s1)):
       while (j < len(s2)):
           if (i < len(s1)):
               if s1[i] == s2[j]:
                   string_from_regex += s2[j]
                   i += 1
                   j += 1
                   break
               elif s2[j] == "*":
                   if (j-1 < 0):
                       j = len(s2)
                       break
                   else:
                       if (s2[j - 1] == "."):
                           # This code is repeated from the nes=xt elif, needs to be optimized
                            specialFlag = True
                            break

                       elif (s2[j - 1] == "*"):
                           j += 1
                           break
                       
                       elif s1[i] == s2[j-1]:
                           string_from_regex += s2[j - 1]
                           i += 1
                           # j += 1    Since * can be 0 or more occurances so the counter for j does not increase.
                           continue
                       else:
                           if s2[j] != "*":
                               string_from_regex += s2[j]   # j or j - 1
                           if (j < len(s2) - 1) and s2[j - 1] == s2[j + 1]:
                               string_from_regex += s1[j + 1]
                               j += 2
                           else:  
                               j += 1
                           #flag = False  # Need some more cases to verify whether to set the #flag or not.
                           break
               elif s2[j] == ".":
                        string_from_regex += s1[i]
                        i += 1
                        j += 1
                        continue
               else:
                   string_from_regex += s2[j]
                   j += 1
                   break
           else:
               break
       if j >= len(s2) and i < len(s1):     # This is an exhaustive break
           break
       if i >= len(s1):
           break
       if specialFlag:
           return specialFlag 
      
   return (s1 in string_from_regex)
 
 
def main():

   s1 = inputStrings(1)
   s2 = inputStrings(2)
   print(match(s1, s2))
 
if __name__ == "__main__":
   main()
