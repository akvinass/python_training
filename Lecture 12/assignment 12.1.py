import codecs
import re
def delete_html_tags(html_file, result_file='cleaned.txt'):
    pattern = re.compile(r'<[\s\S]*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleantext = pattern.sub('', html)

    with open (result_file, 'w', encoding='utf-8') as file:
        file.write(cleantext)

delete_html_tags('draft.html')