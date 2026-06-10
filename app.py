from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load movie data
movies = pickle.load(open('movies.pkl', 'rb'))

# Generate similarity matrix at startup
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []

    if request.method == 'POST':
        movie_name = request.form['movie']
        recommendations = recommend(movie_name)

    return render_template(
        'index.html',
        movies=movies['title'].values,
        recommendations=recommendations
    )

if __name__ == '__main__':
    app.run(debug=True)