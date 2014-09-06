# Gem Stones (https://www.hackerrank.com/challenges/gem-stones) 
# John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a lowercase latin letter from 'a' to 'z'. An element can be present multiple times in a rock. An element is called a 'gem-element' if it occurs at least once in each of the rocks.
#
# Given the list of N rocks with their compositions, display the number of gem-elements that exist in those rocks.
#
# Input Format
# The first line consists of N, the number of rocks.
# Each of the next N lines contain rocks' composition. Each composition consists of lowercase letters of English alphabet.
#
# Output Format
# Print the number of gem-elements that are common in these rocks.
#
# Constraints
# 1 ≤ N ≤ 100
# Each composition consists of only small latin letters ('a'-'z').
# 1 ≤ Length of each composition ≤ 100
#
# Sample Input
#
# 3
# abcdde
# baccd
# eeabg
# Sample Output
#
# 2


s=[]
for i in range(input()):
    s.append(raw_input())

count = 0
x=set()
for i in s[0]:
    if all(s[j].__contains__(i)!=False for j in range(1,len(s))) and i not in x:
        x.add(i)
        count = count + 1
print count
