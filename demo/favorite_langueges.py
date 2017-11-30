"""导入Python的标准库"""
from collections import OrderedDict

"""记录添加字典的顺序"""
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarch'] = 'c'
favorite_languages['edadar'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "的擅长的语言--->" + language.title())
