
# 写一段python代码。
# 首先遍历所有的在./src/content文件夹下的所有子文件夹和文件，然后找到所有的.tex文件
# 对于每个tex文件，读取其内容。逐行读取其文件内容，如果那一行是类似于：\src{snippet01} 这样的模式（它通常独占一行），snippet01这个位置还可能是其他的snippet名字，那么就将snippet01这个名字记录下来。
# 然后在这个tex文件的当前位置的./code/haskell文件夹下找到snippet01.hs文件，读取其内容，然后将”\src{snippet01}“这一行替换为如下
# \begin{lstlisting}[language=Haskell]
#   从snippet01.hs文件中读取到的内容。
# \end{lstlisting}

import os
import re

import os
import re

def process_tex_files(language):
    content_dir = './src/content'
    snippet_pattern = re.compile(r'\\src\{(.*?)\}')
    file_extension = {
        'haskell': 'hs',
        'ocaml': 'ml',
        'reason': 're',
        'scala': 'scala'
    }
    lstlisting_language = {
        'haskell': 'Haskell',
        'ocaml': 'OCaml',
        'reason': 'Reason',
        'scala': 'Scala'
    }

    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.tex'):
                tex_file_path = os.path.join(root, file)
                code_dir = os.path.join(root, f'code/{language}')

                print(f'Processing {tex_file_path}...')
                print('code file dir:', code_dir)
                with open(tex_file_path, 'r', encoding='utf-8') as tex_file:
                    lines = tex_file.readlines()

                new_lines = []
                for line in lines:
                    match = snippet_pattern.match(line.strip())
                    if match:
                        snippet_name = match.group(1)
                        code_file_path = os.path.join(code_dir, f'{snippet_name}.{file_extension[language]}')
                        print(f'Processing snippet {snippet_name}...')
                        if os.path.exists(code_file_path):
                            with open(code_file_path, 'r', encoding='utf-8') as code_file:
                                code_content = code_file.read()
                            new_lines.append(f'\\begin{{lstlisting}}[language={lstlisting_language[language]}]\n')
                            new_lines.append(code_content)
                            new_lines.append('\n')
                            new_lines.append('\\end{lstlisting}\n')
                        else:
                            new_lines.append(line)
                    else:
                        new_lines.append(line)

                with open(tex_file_path, 'w', encoding='utf-8') as tex_file:
                    tex_file.writelines(new_lines)

# Example usage
# process_tex_files('haskell')
# process_tex_files('ocaml')
# process_tex_files('reason')
process_tex_files('scala')
