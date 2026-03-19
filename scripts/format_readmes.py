import re

import os

def clean_file(file_path, is_chinese=False):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 2. Replace all </br> with <br>
    content = content.replace('</br>', '<br>')

    # 5. Replace tabs with spaces
    content = content.replace('\t', ' ')

    lines = content.splitlines()
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # 4. Remove non-breaking spaces
        line = line.replace('\u00A0', ' ')
        
        # 1. Fix broken tables
        if re.match(r'^\s*\|.*\|\s*$', line):
            new_lines.append(line)
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and re.match(r'^\s*\|.*\|\s*$', lines[j]):
                i = j
                continue
            else:
                i += 1
                continue

        # 3 & 8. Standardize all table separators
        if re.match(r'^\s*\|?[:\s-]*\|[:\s-]*\|[:\s-]*\|?\s*$', line) and ('-' in line):
            # This regex might need to be more precise based on number of columns, 
            # but standardizing to 4 cols as requested.
            line = '| --- | --- | --- | --- |'
        elif re.match(r'^\s*[-:\s]*\|[-:\s]*\|[-:\s]*\s*$', line) and ('-' in line):
             line = '| --- | --- | --- | --- |'

        # 6. Ensure table headers are consistent
        if is_chinese:
            if re.match(r'^\s*\|?\s*(Name|名称)\s*\|\s*(Description|说明)\s*\|\s*(Links|链接)\s*\|\s*(Fees?|费用)\s*\|?\s*$', line, re.IGNORECASE):
                line = '| 名称 | 说明 | 链接 | 费用 |'
        else:
            if re.match(r'^\s*\|?\s*Name\s*\|\s*Description\s*\|\s*Links\s*\|\s*(Fees?)\s*\|?\s*$', line, re.IGNORECASE):
                line = '| Name | Description | Links | Fees |'

        new_lines.append(line)
        i += 1

    content = '\n'.join(new_lines)

    # 7. Fix broken TOC links
    if not is_chinese:
        content = content.replace('[News & Information](#news-information)', '[News Information](#news-information)')
    else:
        content = content.replace('[GPT/LLMs 应用](#gpt-llms应用)', '[GPT-LLMs应用](#gpt-llms应用)')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root
    project_root = os.path.dirname(script_dir)
    
    clean_file(os.path.join(project_root, 'README.md'), is_chinese=False)
    clean_file(os.path.join(project_root, 'README-CN.md'), is_chinese=True)
