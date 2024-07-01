from transformers import Autotokenizer,AutoModelForSequenceClassification
import transformers
from transformers import pipeline
import torch
import torch.nn.functional as F

model_name="distilbert-base-uncased-finedtuned-sst-2-english"
model=AutoModelForSequenceClassification.from_preytrained(model_name)
tokenizer=Autotokenizer.from_pretrained(model_name)



classifier=pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)
result=classifier(["We are good we hope we don't hate by them"])
for i in result:
     print(i)
tokens=tokenizer.tokenize("We are good we hope we don't hate by them")
token_ids=tokenizer.convert_tokens_to_ids(tokens)
input_ids=tokenizer("We are good we hope we don't hate by them") 
print(tokens)
print(token_ids)
print(input_ids)