# coding=gbk
# ����ű�ʱutf-8�ı���Ҫ����gbk����
# python3 ���ûὫutf-8ת��ΪUnicode
# �ַ�������unicode���ڴ��д���

s = 'С��'
s2 = s.encode('utf-8')
with open('test.tpad','w',encoding='utf-8') as file:
    file.write(s)

