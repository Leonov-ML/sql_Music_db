from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://userone:userOne@localhost:5432/homework3')

connection = engine.connect()

# название и год выхода альбомов, вышедших в 2018 году;
album_from_2018 = connection.execute('''SELECT title, year
    FROM Albums
    WHERE year = 2018
    ''').fetchall()

print(f'Название и год выхода альбомов, вышедших в 2018 году: {album_from_2018}')

# название и продолжительность самого длительного трека;
max_long_song = connection.execute('''SELECT title, duration 
    FROM Songs
    ORDER BY duration DESC
    LIMIT 1;
    ''').fetchone()

print(f'Название и продолжительность самого длительного трека: {max_long_song}')

# название треков, продолжительность которых не менее 3,5 минуты(210сек);
long_tack = connection.execute('''SELECT title, duration
    FROM Songs
    WHERE duration >= 210''').fetchall()

print(f'название треков, продолжительность которых не менее 3,5 минуты(210сек): {long_tack}')

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
colection_between = connection.execute('''SELECT title
    FROM Collections
    WHERE year BETWEEN 2018 AND 2020''').fetchall()

print(f'Названия сборников, вышедших в период с 2018 по 2020 год включительно: {colection_between}')

# исполнители, чье имя состоит из 1 слова;
nickname_one_word = connection.execute('''SELECT name
    FROM Performers
    WHERE name NOT LIKE '%% %%';''').fetchall()

print(f'Исполнители, чье имя состоит из 1 слова: {nickname_one_word}')

# название треков, которые содержат слово "мой"/"my".
my_track = connection.execute('''SELECT title
    FROM Songs
    WHERE title LIKE '%%my%%' OR title LIKE '%%мой%%';''').fetchall()

print(f'Название треков, которые содержат слово "мой"/"my": {my_track}')
