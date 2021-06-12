from gensim.models import word2vec
import data_loader
import os
class Mysentences(object):
    def __init__(self,dirpath):
        self.dirpath = dirpath
    def __iter__(self):
        for fname in os.listdir(self.dirpath):
            for line in open(os.path.join(self.dirpath,fname)):
                yield line.split()

print('loader data')
train_data_scale , test_data_scale = 200 , 2000
train_src , train_tgt = data_loader.load_data('train_x','train_y', count = train_data_scale)
word2vec_model = word2vec.Word2Vec(train_src,min_count=10 ,size= 300)
print(word2vec_model['2'])
