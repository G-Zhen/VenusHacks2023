# VenusHacks2023

<h1> Meals4Me </h1>
Daily meal planner for breakfast, lunch, dinner, snacks.
Navigating college life is difficult, to say the least. What's even harder is navigating it with an empty stomach. That's why we created Meals4Me. 
Meals4Me helps students, or anyone, with choosing a meal for the day whether you're craving breakfast, lunch, dinner, or a snack. We hope this will encourages users to stay healthy and well-fed.

<h2> Members </h2>
Grace Zhen, Jamie Phan, Sabrina Tang, Lilya Chakhoyan

<h2> Front-end </h2>
Web site with 3 pages: a main page "Meals4Me" that links to other pages in our site, an "The Team" page with site mission and member LinkedIns, and the main functionality of our site that generates recipes in "Create Meals4Me". <br />
This site's front end was developed with only HTML, CSS, and JavaScript.

<h2> Back-end </h2>
This site uses the spoonacular recipe and food API: https://spoonacular.com/food-api and Flask to provide routing capabilities to map URLs to implement the API <br />
<h3> Run this site locally </h3>
If running this code, you must run Flask first (aka app.py) in order to run the front-end side; especially for "Create Meals4Me" page which uses the API.
Requirements: Python 3 <br />
You must always run app.py for the buttons in our Create Meals4Me page. 
Run app.py (for Mac OS): 

```
cd BackEnd
pip install -r requirements.txt
source venv/bin/activate
python app.py

```
After running app.py, run homepage.html file by opening the actual file.  

<h1> Git basics for members </h1>
<h3> Setup </h3>
    1. Download the repo: **git clone [url: grab the url from the green "<> Code" button]** <br />
    2. Move to repo, go to terminal and type: **cd VenusHacks2023**

<h3> Upload Changes you made for everyone to see </h3>
    1. Check if you have anything to upload: git status <br />
    2. If you have changes (from making a new file or adding new code): git add . <br />
    3. Tell us what changes you made with a message: git commit -m "Some Message"<br />
    4. Upload your code to GitHub: git push <br />

<h3> Update your local code after someone else has made changes. </h3>
Do this often and do it before you push: **git pull**



