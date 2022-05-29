from DataSetOperations import DataSetOperations
from DataProcessing import DataProccessing
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import word_tokenize
from textblob import Word


lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()



cacm = DataSetOperations()
cacm.preprocess_docs(filepath='./data_sets/cacm/cacm.all')
cacm.preprocess_docs(filepath='./data_sets/cacm/query.text',type='query')
cacm.preprocess_rel(filepath='./data_sets/cacm/qrels.text')


dp = DataProccessing(data= 'told you   that shit happens while went to hell  ',tagger= pos_tag,stemmer=stemmer,stop_words=stopwords.words('english'),tokenizer=word_tokenize,w_corrector=Word)

dp.tokanize_words()
dp.correct_words()
dp.stemm_words()
dp.lemmatize_words()
dp.gather_stirng()
dp.parse_dates()

print(dp.data)

