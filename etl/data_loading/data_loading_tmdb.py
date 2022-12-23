import pandas as pd

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

# 将 JSON 格式的数据解析为 Pandas DataFrame
df = pd.read_json('/Users/lq/PycharmProjects/DeAirFlowProject/data/raw/movies.json')

# 检测缺失值
missing = df.isnull()

# 检测是否有任何行具有缺失值
has_missing = missing.any(axis=1)

# 获取有缺失值的 DataFrame
df_with_missing = df[has_missing]

# 打印有缺失值的 DataFrame
# print(df_with_missing)

# 手工查看缺失值所在的行 并且将无用的列drop掉 生成新的df
df_modified = df.drop(columns=['backdrop_path'])

# print(df_modified.genre_ids)


def is_empty_list(x):
    try:
        return isinstance(eval(x), list) and len(eval(x)) == 0
    except:
        return False


empty_genre_ids = df['genre_ids'].apply(is_empty_list)
print(df_modified[empty_genre_ids])
