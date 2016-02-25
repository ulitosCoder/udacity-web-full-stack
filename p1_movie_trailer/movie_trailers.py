import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
			"a story of a boy and his toy that come to life",
			"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=KYz2wyBy3kc")
					
avatar = media.Movie("Avatar",
                     "A marine as an alien it a planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
					 
dances_w_wolves = media.Movie("Dances with wolves",
							  "A Civil War soldier develops a relationship with a band of Lakota Indians",
							  "https://upload.wikimedia.org/wikipedia/en/8/82/Dances_with_Wolves_poster.jpg",
							  "https://www.youtube.com/watch?v=J0obOvGGb1U")


ratatouille = media.Movie("Ratatouille",
			  "Remy is an idealistic and ambitious young rat, gifted with highly developed senses of taste and smell",
			  "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
			  "https://www.youtube.com/watch?v=c3sBBRxDAqk")


bolt = media.Movie("Bolt",
                   "The days of canine superstar Bolt (John Travolta) are filled with danger and intrigue ... until the cameras stop rolling",
                   "https://upload.wikimedia.org/wikipedia/en/4/44/Bolt_ver2.jpg",
                   "https://www.youtube.com/watch?v=zm51H0dIzYQ")

ts3 = media.Movie("Toy Story 3",
                  "With their beloved Andy preparing to leave for college, Woody (Tom Hanks), Buzz Lightyear (Tim Allen), Jessie (Joan Cusack), and the rest of the toys find themselves headed for the attic but mistakenly wind up on the curb with the trash",
                  "http://www.gstatic.com/tv/thumb/movieposters/3546307/p3546307_p_v8_aa.jpg",
                  "https://www.youtube.com/watch?v=JcpWXaA2qeg")

movies = [ts3, bolt, ratatouille, toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)

