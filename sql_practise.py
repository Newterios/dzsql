from config import DB_path
import sqlite3


def add_post(titile: str, content: str) -> None:
    add_posts = """
    INSERT INTO posts(title, content) VALUES (?, ?);
    """

    conection = sqlite3.connect(DB_path)
    cursor = conection.cursor()

    cursor.execute(
        add_posts,
        (
            titile,
            content,
        ),
    )

    conection.commit()
    conection.close()
    return "все довавили"


def get_posts():
    get_posts_query = """
    SELECT * FROM posts;
    """

    conection = sqlite3.connect(DB_path)
    cursor = conection.cursor()
    cursor.execute(get_posts_query)
    posts = cursor.fetchall()  #
    conection.close()
    return posts


def delete_post(post_id: int) -> None:
    delete_post_query = """ 
    DELETE FROM posts WHERE posts_id = ?
    """
    connection = sqlite3.connect(DB_path)
    cursor = connection.cursor()

    cursor.execute(delete_post_query, (post_id,))
    connection.commit()
    connection.close()

    return f"Удалено постов: {cursor.rowcount}"


def get_post(post_id: int):
    get_post_query = """
    SELECT * FROM posts WHERE posts_id = ?
    """
    connection = sqlite3.connect(DB_path)
    cursor = connection.cursor()
    cursor.execute(get_post_query, (post_id,))
    connection.commit()
    post = cursor.fetchone()
    if post:
        print(f"Ваш пост : {post}")
        connection.close()
        return True
    else:
        print("Таког айди нет")
        connection.close()
        return False


def update_post(post_id: int, new_title: str, new_content: str) -> str:
    update_post_query = """
    UPDATE posts SET title = (?), content = ? where posts_id = ?
    """
    connection = sqlite3.connect(DB_path)
    cursor = connection.cursor()

    cursor.execute(
        update_post_query,
        (
            new_title,
            new_content,
            post_id,
        ),
    )
    updated_rows_count = cursor.rowcount
    connection.commit()
    if not updated_rows_count:
        return "пост не найден"
        connection.close()
    else:
        return f"Новая коллона на айди: {post_id} сделанна"
        connection.close()
