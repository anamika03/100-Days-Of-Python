from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    random_num = random.randint(1, 100)
    return render_template("index.html", number=random_num, year=current_year)

# Fixed: Added the <name> variable to the URL path
@app.route('/guess/<name>')
def guess(name):
    # Fetch Gender
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data.get("gender", "unknown")
    
    # Fetch Age
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data.get("age", "unknown")
    
    # Generate missing data for guess.html
    current_year = datetime.datetime.now().year
    random_num = random.randint(1, 100)
    
    # Pass everything to the template
    return render_template(
        "guess.html", 
        person_name=name, 
        gender=gender, 
        age=age, 
        number=random_num, 
        year=current_year
    )

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/2af1ec1385e364b76df5"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
