import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("nessa01macias/phi-2_sustainability-qa", trust_remote_code=False)

tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=False)

propmt = "Group the words into two categories, 'positive' or 'negative' based on the sentiment: efficient, helpful, slow, horrible, fantastic, disappointing, confusing, lovely, excellent. "

inputs = tokenizer(propmt, return_tensors="pt", return_attention_mask=False)

outputs = model.generate(**inputs, max_new_tokens=100)

text = tokenizer.batch_decode(outputs)[0]

print(text)
