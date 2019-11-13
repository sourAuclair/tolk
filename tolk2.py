import spacy
from spacy import displacy
from spacy.language import Language
from spacy.lang.nb import Norwegian
from spacy.lemmatizer import Lemmatizer

def main():
	# nlp_main = spacy.load('nb_ud_ner')
	nlp_main = spacy.load('nb_core_news_sm')

	sent = [
		"Kjør frem i 5 sekunder",
		"Kjør fram i 5 sekunder",
		"Kjør fremover i 5 sekunder",
		"Kjør baklengs i 5 sekunder",
		"Stopp nå",
		"Snu til høyre",
		"Snu til venstre",
		"Snu mot høyre",
		"Snu mot venstre"
		"Snu deg 5 grader til høyre",
		"Snu deg 5 grader til venstre"
	]
	for sentence in sent:
		tolk(sentence, nlp_main)
		print("")

def tolk(text, nlp):
	doc = nlp(text)
	for token in doc:
		print(token.text, token.lemma_, token.pos_, token.dep_, token.is_alpha, token.is_stop)
	#displacy.serve(doc, style="dep")

main()