from imports import *

class Preprocessing:
    def __init__(self):
        pass

    def extract_resume_text(self,resume_path):
        pdf = pdfx.PDFx(resume_path)
        text = pdf.get_text()
        
        return text
    
    def preprocess_text(self,text):
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text.lower())
        filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
        return lemmatized_tokens
    
    def pos_filter(self,tokens):
        pos_tags = pos_tag(tokens)
        filtered_tokens = [token for token, pos in pos_tags if pos.startswith('NN') or pos.startswith('VB')]
        model_input=' '.join(filtered_tokens)
        return model_input

    def extract_named_entities(text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        named_entities = [ent.text for ent in doc.ents if ent.label_ != "CARDINAL" and ent.label_ != "DATE"]
        processed_list = []
        for word in named_entities:
            processed_word = word.replace('\n', '').lower()
            processed_list.append(processed_word)
        return named_entities
    
    def extract_keywords(text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        keywords = []
        for token in doc:
            if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
                lemma = token.lemma_.lower().strip()
                keywords.append(lemma)
        return keywords