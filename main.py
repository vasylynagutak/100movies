import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movie_titles)


with open("../../Desktop/Python/PycharmProjects/100movies/movies.txt", mode="w") as file:
    try:
        for movie in movies:
            file.write(f"{movie}\n")
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")



