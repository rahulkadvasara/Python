# poem.txt contains famous poem "Road not taken" by poet Robert Frost. 
# You have to read this file in your python program and find out words with maximum occurance.

word_stats = {}

with open('poem.txt','r') as f:
    for line in f:
        words=line.split(' ')
        for word in words:
            if word in word_stats:
                word_stats[word]+=1
            else:
                word_stats[word]=1
print(word_stats)

word_occurence = list(word_stats.values())
max_count = max(word_occurence)
print("Max occurence is ",max_count)
print("Word with max occurence are : ")
for word,count in word_stats.items():
    if count == max_count:
        print(word)