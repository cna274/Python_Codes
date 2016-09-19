def print_words(filename):
    f = open(filename, 'r')
    texts = f.read()
    words = (texts.lower())
    words = words.split()
    dict = {}
    for i in words:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    p = dict.items()
    p.sort()
    for i in range(len(p)):
        print p[i][0],p[i][1]
        
    return dict
"""
def word_count_dict(filename):
  # Utility used by count() and Topcount().
  word_count = {}  # Map each word to its count
  input_file = open(filename, 'r')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      # Special case if we're seeing this word for the first time.
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close()  # Not strictly required, but good form.
  return word_count


def print_words(filename):
 
  word_count = word_count_dict(filename)
  words = sorted(word_count.keys())
  for word in words:
    print word, word_count[word]
   """ 