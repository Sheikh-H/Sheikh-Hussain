import sqlite3
from dotenv import load_dotenv

load_dotenv()


def connect_database():
    connection = sqlite3.connect("instance/portfolio.db")
    connection.row_factory = sqlite3.Row
    return connection


def all_tags():
    connection = None
    result = []
    query = []
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute("""SELECT tags FROM projects;""")
        tags = cursor.fetchall()
        items = []
        for tag in tags:
            items.append(tag["tags"].split(","))
        for item in items:
            for tag in item:
                result.append(tag)
        result = set(result)
        for tag in result:
            query.append(tag)
        return query
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def search_projects(search="", tag=""):
    query = "SELECT * FROM projects WHERE 1=1"
    params = []
    if search:
        query += " AND (LOWER(title) LIKE ? OR LOWER(description) LIKE ? OR LOWER(tags) LIKE ?)"
        params.append(f"%{search}%")
        params.append(f"%{search}%")
        params.append(f"%{search}%")
    if tag:
        query += " AND LOWER(tags) LIKE ?"
        params.append(f"%{tag}%")
    query += " ORDER BY featured DESC, id DESC;"
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute(query, params)
        projects = cursor.fetchall()
        return projects
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def get_projects(limit=None):
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        if limit:
            cursor.execute(
                """SELECT * FROM projects ORDER BY featured DESC, id DESC LIMIT ?;""",
                (limit,),
            )
        else:
            cursor.execute(
                """SELECT * FROM projects ORDER BY featured DESC, id DESC;"""
            )
        projects = cursor.fetchall()
        return projects
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def get_project(id):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
        """SELECT * FROM projects WHERE id = ?;""",
        (id,),
    )
    project = cursor.fetchone()
    connection.close()
    return project


def delete_project(id):
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute(
            """DELETE FROM projects WHERE id = ?;""",
            (id,),
        )
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def update_project(project):
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute(
            """UPDATE projects SET title = ?, description = ?, image_url = ?, github_link = ?, demo_link = ?, completion = ?, tags = ?, featured = ? WHERE id = ?;""",
            (
                project["title"],
                project["description"],
                project["image_url"],
                project["github"],
                project["demo"],
                project["completion"],
                project["tags"],
                project["featured"],
                project["id"],
            ),
        )
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def insert_project(project):
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO projects (title, description, image_url, github_link, demo_link, completion, tags, featured) VALUES (?,?,?,?,?,?,?,?);""",
            (
                project["title"],
                project["description"],
                project["image_url"],
                project["github"],
                project["demo"],
                project["completion"],
                project["tags"],
                project["featured"],
            ),
        )
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def get_skills():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM skills;""")
    skills = cursor.fetchall()
    connection.close()
    return skills


def get_skill(id):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
        """SELECT * FROM skills WHERE id = ?;""",
        (id,),
    )
    skill = cursor.fetchone()
    connection.close()
    return skill


def insert_skill(skill, progress):
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO skills (skill, progress) VALUES (?, ?);""",
            (
                skill,
                progress,
            ),
        )
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def update_skill(id, skill, progress):
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute(
            """UPDATE skills SET skill = ?, progress = ? WHERE id = ?""",
            (
                skill,
                progress,
                id,
            ),
        )
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def delete_skill(id):
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute(
            """DELETE FROM skills WHERE id = ?;""",
            (id,),
        )
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()


def get_user():
    connection = None
    try:
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM admin;""")
        admin = cursor.fetchone()
        return admin
    except Exception as e:
        print(e)
        return False
    finally:
        if connection:
            connection.close()
