from ollama import chat

def extract_schedule(text):
    prompt = f"""
Extract meeting details from this sentence.

Return JSON list like:
[{{"event":"meeting name","day":"day","time":"time"}}]

Sentence:
{text}
"""
    response = chat(model='llama3', messages=[{'role':'user','content':prompt}])
    return response['message']['content']

