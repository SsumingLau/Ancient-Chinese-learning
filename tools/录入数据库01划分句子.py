import re

def split_sentences(text):
    # 使用正则表达式划分句子，考虑中文的句号、分号、问号、感叹号，但不将引号内的内容单独作为句子
    sentences = re.split(r'(?<=[。；？！])', text)
    
    # 将连续的引号内容合并到前一个句子中
    merged_sentences = []
    quote_buffer = ''
    for sentence in sentences:
        if sentence.endswith('“') or sentence.endswith('”'):
            quote_buffer += sentence
        elif quote_buffer:
            merged_sentences.append(quote_buffer + sentence)
            quote_buffer = ''
        else:
            merged_sentences.append(sentence)
    
    # 去除空白句子和空格
    merged_sentences = [sentence.strip() for sentence in merged_sentences if sentence.strip()]
    
    return merged_sentences

def read_and_split_text_file(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    title = lines[0].strip()  # 提取标题
    author = lines[1].strip()  # 提取作者
    
    # 将正文拼接成一个字符串
    content = ''.join(lines[2:])
    
    sentences = split_sentences(content)
    
    # 添加标题和作者的信息作为第一个句子
    sentences.insert(0, f"标题：{title}")
    sentences.insert(1, f"作者：{author}")
    
    return sentences

if __name__ == "__main__":
    txt_file = '/Users/liusiming/Documents/工作/北大附中/古文网站项目/教材古文材料.txt'
    sentences = read_and_split_text_file(txt_file)
    
    # 打印划分后的句子
    for index, sentence in enumerate(sentences, start=1):
        print(f"句子 {index}: {sentence}")
