#8. Create an iterator that yields words from a sentence one by one.
# class words:
#     def __init__(self,sentence):
#         self.sentence=sentence
#         self.count=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         word=""
#         for i in self.sentence:
#             if self.count==len(self.sentence):
#                 raise StopIteration
#             if i==" ":
#                 yield word
#                 self.count+=1
#             word+=i
#             self.count+=1
def words(str):
    for i in str.split(" "):
        print(i)
thanksgiving=words("Standing here today, I am filled with immense gratitude and joy.")
for i in thanksgiving:
    print(i,end=" ")