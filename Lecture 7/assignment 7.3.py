def second_index(text, some_str):
    text_1st = text.find(some_str)
    if text_1st == -1:
        return None

    text_2nd = text.find(some_str, text.find(some_str) + 1)
    if text_2nd == -1:
        return None
    return text_2nd

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
#assert second_index("buddy", "s") is None, 'Test5'
print('ОК')