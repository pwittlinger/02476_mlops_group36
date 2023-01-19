import torch
from transformers import PegasusTokenizer, PegasusForConditionalGeneration

tokenizer = PegasusTokenizer.from_pretrained("results/model.pt/")
model = PegasusForConditionalGeneration.from_pretrained("results/model.pt/")
device = 'cuda' if torch.cuda.is_available() else 'cpu'

from fastapi import Request, FastAPI
app = FastAPI()
@app.post("/bert")
async def get_body(request: Request):
    data = await request.json()
    
    batch = tokenizer.prepare_seq2seq_batch(data['content'], truncation=True, padding='longest', return_tensors="pt")
    translated = model.generate(**batch)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    
    return {'summary': tgt_text[0]}