CREATE TABLE imdb_df (
	movie_name TEXT PRIMARY KEY,
	rating FLOAT
)

CREATE TABLE nyt_df (
	movie_names TEXT,
	mpaa_rating TEXT,
	critics_pick INT,
	byline TEXT,
	headline TEXT,
	summary_short TEXT
)

CREATE TABLE rotten_df (
	movie_name TEXT,
	meter_class TEXT,
	meter_score INT
)

SELECT * FROM rotten_df

SELECT DISTINCT imdb_df.movie_name, imdb_df.rating, rotten_df.meter_class, rotten_df.meter_score, nyt_df.critics_pick, nyt_df.byline, nyt_df.headline, nyt_df.summary_short
FROM imdb_df
INNER JOIN rotten_df
ON imdb_df.movie_name = rotten_df.movie_name
INNER JOIN nyt_df
ON imdb_df.movie_name = nyt_df.movie_names
