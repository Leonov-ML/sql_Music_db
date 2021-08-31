CREATE TABLE Performers (
	id SERIAL PRIMARY KEY,
	Name varchar(50) NOT NULl UNIQUE
);

CREATE TABLE Albums (
	id SERIAL PRIMARY KEY,
	Title varchar(50) NOT NULL,
	Year integer NOT null,
);

CREATE TABLE album_Performers (
	Performer_id integer REFERENCES Performers(id) NOT NULL,
	Album_id integer REFERENCES Albums(id) NOT NULL,
	CONSTRAINT Album_musician_pk PRIMARY KEY (Performer_id, Album_id)
);

CREATE TABLE Songs (
	id SERIAL PRIMARY KEY,
	Title varchar(50) NOT NULL,
	Duration integer NOT NULL,
	Album_id integer REFERENCES Albums(id) NOT NULL
);

CREATE TABLE Collections (
	id SERIAL PRIMARY KEY,
	Title varchar(50) NOT NULL,
	Year integer NOT NULL
);

CREATE TABLE Song_collection (
	Collection_id integer REFERENCES Collections(id) NOT NULL,
	Song_id integer REFERENCES Songs(id) NOT NULL,
	CONSTRAINT Song_collection_pk PRIMARY KEY (Collection_id, Song_id)
);

CREATE TABLE Genres (
	id SERIAL PRIMARY KEY,
	title varchar(50) NOT NULL
);

CREATE TABLE Genre_performer (
	Performer_id integer REFERENCES Performers(id) NOT NULL,
	Genre_id integer REFERENCES Genres(id) NOT NULL,
	CONSTRAINT Genre_performer_pk PRIMARY KEY (Performer_id, Genre_id)
);
