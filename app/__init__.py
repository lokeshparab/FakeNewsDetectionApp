import pickle
import pandas as pd
import re
import string

vectorization = pickle.load(open('static/model/vector_model.sav','rb'))
linear_clf = pickle.load(open('static/model/model_lc.sav','rb'))
DT = pickle.load(open('static/model/model_dt.sav','rb'))
GBC = pickle.load(open('static/model/model_gbc.sav','rb'))
LR = pickle.load(open('static/model/model_lr.sav','rb'))


def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

def detect_text(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt) 
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    pred_LR = LR.predict(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_GBC = GBC.predict(new_xv_test)
    #pred_RFC = RFC.predict(new_xv_test)
    return (pred_LR, pred_DT, pred_GBC)

    #RFC = pickle.load(open('model_rfc.sav','rb')