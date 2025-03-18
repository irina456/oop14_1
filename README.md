# oop14_1
# Мой проект
## Запуск проекта
Запустите следующую команду в терминале, находясь в корневой дирректории проекта, чтобы увидеть результат работы всех функций:
```
python .\__main__.py
```

### Требование для запуска:
- python - v3.13


## Пакет src:
Модуль "classes.py" имеет 2 класса:

- Product
Принимает 4 обязательных свойства и возвращает данные с помощью 4х методов:
    name - возвращает название категори
    description - возвращает описание товара
    price - возвращает цену товара
    quantity - возвращает колличество товара
Имеет методы:
    price - возвращяют цену товара или может записывать значения в защещённую переменную
    new_product - возвращает экземпляр класса с обновлёнными данными

- Category
Принимает 3 обязательных свойства и возвращает данные с помощью 3х методов
    ame - возвращает название категории
    description - возвращает описание товара
    products - возвращает список товаров
Имеет 2 атрибута:
    category_count - вернёт колличество категорий
    product_count - вернёт колличество товаров
Имеет методы:
    add_product - добавляет новый список продуктов взащищённую переменную
    products - печатает в консоль список продуктов

Для классов реализованна защита данных, которые не должны быть изменены через публичный доступ, чтобы не нарушилась целостность данных

#### Обновление 15.2
В классы добавлены магические мeтоды, для возможности вызова экземпляра класса, а также метод __str__ для возможности вывести на экран информацию о содежимом экземпляра.

#### Обновление 16.1
Добавлены Дочерние классы Smartphone & LawnGrass, для создания экземпляров продуктов категории "Смартфоны" и "Трава газонная"


#### Обновление 16.2
Добавлен абстрактный класс для продуктов с абстрактными методами
Добавлен Миксин-класс для вывода информации, при создании экземпляров класса "LawnGrass" или "Smartphone"



## Тестирование 
Для запуска тестов потребуется:
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

Далее в терминале нужно запустить команду:
```
pytest
```


******************************************************************************************************************

# Homework project on implementing functionality for working with banking data

## Running the project
Run the following command in the terminal, being in the root directory of the project, to see the result all functions:
```
python .\__main__.py
```

### Requirement for running:
- python - v3.13

## Package src:

- Product
Accepts 4 required properties and returns data using 4 methods:
    name - returns the name
    description - returns the product description
    price - returns the product price
    quantity - returns the product quantity
Has methods:
    price - returns the price of the product or can write values ​​to a protected variable
    new_product - returns a class instance with updated data

- Category
Accepts 3 required properties and returns data using 3 methods
    name - returns the name of the category
    description - returns the description of the product
    products - returns a list of products
Has 2 attributes:
    category_count - returns the number of categories
    product_count - returns the number of products
Has methods:
    add_product - adds a new list of products to a protected variable
    products - prints a list of products to the console

#### Update 15.2
Magic methods have been added to classes to allow calling an instance of the class, as well as the __str__ method to display information about the contents of the instance.

#### Update 16.1
Smartphone & LawnGrass сhild Classes have been added to create instances of products in the "Smartphones" and "Lawn Grass" categories.


#### Update 16.2
Added abstract class for products with abstract methods
Added mixin class for outputting information when creating instances of the "LawnGrass" or "Smartphone" class



## Testing
To run tests you will need:
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

Next, you need to run the command in the terminal:
```
pytest
```
