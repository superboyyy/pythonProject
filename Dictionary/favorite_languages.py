# 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite langugae is {language}.")

# 遍历字典
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())

# 指出两位朋友喜欢的语言
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# 确定某人是否参与了调查
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 按特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# 遍历字典中的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 使用集合来剔除重复项
for language in set(favorite_languages.values()):
    print(language.title())

# 在字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is: ")
    else:
        print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")