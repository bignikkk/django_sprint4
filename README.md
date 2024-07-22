### Проект BLOGICUM

Blogicum - это социальная сеть-дневник для публикации собственных записей. На персональной странице пользователь может публиковать посты на разные темы, а также  посещать профайлы других участников проекта, просматривать и комментировать посты конкретного пользователя или определенной категории. Для нового поста необходимо указать категорию — например «путешествия», «кулинария» или «python-разработка», а также опционально локацию, с которой связан пост, например «Остров отчаянья» или «Караганда». 

### Автор:
Автор: Nikita Blokhin
GitHub: github.com/bignikkk

### Технологии:

Python
SQLite
Django

### Как развернуть проект локально:

```
git clone https://github.com/bignikkk/blogicum
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver