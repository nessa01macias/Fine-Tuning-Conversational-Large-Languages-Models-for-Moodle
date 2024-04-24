import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("nessa01macias/phi1.5_finetuned_sustainability_qa", trust_remote_code=True, torch_dtype=torch.float32)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5", trust_remote_code=True)

test_text = """"Read the article and select the best answer. Article: When I was a baby, I interested you and made you laugh.
Whenever I was \"bad\", you'd shake your finger at me and ask: \"How could you?\"--but then you'd give up, and roll me over
for a belly scratch  and I believed that life could not be any more perfect. My housetraining was a long process, because
you were terribly busy, but we worked on that together. We went for long walks, runs in the park and car rides.
We stopped for ice cream. I took long sleeps in the sun waiting for you to come home at the end of the day.
Step by step, you began spending more time at work and on your career, and more time searching for a human friend.
Finally, you fell in love. She, now your wife, is not a dog person, but I still welcomed her into our home.
I was happy because you were happy. Then the human babies came along and I shared your excitement,
I was attracted by their pinkness, how they smelled, and I wanted to mother them too. Your wife was afraid I would bite them.
However, as they began to grow, I became their friend. Now, you have a new job in another city and you and they will be moving 
to a flat that does not allow pets. You've made the right decision for your \"family\", but there was a time when I was your only family. 
I was excited about the car ride until we arrived at the dog pound . It smelled of dogs and cats, of fear, of hopelessness.
You filled out the paperwork and said: \"I know you will find a good home for her.\" They shrugged  and gave you a pained look.
The children were in tears as they waved me goodbye. And \"How could you?\" were the only three words that swept over my mind. 
Is it better to live with hope or without hope? At first, whenever anyone passed my pen, I rushed to the front, hoping it was you,
that you had changed your mind and that this was all a bad dream. My beloved master, I will think of you and wait for you forever. 
I hope you receive more faithfulness  from your family than you showed to me. Question: What is the theme of the story? 
Options: A: Be faithful to those who love you. B: Never expect too much. C: Never complain about your life. D: Be ready for changes"""

test =f"question: {test_text} answer: "

inputs = tokenizer(test, return_tensors="pt", return_attention_mask=False)

outputs = model.generate(**inputs, max_length=512)
text = tokenizer.batch_decode(outputs)[0]
print(text)
