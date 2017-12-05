def count_words(filename):
    """计算一个文件包含多少个单词"""
    try:
        with open(filename) as file_object:
            """读取文件"""
            contents = file_object.read()
    except FileNotFoundError:
        msg = filename + "--->文件不存在"
        print(msg)
    else:
        """计算多少个单词"""
        words = contents.split()
        num_words = len(words)
        print(filename + ":文件的单词数是-->" + str(num_words))


filenames = ["..\\file\\programeming.txt", "..\\file\\text_files\\test.txt", "abcd.txt"]
for filename in filenames:
    count_words(filename)
