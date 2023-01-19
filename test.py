from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


#open text file in read mode
text_file = open("./text.txt", "r")
 
#read whole file to a string
ARTICLE = text_file.read()
 
#close file
text_file.close()
print(summarizer(ARTICLE, max_length=300, min_length=100, do_sample=False))