import pandas as pd
from rouge import Rouge 
import os
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer, Trainer, TrainingArguments
import wandb


#load data
# https://www.kaggle.com/datasets/sbhatti/news-summarization
data = pd.read_csv('data.csv', nrows=10000)
data = data[['Content', 'Summary']]
#show the data
#print(data.head())


#download the pre_trained model from the web
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")


device = 'cuda' if torch.cuda.is_available() else 'cpu'
device = 'cpu'

batch = tokenizer.prepare_seq2seq_batch(data['Content'].iloc[20], 
                                        truncation=True, 
                                        padding='longest', 
                                        return_tensors="pt")
translated = model.generate(**batch)
tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

#Rouge
print(rouge.get_scores(data['Summary'].iloc[20], tgt_text[0]))



#build the dataset[merge the content and summary]
class PegasusDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
        
    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels['input_ids'][idx])  # torch.tensor(self.labels[idx])
        return item
    
    def __len__(self):
        return len(self.labels['input_ids'])


def tokenize_data(texts, labels):
    # content
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=300)
    
    # summary
    decodings = tokenizer(labels, truncation=True, padding=True, max_length=200)
    
    dataset_tokenized = PegasusDataset(encodings, decodings)
    return dataset_tokenized

def prepare_data(model_name, 
                 train_texts, train_labels, 
                 val_texts=None, val_labels=None, 
                 test_texts=None, test_labels=None):
    """
    Prepare input data for model fine-tuning
    """
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    prepare_val = False if val_texts is None or val_labels is None else True
    prepare_test = False if test_texts is None or test_labels is None else True

    train_dataset = tokenize_data(train_texts, train_labels)
    val_dataset = tokenize_data(val_texts, val_labels) if prepare_val else None
    test_dataset = tokenize_data(test_texts, test_labels) if prepare_test else None

    return train_dataset, val_dataset, test_dataset, tokenizer


#fine-turn

def prepare_fine_tuning(model_name, tokenizer, train_dataset, val_dataset=None, freeze_encoder=False, output_dir='./results'):
    """
    Prepare configurations and base model for fine-tuning
    """
    # torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    torch_device = 'cpu'
    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    
    
    
    if freeze_encoder:
        for param in model.model.encoder.parameters():
            param.requires_grad = False

    if val_dataset is not None:
        training_args = TrainingArguments(
          output_dir=output_dir,           # output directory
          num_train_epochs=1,              # total number of training epochs
          per_device_train_batch_size=1,   # batch size per device during training, can increase if memory allows
          per_device_eval_batch_size=1,    # batch size for evaluation, can increase if memory allows
          save_steps=500,                  # number of updates steps before checkpoint saves
          save_total_limit=5,              # limit the total amount of checkpoints and deletes the older checkpoints
          evaluation_strategy='steps',     # evaluation strategy to adopt during training
          eval_steps=100,                  # number of update steps before evaluation
          warmup_steps=500,                # number of warmup steps for learning rate scheduler
          weight_decay=0.01,               # strength of weight decay
          logging_dir='./logs',            # directory for storing logs
          logging_steps=10,
          report_to = 'wandb',
        )

        trainer = Trainer(
          model=model,                         # the instantiated 🤗 Transformers model to be trained
          args=training_args,                  # training arguments, defined above
          train_dataset=train_dataset,         # training dataset
          eval_dataset=val_dataset,            # evaluation dataset
          tokenizer=tokenizer
        )

    else:
        training_args = TrainingArguments(
          output_dir=output_dir,           # output directory
          num_train_epochs=1,           # total number of training epochs
          per_device_train_batch_size=1,   # batch size per device during training, can increase if memory allows
          save_steps=500,                  # number of updates steps before checkpoint saves
          save_total_limit=5,              # limit the total amount of checkpoints and deletes the older checkpoints
          warmup_steps=500,                # number of warmup steps for learning rate scheduler
          weight_decay=0.01,               # strength of weight decay
          logging_dir='./logs',            # directory for storing logs
          logging_steps=10,
          report_to = 'wandb',
          
        )

        trainer = Trainer(
          model=model,                         # the instantiated 🤗 Transformers model to be trained
          args=training_args,                  # training arguments, defined above
          train_dataset=train_dataset,         # training dataset
          tokenizer=tokenizer
        )

    return trainer


train_texts, train_labels = list(data['Content'].iloc[:100]), list(data['Summary'].iloc[:100])

# use Pegasus Large model as base for fine-tuning
model_name = 'google/pegasus-xsum'

train_dataset, _, _, tokenizer = prepare_data(model_name, train_texts, train_labels)

trainer = prepare_fine_tuning(model_name, tokenizer, train_dataset)
trainer.train()

#save the model
trainer.save_model('results/model.pt')