import json


def convert(infile, outfile):
  fin = open(infile, 'r', encoding='utf-8')
  fout = open(outfile, 'w', encoding='utf-8')
  for line in fin:
    document, summary = line.strip('\n').split('\t')
    # json.dumps把python对象(诸如dict/list/tuple/string等数据结构)转换为字符串。只不过这个字符串比较特别，其特别之处在于它的语法格式同json保持一致。如将字典中的单引号均置为双引号
    print(json.dumps({'document': document, 'summary': summary}), file=fout)
  fin.close()
  fout.close()

if __name__ == '__main__':
  convert('data/train.txt', 'data/good_format_train.txt')
  convert('data/valid.txt', 'data/good_format_valid.txt')
  convert('data/test.txt', 'data/good_format_test.txt')
