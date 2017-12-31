import os
import csv

#I attempted to use regular expressions like suggested for sentence length, but couldn't get them to work
#I had lots of errors calling the function, so I'm not sure what the issue was.  The method I came up with
#wasn't elegant, but I believe got the job done

paragraph_text = os.path.join("Resources","paragraph_1.txt")

paragraph = []
words = []
sentences = 0
letters = 0

with open (paragraph_text) as inputfile:
    for row in inputfile:
        paragraph = row

character_count = (len(paragraph))

words = paragraph.split (" ")

word_count = (len(words))

for row in words:
    if "." in row or "?" in row or "!" in row:
        sentences = sentences + 1

output_file = os.path.join("Resources","ParagraphAnalysis.txt")
with open (output_file, "w") as text_file:
    print ("Paragraph Analysis", file=text_file)  
    print ("-" * 20, file=text_file)
    print ("Approximate Word Count: " + str(word_count), file=text_file)
    print ("Approximate Sentence Count: " + str(sentences), file=text_file)
    print ("Average Letter Count: " + str ((character_count/word_count)), file=text_file)
    print ("Average Sentence Length: " + str ((word_count/sentences)), file=text_file)


print ("Paragraph Analysis")  
print ("-" * 20)
print ("Approximate Word Count: " + str(word_count))
print ("Approximate Sentence Count: " + str(sentences))
print ("Average Letter Count: " + str ((character_count/word_count)))
print ("Average Sentence Length: " + str ((word_count/sentences)))

