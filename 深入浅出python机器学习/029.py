#使用CountVectorizer对文本进行特征提取
#x导入向量化工具CountVectorizer工具
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
#s使用ountVectorizer拟合文本数据
en = ['The quick brown fox jumps over a lazy dog']
vect.fit(en)

#使用中文文本进行试验
cn = ['那只敏捷的棕色狐狸跳过了一只懒惰的狗']
#拟合中文文本数据
vect.fit(cn)



#使用分词工具对中文文本进行分词
#导入结巴分词
import jieba 
#使用jieba分词对中文文本进行分词
cn = jieba.cut('那只敏捷的棕色狐狸跳过了一只懒惰的狗')
#使用空格作为词与词之间的分界线
cn = [' '.join(cn)]
#print(cn)


#使用CountVectorizer对中文文本呢进行向量化
vect.fit(cn)


#使用词袋模型将我呢本数据转为数组
bag_of_words = vect.transform(cn)
#懒惰的狐狸不如敏捷的狐狸敏捷 敏捷的狐狸不如 惰的狐狸懒惰
#输入新的中文文本
cn_1 = jieba.cut('懒惰的狐狸不如敏捷的狐狸敏捷,敏捷的狐狸不如懒惰的狐狸懒惰')
#以空格进行分隔
cn2 = [' '.join(cn_1)]
#print(cn2)

#建立新的词袋模型
new_bag = vect.transform(cn2)


#随笔那写一句话
joke = jieba.cut('道士看见和尚亲吻了尼姑的嘴唇')
#插入空格
joke = [' '.join(joke)]
vect.fit(joke)
joke_feature = vect.transform(joke)

joke2 = jieba.cut('尼姑看见道士的嘴唇亲吻了和尚')
#插入空格
joke2 = [' '.join(joke2)]
joke2_feature = vect.transform(joke2)



#修改CountVectorizer的ngram参数
vect = CountVectorizer(ngram_range = (2,2))
#重新进行文本数据的特征提取
cv = vect.fit(joke)
joke_feature = cv.transform(joke)


joke2 = jieba.cut('尼姑看见道士的嘴唇亲吻了和尚')
#插入空格
joke2 = [' '.join(joke2)]
joke2_feature = vect.transform(joke2)

















#打印词袋模型中的数据特征
print('转化为词袋的特征:\n{}'.format(repr(bag_of_words)))
print('词袋的密度表达:\n{}'.format(bag_of_words.toarray()))
print('转化为词袋的新特征:\n{}'.format(repr(new_bag)))
print('词袋的密度新表达:\n{}'.format(new_bag.toarray()))
print('调整N-Gram参数后的词典：{}'.format(cv.get_feature_names_out()))
print('这句话的特征表达:\n{}'.format(joke_feature.toarray()))
print('这句话2的特征表达:\n{}'.format(joke2_feature.toarray()))
print('单词数:{}'.format(len(vect.vocabulary_)))
print('分词:{}'.format(vect.vocabulary_))
