"""

模拟一套简化的序列化传输方式，请实现下面的数据编码与解码过程
1.编码前数据格式为[位置，类型，值],多个数据的时候用逗号分隔，位置仅支持数字，不考虑重复等场景，类型仅支持
Integer/String/Compose(compose的数据类型表示该存储的数据也需要编码)
2.编码后数据参考图示，数据区的格式是：位置#类型#数，类型存储需要编码，Integer->0;String->1;Compose->2 长度是指数据的字符长度；数据仅允许数字，大小写字母，空格
3.输入的编码字符长度不能超过1000，一个数据的格式错误，则解析剩下数据，其他错误输出ENCODE_ERROR
4.输入的解码字符不能超过1000，数据区异常则跳过继续解析剩余数据区，其他异常输出DECODE_ERROR


输入描述：
输入有两行，第一行是命令，1表示编码，2表示解码，第二行输入待编码，解码的字符
数据最多嵌套10层，[1,Compose],[1,String,Second]为2层嵌套

输出描述：
如果输入要求是编码，则输出编码结果，如果输入要求是解码，则输出解码结果，当异常时输出对应的错误字符


"""

