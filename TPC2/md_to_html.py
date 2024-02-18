import re

def md_to_html(md_text):
    # Heading
    md_text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', md_text)
    md_text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', md_text)
    md_text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', md_text)
    
    # Bold
    md_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b><br><br>', md_text)
    
    # Italic
    md_text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', md_text)
    
    # Ordered List
    md_text = re.sub(r'^(\d+)\. (.*?)$', r'<ol start="\1"><li>\2</li></ol>', md_text, flags=re.M)
    
    # Unordered List
    md_text = re.sub(r'^\* (.*?)$', r'<ul><li>\1</li></ul><br>', md_text, flags=re.M)
    
    # Blockquote
    md_text = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', md_text, flags=re.M)
    
    # Code
    md_text = re.sub(r'`(.*?)`', r'<code>\1</code>', md_text)
    
    # Horizontal Rule
    md_text = re.sub(r'^---$', r'<hr>', md_text)

    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', md_text)
    
    # Link
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a><br><br>', md_text)
    
    # Image
    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', md_text)

    md_text = f'<div style="text-align: left;">{md_text}</div>'

    return md_text


def read_md(path_to_md):
    with open(path_to_md, 'r') as md_file:
        md_lines = md_file.readlines()
    return [md_to_html(line.strip()) for line in md_lines]

def write_html(html_lines):
    html_content = f"""
    <html>
    <head>
        <title>MarkDown</title>
    </head>
    <body>
        {''.join(html_lines)}
    </body>
    </html>
    """

    with open('index.html', 'w') as html_file:
        html_file.write(html_content)

def main():
    path_to_md = input("Indique o caminho para o ficheiro MarkDown: ")
    html_lines = read_md(path_to_md)
    write_html(html_lines)

if __name__ == "__main__":
    main()