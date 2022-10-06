#!/usr/bin/env python3

import os
import os.path
import re
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

dir_pattern = re.compile('[0-9]{2}[a-z]*_(.*)')
file_pattern = re.compile('([0-9]{2}[a-z]*_.*)\.py')
repo_url = 'https://github.com/azzieg/mindstorms-inventor'
repo_commit = 'e6efa09fc7ff193947130f678f5a9b44236d78d7'
repo_path = 'word_blocks'

print('''# Word Blocks Python reference

In the following snippets, the `vm` variable is a reference to a VirtualMachine
instance and the `await` keyword can only be used in async functions. Please
read the [introduction](/README.md) to learn about the basic setup necessary to
run such code on a LEGO hub.''')
for dir in sorted(os.listdir('.')):
    dir_match = dir_pattern.match(dir)
    if not dir_match: continue
    print()
    title = ' '.join(
        word if word == 'to' else word.capitalize()
        for word in dir_match.group(1).split('_'))
    print(f'''## {title}

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |''')
    for file in sorted(os.listdir(dir)):
        file_match = file_pattern.match(file)
        if not file_match: continue

        file_png = f'{dir}/{file_match.group(1)}.png'
        with Image.open(file_png) as png:
            half_width = png.size[0] // 2
            img = f'<img src="/{repo_path}/{file_png}" width="{half_width}">'

        file_py = f'{dir}/{file}'
        with open(file_py) as py:
            ref = f'{repo_url}/blob/{repo_commit}/{repo_path}/{file_py}#L1'
            lines = len(py.readlines())
            if lines > 1: ref += f'-L{lines}'

        print(f'| {img} | {ref} |')
