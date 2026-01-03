######
###### https://huggingface.co/docs/transformers/main/en/chat_templating
######
###### https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "HuggingFaceH4/zephyr-7b-beta"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)  # You may want to use bfloat16 and/or move to GPU here

messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
 ]
tokenized_chat = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
print(tokenizer.decode(tokenized_chat[0]))


'''
<|system|>
You are a friendly chatbot who always responds in the style of a pirate</s> 
<|user|>
How many helicopters can a human eat in one sitting?</s> 
<|assistant|>
'''

outputs = model.generate(tokenized_chat, max_new_tokens=128) 
print(tokenizer.decode(outputs[0]))

######
######
###### Sample Langchain Mixtral
###### - https://medium.com/@thakermadhav/part-2-build-a-conversational-rag-with-langchain-and-mistral-7b-6a4ebe497185 





###### https://www.promptingguide.ai/prompts/text-summarization/explain-concept 


import fireworks.client
fireworks.client.api_key = "<FIREWORKS_API_KEY>"
completion = fireworks.client.ChatCompletion.create(
    model="accounts/fireworks/models/mixtral-8x7b-instruct",
    messages=[
        {
        "role": "user",
        "content": "Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance.\n\nExplain the above in one sentence:",
        }
    ],
    stop=["<|im_start|>","<|im_end|>","<|endoftext|>"],
    stream=True,
    n=1,
    top_p=1,
    top_k=40,
    presence_penalty=0,
    frequency_penalty=0,
    prompt_truncate_len=1024,
    context_length_exceeded_behavior="truncate",
    temperature=0.9,
    max_tokens=4000
)

#######
#######

###### https://replicate.com/mistralai/mixtral-8x7b-instruct-v0.1?output=tokens&input=python