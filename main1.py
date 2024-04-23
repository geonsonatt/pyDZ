import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Инициализация пустого DataFrame для one-hot encoding
one_hot_data = pd.DataFrame()

# Получение уникальных категорий
categories = pd.Categorical(data['whoAmI']).categories

# Добавление столбцов для каждой категории
for category in categories:
    # Создание столбца и его заполнение 0 или 1 в зависимости от соответствия категории
    one_hot_data[category] = (data['whoAmI'] == category).astype(int)

# Показ результирующего DataFrame
one_hot_data.head()