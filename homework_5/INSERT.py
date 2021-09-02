from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://userone:userOne@localhost:5432/homework3')

connection = engine.connect()
connection.execute('''INSERT INTO Genres(title)
	VALUES ('Pop'),
	('Classical'),
	('Rock'),
	('Jazz'),
	('Latin'),
	('Hip Hop'),
    ('Country'),
	('Reggae'),
	('Indie'),
	('Blues');
	''')

connection.execute(''' INSERT INTO Performers(name)
    VALUES ('Pink Floyd'),
    ('Queen'),
    ('Nirvana'),
    ('Eric Clapton'),
    ('AC/DC'),
    ('Miles Davis'),
    ('Norah Jones'),
    ('ABBA'),
    ('Boston'),
    ('Enya');
    ''')

connection.execute(''' INSERT INTO Albums (title, year)
    VALUES ('Miami 1994', '1994'),
    ('Old Blue', '2018'),
    ('74 Jailbreak', '2009'),
    ('Miles Ahead', '2008'),
    ('Til We Meet Again', '2018'),
    ('GOLD', '1992'),
    ('Pulse', '1998'),
    ('Greatest Hits II', '2020'),
    ('Nevermind', '2019'),
    ('Storms In Africa', '1989');
    ''')

connection.execute(''' INSERT INTO Collections (title, year)
    VALUES ('Country home', '2014'),
    ('Reggae and blues', '2000'),
    ('Indie collection', '2015'),
    ('Rock collection', '2020'),
    ('Disco dance', '2018'),
    ('Fusion music', '2016'),
    ('Pop art', '1998'),
    ('Blues home', '2018'),
    ('Classical collection 1', '2018'),
    ('Classical collection 2', '2019'),
    ('Classical rap', '2017'),
    ('Rap collection', '2018');
    ''')

connection.execute(''' INSERT INTO Songs(title, duration, album_id)
    VALUES('Astronomy domine Barrett', '238', '1'),
    ('Learning to fly Gilmour ', '317', '1'),
    ('Learning To Fly', '316', '2'),
    ('Keep Talking', '376', '2'),
    ('One Vision', '267', '3'),
    ('Tie Your Mother Down', '236', '3'),
    ('Sappy', '209', '4'),
    ('Cold, Cold Heart', '325', '8'),
    ('It Was You', '338', '8'),
    ('Dancing Queen', '358', '9'),
    ('Knowing Me, Knowing You', '123', '9'),
    ('Blood For Blood', '159', '10'),
    ('Stay away', '215', '4'),
    ('What do you want from my Gilmour', '259', '1'),
    ('Shine On You Crazy Diamond', '795', '2'),
    ('What Do You Want From my', '250', '2'),
    ('Badge', '417', '5'),
    ('Wonderful Tonight', '541', '5'),
    ('Jailbreak', '285', '6'),
    ('You Aint Got a Hold On my', '216', '6'),
    ('Vierd Blues', '412', '7'),
    ('Diane', '467', '7'),
    ('Tommy and The Terrors', '231', '10');
    ''')

connection.execute(''' INSERT INTO Album_performers (Performer_id, Album_id)
    VALUES('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10');	;
    ''')

connection.execute(''' INSERT INTO Genre_performer (Performer_id, Genre_id)
    VALUES ('1', '3'),
    ('2', '1'),
    ('3', '3'),
    ('4', '6'),
    ('5', '5'),
    ('6', '3'),
    ('7', '4'),
    ('8', '8'),
    ('9', '10'),
    ('10', '9'),
    ('2', '3'),
    ('2', '6');
    ''')

connection.execute(''' INSERT INTO Song_collection (collection_id, song_id)
    VALUES ('1', '2'),
    ('1', '5'),
    ('1', '3'),
    ('2', '2'),
    ('2', '10'),
    ('2', '11'),
    ('2', '6'),
    ('3', '5'),
    ('3', '7'),
    ('4', '8'),
    ('4', '7'),
    ('5', '9'),
    ('5', '10'),
    ('6', '2'),
    ('6', '3'),
    ('7', '2'),
    ('7', '1'),
    ('8', '11'),
    ('8', '5'),
    ('9', '6'),
    ('9', '7'),
    ('10', '10'),
    ('10', '11'),
    ('11', '4'),
    ('11', '2');
    ''')
