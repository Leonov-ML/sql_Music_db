CREATE TABLE Genres (
id SERIAL PRIMARY KEY,
Name varchar(50)
);

CREATE TABLE Performers (
id SERIAL PRIMARY KEY,
Name varchar(100)
genreid integer REFERENCES Genres(id),
);

CREATE TABLE Albums (
id SERIAL PRIMARY KEY,
Title varchar(255),
Year int,
Genres varchar(50),
performerid integer REFERENCES Performers(id),
);

CREATE TABLE Songs (
id SERIAL PRIMARY KEY,
Tite varchar(255),
Duration integer,
albumid integer REFERENCES Albums(id),
);
