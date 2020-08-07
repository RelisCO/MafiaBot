import sqlite3
from random import shuffle
from config import database_name
from config import shelve_name
import roles
import shelve
import os


def add_row(player_id: str, chat_id: str):
    """Добавление информации о новом игроке"""
    sql = """INSERT INTO Players (id, chat)
    VALUES (?, ?);"""

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(sql, (player_id, chat_id))
    conn.commit()
    conn.close()


def delete_chat(chat_id: str):
    """Удаление информации о всех участниках чата"""
    sql = """DELETE FROM Players
    WHERE chat = (?);"""

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(sql, (chat_id,))
    conn.commit()
    conn.close()


def check_player(player_id):
    """Проверка, является ли пользователь участником какой-то игры"""
    sql = """SELECT *
    FROM Players
    WHERE id = (?);"""

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    result = cursor.execute(sql, (player_id,)).fetchall()
    conn.commit()
    conn.close()
    return True if result else False


def get_chat(player_id: str):
    """Возвращает чат в котором играет пользователь"""
    sql = """SELECT chat
    FROM Players
    WHERE id = (?);"""

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    result = cursor.execute(sql, (player_id,)).fetchall()
    conn.commit()
    conn.close()
    return result[0][0] if result else result


def start_game(chat_id: str, players_id: list):
    """Создание новой игры"""
    assert roles.minimum <= len(players_id) <= roles.maximum, 'Incorrect count of players'
    game_roles = roles.roles[str(len(players_id))]
    shuffle(game_roles)
    with shelve.open(shelve_name+f'{chat_id}') as game:
        for player, role in zip(players_id, game_roles):
            game[player] = [role, 'alive']  # Каждый игрок имеет роль и статус жизни


def end_game(chat_id: str):
    """Удаление информации об игре"""
    try:
        os.remove(shelve_name+f'{chat_id}.bak')
        os.remove(shelve_name + f'{chat_id}.dat')
        os.remove(shelve_name + f'{chat_id}.dir')
    except FileNotFoundError:
        pass


def kill_player(chat_id: str, player_id: str):
    """Смена статуса жизни игрока на 'убит'"""
    with shelve.open(shelve_name+f'{chat_id}') as game:
        game[player_id][1] = 'killed'
