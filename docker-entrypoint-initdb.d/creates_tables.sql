CREATE TABLE IF NOT EXISTS user(
    user_ID INT NOT NULL,
    name varchar(250),
    email varchar(254),
    age INT,
    country varchar(250),
    spotify_client_id varchar(32) NOT NULL,
    spotify_client_secret varchar(32) NOT NULL,
    PRIMARY KEY (user_ID),
);

CREATE TABLE IF NOT EXISTS playlist(
    playlist_id INT NOT NULL,
    title varchar(50),
    duration INT,
    number_of_tracks INT,
    cover_image varchar(200),
    PRIMARY KEY (user_ID),
    CONSTRAINT fk_user,
        FOREIGN KEY(user_id) 
	        REFERENCES user(user_id)	
);

CREATE TABLE IF NOT EXISTS track(
    track_id INT NOT NULL,
    title varchar(50),
    artist_id varchar(50),
    artist_name varchar(50),
    album_id varchar(50),
    album_name varchar(50),
    duration INT,
    number_of_tracks INT,
    cover_image varchar(200),
    PRIMARY KEY (track_id),
    CONSTRAINT fk_playlist,
        FOREIGN KEY(playlist_id) 
	        REFERENCES user(playlist_id)	
);
