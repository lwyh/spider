file = open('D:\\spider\\深入浅出python机器学习\\joke.txt','r',encoding='utf-8')
lines = file.readlines()
line = str(lines)
import jieba
line = jieba.cut(line)
x= ' '.join(line)
with open('D:\\spider\\深入浅出python机器学习\\cutjokes.txt','w') as f:
    f.write(x)

from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def print_topics(model,feature_names,n_top_words):
    for topic_idx,topic in enumerate(model.components_):
        message = 'topic #%d:' % topic_idx
        message += ' '.join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()

f =  open('D:\\spider\\深入浅出python机器学习\\cutjokes.txt','r')
n_top_words = 20
#Tfidf最大特征数为1000
tf = TfidfVectorizer(max_features=1000)
X_train = tf.fit_transform(f)
lda = LatentDirichletAllocation(n_components=10)
lda.fit(X_train)
print_topics(lda,tf.get_feature_names_out(),n_top_words)