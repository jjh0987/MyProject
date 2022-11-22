import pandas as pd
import numpy as np
from sklearn.metrics import f1_score
from sklearn.preprocessing import LabelEncoder
import random
import os

import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from tqdm.notebook import tqdm
from transformers import BertTokenizer
from transformers import BertModel
from torch.optim import Adam

import matplotlib as mpl
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings(action='ignore')

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

CFG = {
    'EPOCHS': 2,
    'LEARNING_RATE':1e-5,
    'BATCH_SIZE':4,
    'SEED':41
}

def seed_everything(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True

seed_everything(CFG['SEED']) # Seed 고정

train = pd.read_csv('/Users/junho/Desktop/git_repo/pycharmProjects/pythonProject/dacon/NLP/train.csv')
train['Target'].value_counts()


le = LabelEncoder()
le = le.fit(train['Target'])
train['Target']=le.transform(train['Target'])


valid=train[train['Dialogue_ID'].isin([i for i in range(1016,1039)])].reset_index(drop=True)
train=train[~train['Dialogue_ID'].isin([i for i in range(1016,1039)])].reset_index(drop=True)

train_len=len(train)
val_len=len(valid)

print(train_len)
print(val_len)

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
# tokenizers = BertTokenizer.from_pretrained('bert-base-cased')

# model = AutoModelForSequenceClassification.from_pretrained("tae898/emoberta-base")
# tp = tokenizers(train['Utterance'][0], padding='max_length', max_length=512, truncation=True, return_tensors="pt")
# train_dataloader = torch.utils.data.DataLoader(tp, batch_size= CFG['BATCH_SIZE'], shuffle=True)
# tp['input_ids'][0]
# tp.keys()



class CustomDataset(Dataset):

    def __init__(self, data, mode="train"):
        self.dataset = data
        self.tokenizer = tokenizer
        self.mode = mode

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        text = self.dataset['Utterance'][idx]
        inputs = self.tokenizer(text, padding='max_length', max_length=512, truncation=True, return_tensors="pt")
        input_ids = inputs['input_ids'][0]
        # token_type_ids = inputs['token_type_ids'][0]
        attention_mask = inputs['attention_mask'][0]

        if self.mode == "train":
            y = self.dataset['Target'][idx]
            return input_ids, attention_mask, y
        else:
            return input_ids, attention_mask


train = CustomDataset(train, mode = "train")
valid = CustomDataset(valid, mode = "train")

train_dataloader = torch.utils.data.DataLoader(train, batch_size= CFG['BATCH_SIZE'], shuffle=True)
val_dataloader = torch.utils.data.DataLoader(valid, batch_size= CFG['BATCH_SIZE'], shuffle=False)

class BaseModel(nn.Module):

    def __init__(self, dropout=0.5, num_classes=len(le.classes_)):

        super(BaseModel, self).__init__()

        self.bert = BertModel.from_pretrained("bert-base")
        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(768, num_classes)
        self.relu = nn.ReLU()

    def forward(self, input_id, mask):

        _, pooled_output = self.bert(input_ids= input_id, attention_mask=mask,return_dict=False)
        dropout_output = self.dropout(pooled_output)
        linear_output = self.linear(dropout_output)
        final_layer = self.relu(linear_output)

        return final_layer

def train(model, optimizer, train_loader, test_loader, device):
    model.to(device)

    criterion = nn.CrossEntropyLoss().to(device)

    best_score = 0
    best_model = "None"
    for epoch_num in range(CFG["EPOCHS"]):

        model.train()
        train_loss = []
        for input_ids, attention_mask, train_label in tqdm(train_loader):
            optimizer.zero_grad()

            train_label = train_label.to(device)
            input_id = input_ids.to(device)
            mask = attention_mask.to(device)

            output = model(input_id, mask)

            batch_loss = criterion(output, train_label.long())
            train_loss.append(batch_loss.item())

            batch_loss.backward()
            optimizer.step()

        val_loss, val_score = validation(model, criterion, test_loader, device)
        print(
            f'Epoch [{epoch_num}], Train Loss : [{np.mean(train_loss) :.5f}] Val Loss : [{np.mean(val_loss) :.5f}] Val F1 Score : [{val_score:.5f}]')

        if best_score < val_score:
            best_model = model
            best_score = val_score

    return best_model

def competition_metric(true, pred):
    return f1_score(true, pred, average="macro")


def validation(model, criterion, test_loader, device):
    model.eval()

    val_loss = []
    model_preds = []
    true_labels = []
    with torch.no_grad():
        for input_ids, attention_mask, valid_label in tqdm(test_loader):
            valid_label = valid_label.to(device)
            input_id = input_ids.to(device)
            mask = attention_mask.to(device)

            output = model(input_id, mask)

            batch_loss = criterion(output, valid_label.long())
            val_loss.append(batch_loss.item())

            model_preds += output.argmax(1).detach().cpu().numpy().tolist()
            true_labels += valid_label.detach().cpu().numpy().tolist()
        val_f1 = competition_metric(true_labels, model_preds)
    return val_loss, val_f1




model = BaseModel()
model.eval()
optimizer = torch.optim.Adam(params = model.parameters(), lr = CFG["LEARNING_RATE"])

infer_model = train(model, optimizer, train_dataloader, val_dataloader, device)

