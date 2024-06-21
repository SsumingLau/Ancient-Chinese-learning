import os

# 读取并解析txt文件内容
def parse_txt_file(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    articles = []
    current_article = {}
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        if line.startswith('标题：'):
            if current_article:
                articles.append(current_article)
            current_article = {'标题': line[3:].strip()}
            index += 1

            if index < len(lines) and lines[index].strip().startswith('作者：'):
                current_article['作者'] = lines[index].strip()[3:].strip()  # 去除前缀的“作者：”
                index += 1
            else:
                print(f"Error: Missing or malformed '作者：' at line {index + 1}")
                current_article = {}
                continue

            if index < len(lines) and lines[index].strip().startswith('正文：'):
                index += 1
                current_article['正文'] = []
                while index < len(lines) and not lines[index].strip().startswith('标题：'):
                    current_article['正文'].append(lines[index])
                    index += 1
            else:
                print(f"Error: Missing or malformed '正文：' at line {index + 1}")
                current_article = {}
                continue
        else:
            index += 1
    
    if current_article:
        articles.append(current_article)
    
    return articles

# 生成HTML文件
def generate_html_files(articles, output_dir='output_html'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for index, article in enumerate(articles):
        title = article['标题']
        author = article['作者']
        content = ''.join(article['正文'])  # 保留换行符
        
        # 生成HTML内容
        html_content = (
            "<html>\n"
            "<head>\n"
            "    <title>" + title + "</title>\n"
            "</head>\n"
            "<body>\n"
            "    <h1>" + title + "</h1>\n"
            "    <h2>" + author + "</h2>\n"  # 不再添加“作者：”
            "    <p>" + content.replace('\n', '<br>') + "</p>\n"
            "</body>\n"
            "</html>"
        )
        
        # 保存为HTML文件
        file_name = str(index + 1) + "_" + title + ".html"
        with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
    
    print(f"HTML文件已生成并保存到 {output_dir} 文件夹中")

# 主程序入口
if __name__ == "__main__":
    txt_file = '/Users/liusiming/Documents/工作/北大附中/古文网站项目/教材古文材料.txt'  # 替换为你的txt文件路径
    articles = parse_txt_file(txt_file)
    generate_html_files(articles)
