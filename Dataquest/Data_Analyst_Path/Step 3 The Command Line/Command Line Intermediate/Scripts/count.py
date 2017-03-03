import read
import collections

df = read.load_data()

combine_headline = ""
for row in df.iterrows():
    combine_headline += str(df["headline"]).lower()

word_list = combine_headline.split(" ")
print(word_list[0:5])

cnt = collections.Counter()
for wd in word_list:
    cnt[wd] += 1
    
word100 = cnt.most_common(100)
print(word100)