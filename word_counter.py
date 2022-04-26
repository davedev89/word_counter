from collections import Counter

def word_counter(func):
     def counter(*args, **kwargs):
          data = func(*args, **kwargs)
          total_words = data#.split()
          stopwords = ['y','Y','la','de','una','los','me','No','con','que','el','un','es','en','Que','muy','al','a','él','le','quiere','A','da','faltan','Mas','bien','del','las','por','lo','La','para','como']
          words = [word for word in total_words if word not in stopwords]
          wordcount = Counter(words)
          print('>>> TOP FIVE WORDS IN THIS TEXT <<<')
          for w in wordcount.most_common(5):
               print(f"{w[0]}: {w[1]}")
     return counter

@word_counter
def text_reader(file):
     data = []
     with open(file, "r", encoding="utf-8") as f:
          for line in f:
               split_line = line.split()
               data.extend(split_line)
     return data

# @word_counter
# def text_reader(url):
#      data = open(url , "r", encoding="utf-8")
#      return data 

news = "./texts/news.txt"
song = "./texts/song.txt"
speech = "./texts/speech.txt"

text_reader(news)
text_reader(song)
text_reader(speech)