# 键值错误
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# 使用get（）来访问值
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
