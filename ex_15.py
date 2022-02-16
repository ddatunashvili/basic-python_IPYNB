
from sys import argv

filename = "ex_15_sample.txt"

txt = open(filename, encoding='utf8')

print(f"აქ არის შენი ფაილი {filename}:")
print(txt.read())

print("ძმურად, კიდევ ერთხელ დაწერე ფაილის სახელი:")
file_again = input('>')

text_again=open(file_again, encoding='utf8')

print(text_again.read())
'''
txt= open('ex_15_sample.txt')
'''
