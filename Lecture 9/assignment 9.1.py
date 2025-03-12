def popular_words (text, words):
    x = text.lower().split()
    my_dict = {i: x.count(i) for i in words}
    return my_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
