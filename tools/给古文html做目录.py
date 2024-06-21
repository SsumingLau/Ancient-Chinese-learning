import os
from bs4 import BeautifulSoup

def generate_index_html(input_dir='/Users/liusiming/Documents/GitHub/Ancient-Chinese-learning/materials from textbooks', index_file='/Users/liusiming/Documents/GitHub/Ancient-Chinese-learning/contents of articlces in textbooks2.html'):
    # 获取input_dir目录下的所有HTML文件
    html_files = [f for f in os.listdir(input_dir) if f.endswith('.html')]
    
    # 根据文件名中的数字部分排序
    html_files_sorted = sorted(html_files, key=lambda x: int(x.split('_')[0]))
    
    index_content = """
    <html>
    <head>
        <title>文言文目录</title>
    </head>
    <body>
        <h1>文言文目录</h1>
        <ul>
    """
    
    for html_file in html_files_sorted:
        # 拼接文件的完整路径
        file_path = os.path.join(input_dir, html_file)
        
        # 使用BeautifulSoup解析HTML文件
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
        
        # 提取标题和作者信息
        title = soup.find('h1').text.strip()
        author = soup.find('h2').text.strip()
        
        # 添加链接到目录中，显示为“标题 / 作者”
        index_content += f'<li><a href="{html_file}">{title} / {author}</a></li>\n'
    
    index_content += """
        </ul>
    </body>
    </html>
    """
    
    # 保存目录HTML文件
    with open(index_file, 'w', encoding='utf-8') as index_html:
        index_html.write(index_content)
    
    print(f"目录HTML文件已生成并保存为 {index_file}")

# 主程序入口
if __name__ == "__main__":
    generate_index_html()
