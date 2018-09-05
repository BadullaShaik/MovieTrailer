import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story","A story os a boy and his toys that come to life",
                    "https://i.ytimg.com/vi/DVrSkd0s7Yg/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDJxkljuAp8CbAEnO5mEDLGCu8Q2Q",
                    "htpps://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

katamraudu=media.Movie("Katamrayudu",
                       "It is Beautuful love song",
                       "https://i.ytimg.com/an_webp/zggQw2wb60M/mqdefault_6s.webp?du=3000&sqp=CNvB38wF&rs=AOn4CLBWftRK4RY4AQS3ayrw1-9HPK8WRQ",
                       "https://www.youtube.com/watch?v=zggQw2wb60M")

#print(katamraudu.storyline)

#katamraudu.show_trailer()

movies=[toy_story,katamraudu]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
