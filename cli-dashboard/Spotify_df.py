from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, desc


class Spotify_df:
    def __init__(self):
        self.__session = SparkSession.builder.appName('dashboard').getOrCreate()
        try:
            self.__df = self.__session.read.csv('../content/.f_spotifyzipcodes', header=True, inferSchema=True)
        except:
            print("File not found or not existing")
        self.__session.sparkContext.setLogLevel("ERROR")
            
            
        self.__df = (
            self.__df
            .withColumn('popularity', col('popularity').cast('int'))
            .withColumn('duration_ms', col('duration_ms').cast('int'))
            .withColumn('danceability', col('danceability').cast('double'))
            .withColumn('energy', col('energy').cast('double'))
            .withColumn('loudness', col('loudness').cast('double'))
            .withColumn('speechiness', col('speechiness').cast('double'))
            .withColumn('acousticness', col('acousticness').cast('double'))
            .withColumn('liveness', col('liveness').cast('double'))
            .withColumn('valence', col('valence').cast('double'))
        )

    @property
    def df(self):
        return self.__df

    def most_popular_genre(self, n): 
        genre_avg_popularity = self.df.groupBy('track_genre') \
            .agg(avg(col('popularity')).alias('avg_popularity')) \
            .orderBy(col('avg_popularity').desc())

        track_genres = [row['track_genre'] for row in genre_avg_popularity.limit(n).collect()]
        avg_popularities = [row['avg_popularity'] for row in genre_avg_popularity.limit(n).collect()]

        return track_genres, avg_popularities

    def top_popular_songs_of_less_popular_genre(self, n):
        genre_avg_popularity = self.df \
            .groupBy('track_genre') \
            .agg(avg(col('popularity')).alias('avg_popularity'))\
            .orderBy(col('avg_popularity')).limit(n).collect()  
        genres = [row['track_genre'] for row in genre_avg_popularity]
        result = []
        
        for genre in genres:
            result.append(self.df.select('artists', 'track_name', 'popularity', 'track_genre').orderBy(col('popularity').desc()).where(col('track_genre') == genre).collect()[0])
        
        artists = [row['artists'] for row in result]
        track_name = [row['track_name'] for row in result]
        popularity = [row['popularity'] for row in result]
        track_genre = [row['track_genre'] for row in result]
        
        return artists, track_name, popularity, track_genre
    
    def distribution_of_explicit_songs(self):
        count = self.df.groupBy('explicit').count().collect()
        
        explicit = [row['explicit'] for row in count]
        counts = [row['count'] for row in count]
        
        return explicit, counts
    
    def top_artist_by_popularity(self, n):
        genre_avg_popularity = self.df.groupBy('artists') \
            .agg(avg(col('popularity')).alias('avg_popularity')) \
            .orderBy(col('avg_popularity').desc())

        artists = [row['artists'] for row in genre_avg_popularity.limit(n).collect()]
        avg_popularities = [row['avg_popularity'] for row in genre_avg_popularity.limit(n).collect()]
        
        return artists, avg_popularities
        
    def top_popular_songs_by_artist(self, artists, n):
        tracks = self.df.select('track_name', 'popularity', 'track_genre').where(col('artists').contains(artists)).orderBy(col('popularity')).limit(n).collect()
        
        track_name = [row['track_name'] for row in tracks]
        track_genre = [row['track_genre'] for row in tracks] 
         
        return track_name, track_genre
        
            
        
