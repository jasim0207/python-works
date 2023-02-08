#3. Replace each special symbol with # in the following string

# str1 = '/*jon is @developer & musician!!'
# o/p: ##jon is #developer #musician##

str1 = '/*jon is @developer & musician!!'
str1 = str1.replace('/','#').replace('*','#').replace('!','#').replace('@','#').replace("&","#")
print(str1)