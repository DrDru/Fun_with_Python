import wikipedia
import spacy
nlp = spacy.load('en_core_web_md')

wikipedia.set_lang("jp")
b = (wikipedia.page("ロンドン").content)


doc = nlp(b)


#my_set = {'routes', 'python', 'there', 'cycle', 'paris.', '(270', 'and', 'anaconda', 'are', 'in', 'paths', 'km', 'of', 'mi)', '440'}
my_set = {'ヒースロー', '空港','T5'}


for sent in doc.sents:
    tmp = sent.text	
    
    tmp2 = set(tmp.lower().split(" "))
    if tmp2.issubset(my_set):
        print(tmp)
			
			
doc = nlp(u"This is a sentence. This is another sentence.")
for sent in doc.sents:
    print(sent.text)
	
p = 	"イギリスやヨーロッパ域内で最大の都市圏を形成している"
p.lower().split(" ")