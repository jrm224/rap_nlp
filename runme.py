from data_processing import *
#txt, huj = make_array("Mein Kampf-Polish.txt")
#txt, huj = make_array("w-pustyni-i-w-puszczy.txt")
txt, huj = make_array("mein-kampf-w-pustyni-i-w-puszczy.txt")
fq, words, weights = bigram_haiku_data(txt,huj)
#print(fq)
print(random_haiku(txt))
print('\n', bigram_haiku(fq,words,weights))
print('\n', bigram_hot16(fq, words, weights))
