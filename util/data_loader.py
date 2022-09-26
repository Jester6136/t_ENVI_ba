"""
@author : Hyunwoong
@when : 2019-10-29
@homepage : https://github.com/gusdnd852
"""
from torchtext.legacy.data import Field, BucketIterator,TabularDataset
class DataLoader:
    source: Field = None
    target: Field = None

    def __init__(self, tokenize_vi, tokenize_en, init_token, eos_token):
        self.tokenize_vi = tokenize_vi
        self.tokenize_en = tokenize_en
        self.init_token = init_token
        self.eos_token = eos_token
        print('dataset initializing start')

    def make_dataset(self):
        self.source = Field(tokenize=self.tokenize_en, init_token=self.init_token, eos_token=self.eos_token,
                                lower=True, batch_first=True)
        self.target = Field(tokenize=self.tokenize_vi, init_token=self.init_token, eos_token=self.eos_token,
                                lower=True, batch_first=True)
        self.fields = {'vi':('trg',self.target),'en':('src',self.source)}
        
        train_data, valid_data, test_data = TabularDataset.splits(
            path='data',
            train='train.json',validation='val.json',test='test.json',
            format='json',
            fields=self.fields
        )
        return train_data, valid_data, test_data

    def build_vocab(self, train_data, min_freq):
        self.source.build_vocab(train_data, min_freq=min_freq)
        self.target.build_vocab(train_data, min_freq=min_freq)

    def make_iter(self, train, validate, test, batch_size, device):
        train_iterator, valid_iterator, test_iterator = BucketIterator.splits((train, validate, test),
                                                                              batch_size=batch_size,
                                                                              sort_key=lambda x: len(x.src),
                                                                              sort_within_batch=True,
                                                                              shuffle=True,
                                                                              device=device)
        print('dataset initializing done')
        return train_iterator, valid_iterator, test_iterator
