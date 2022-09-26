"""
@author : Hyunwoong
@when : 2019-10-29
@homepage : https://github.com/gusdnd852
"""
from conf import *
from util.data_loader import DataLoader
from util.tokenizer import Tokenizer

tokenizer = Tokenizer()
loader = DataLoader(
                    tokenize_vi=tokenizer.tokenize_vi,
                    tokenize_en=tokenizer.tokenize_en,
                    init_token='<sos>',
                    eos_token='<eos>')

train, valid, test = loader.make_dataset()

print("load data raw successfully!!")
loader.build_vocab(train_data=train, min_freq=32000)
train_iter, valid_iter, test_iter = loader.make_iter(train, valid, test,
                                                     batch_size=batch_size,
                                                     device=device)
print("make iter successfully")
src_pad_idx = loader.source.vocab.stoi['<pad>']
trg_pad_idx = loader.target.vocab.stoi['<pad>']
trg_sos_idx = loader.target.vocab.stoi['<sos>']

enc_voc_size = len(loader.source.vocab)
dec_voc_size = len(loader.target.vocab)