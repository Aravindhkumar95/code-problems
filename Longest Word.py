'''
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
'''
def LongestWord(sen):
  k = []
  for i in sen:
    if i.isalpha() or i==' ':
      k.append(i)
  sun = (''.join(k)).split()
  long = sun[0]
  for j in range(1,len(sun)):
    if len(sun[j])>len(long):
      long=sun[j]

  # code goes here
  return long

# keep this function call here 
print(LongestWord(input()))
