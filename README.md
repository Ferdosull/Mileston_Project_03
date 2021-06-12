# Milestone Project 03 

### Smoothies, Shakes and Juices Community (SS&J)<br/><br/>

## Table of contents
1. [Introduction](#intro)
2. [Responsive Design](#responsive_design)
3. [My Project Description and Design](#project_description)
    1. [Wire Frames](#wire_frame)
    2. [Pop up Modals](#pop_modal)
    3. [Nav Bar](#nav_bar)
    4. [Hero Image](#hero_image)
    5. [Header & Description Text](#header_description)
    6. [Page Links and Button Navigation](#page_links)
    7. [flash_messages](#flash_messages)
    8. [Search Recipes](#search_recipes)
    9. [Default Recipe Image](#default_recipe)
    10. [Footer](#footer)
4. [Utilising the 5 Planes of UX Design](#ux_design)
    1. [The Strategy Plane](#strategy_plane)
    2. [The Scope Plane](#scope_plane)
    3. [The Structure Plane](#structure_plane)
    4. [The Skeleton Plane](#skeleton_plane)
    5. [The Surface Plane](#surface_plane)
5. [Typography](#typography)
6. [User Stories](#user_stories)
    1. [External User's Goal](#external_user_goal)
    2. [App Owner's Goal](#app_owner_goal)
    3. [First Time User Goals](#first_time_user_goals)
    4. [Returning User Goals](#returning_user_goals)
    5. [Frequent User Goals](#frequent_user_goals)
7. [Bugs and Fixes](#bug_fixes)
8. [References and Credits Section](#references_and_credits)
    1. [Code](#code)
    2. [Media](#media)
9. [User Testing](#testing)
    1. [Website Responsiveness through Browser and Device Compatibility](#testing_procedure)
    2. [Call to Action Functionality Testing](#testing_user_stories)
    3. [HTML CSS and JavaScript Validation](#validation)
10. [Future "Nice to Have" Additions to The Website](#additions)
11. [Deployment of Project](#project_deployment)
    1. [Creating a New Project](#new_project)
    2. [Commands Utilised Throughout The Project After Changes](#commands)
    3. [How to Deploy My Milestone\_Project\_03 on Heroku](#how_to_deploy)
    4. [How to Download, View and Edit and Run this project locally](#how_to_download)
12. [My Data Base Layout and Structure](#db_structure)<br/><br/>
13. [Previous Assessment Comments and How I Have Addressed Them](#previous_comments)<br/><br/>
14. [Acknowledgements](#acknowledgements)<br/><br/>

## Introduction <a name="intro"></a>

My Milestone Project 3 was envisioned by me and created based on the knowledge gained so far from this course. 
I have taken the fundamentals that I have learned from the course and applied them to this website with style and format changes. 
I have created Python, Jscript and jQuery functions where required to manipulate data, undertake logic and enable the end result back to the user.
I hope that the outcome of my works has translated into a web application UI, that shows and facilitates the CRUD functionality learned throughout the backend development module.
I feel by creating custom, re-usable python code and efficiently structuring my DataBase, I have created a system that could be scalable with minimal effort.
My goal was to create an application that visually appears accessible, responsive and easy to navigate through the use of HTML, CSS and Javascript.
As well as the course materials, there have been some additional code examples which I have searched for online and utilised.
These additions have been highlighted and referenced later on in this document (references and credits section).
As well as these additions I have received excellent feedback from my mentor Maranatha Ilesanmi.
Maranatha has re-capped and explained the reasons for the comments I received from my last Milestone Project and has advised how to improve so that a distinction may be achieved this time around.
I have also added a [section](#previous_comments) in this README file, where I explain what has been implemented in this project to counter act the reasons for falling down in the last project.

## Responsive Design <a name="responsive_design"></a>

As can be seen in the screenshot below, media queries and Materialize classes have been used to ensure that the website is completely responsive across Desktop and Mobile devices.

![](static/images/readme_images/README001.png)

View the deployed project here:[ SS&J ](https://smoothies-shakes-and-juices.herokuapp.com/)<br/><br/>

## My Project Description and Design <a name="project_description"></a>

The SS&J website is a full-stack responsive website which utilises Python, JQuery & javasript methods and functions to carry out CRUD functionality using the Flask framewok and MongoDB Atlas. 
Please see initial envisioned wireframes for desktop and mobile devices (before project start) and actual screenshots of the finished website in the sections that follow:
<br/><br/>

### Wire Frames <a name="wire_frame"></a>

![](static/images/readme_images/README002.png)

The wire-frames I found very useful for planning the structure and navigation required to make the CRUD functionality efficient and easy to follow. 
I wanted my main page to be the centre hub until logged in. Once logged-in, the users new centre hub becomes the profile page, which is essentially the main page without the search bar or hero image.
A number of redirects are used and placed in known locations that users that would be familiar with in keeping with good practise.
<br/><br/>

### Pop up Modals <a name="pop_modal"></a>

![](static/images/readme_images/README003.png)

There are 2 pop up modals used on this application, The first encountered modal (base.html template) is triggered by a brightly coloured button in the task bar (desktop) or inside the hamburger menu on mobile.
The brightly coloured button is a way to catch the eye of the user and to try and attract them to click on it. Once they click on the button a modal appears which describes the offer
available to them as an SS&J community contributer. If they are an existing user there is information on how to proceed with the offer. 
If they are not an existing user they are presented with a link for joining the community and availing of the offer.

The second modal is linked to the profile page and it is triggered by pressing the "Delete" button for a specific recipe. 
It is a way of protecting against accidental deletion of a recipe. It provides the user with a way of opting out if delete was pressed accidentally 
and a way of giving the user a second chance if they had decided to delete the recipe but now have changed their mind.

<br/><br/>

### Nav Bar <a name="nav_bar"></a>

![](static/images/readme_images/README004.png)

For this project I have decided to go with a Fixed nav-bar. Once the page is scrolled the navbar follows. 
I felt that having the navbar accessible from all locations on a scrolled page would be of benefit to the user.
It would mean easy access to the "Home", "Profile", "New Recipe" and "Log-Out" pages once logged in.
The nav-bar can be separated up into desktop and mobile views as seen below. 
The "HOME" button re-loads the main recipe page and re-directs you here if clicked from another location.
The "Profile" button navigates the user to their profile page to carry out CRUD actions.
The "New Recipe" button navigates the user to the New Recipe page where recipe details can be entered and saved.
The "Log In" button navigates the user to the log-in page so that username and password details can be entered.
The "Log Out" button uses the "session.pop" method to remove a signed-in user from the application and re-directs to the login page.
The "Sign-up" button navigates the user to the Sign-up page where a new SS&J account can be created.
The "Special Offer!" button pops up a modal which details information about how existing and new users can avail of cost reduction when purchasing items from Kitchen Aid.

<br/><br/>

### Hero Image <a name="hero_image"></a>

![](static/images/readme_images/README005.png)

The Hero Image that loads upon display of the main page is of an outdoor wooden style picnic bench with lots of fruit and glass bottles of juice on display. 
I have made this image semi-transparent to allow the green background colour to seep through a little, keeping everything flowing and in tune with the colour scheme. 
The image is responsive accross all sizes of device by utilising dedicated Materialize classes.

<br/><br/>

### Header & Description Text <a name="header_description"></a>

![](static/images/readme_images/README006.png)

The Header text, when first landed on the page, is the name of the user community, "Smoothies, Shakes & Juices" and the description text below it is a small summary of 
what the community are about and where they are headed. The goal here is to encourage more users to join and spread the word.
<br/><br/>


### Page Links and Button Navigation <a name="page_links"></a>

![](static/images/readme_images/README007.png)

In the image above I have detailed all the href, onClick and submit button navigations used in this project. 
All links have been incorporated with huge consideration to the users overall experience and ease of use.
It is my intention here to have the user feel a sense of familiarity by keeping everything quite similar to UI's, websites and layouts that I am familiar with using.
I have tried to make sure that every feature here conforms to modern best practise standards.
All links have been tested and are fully functional. The social media links in the footer open in separate tabs where required.
<br/><br/>

### Flash Messages <a name="flash_messages"></a>

![](static/images/readme_images/README008.png)

The Flash messages being presented back have been styled to be more pleasing to the user. The style format is based on the appearance of well known Toastr messages.
They appear consistently at the top of the screen and convey a successfull transaction from the users input.
They are green in colour and have a font awesome tick which is widely associated with success. 
I have also written a JavaScript function to hide the message if the user wishes to click on the "X" located at the top right of the message.
<br/><br/>

### Search Recipes <a name="search_recipes"></a>

![](static/images/readme_images/README009.png)

The search recipes search bar will query the index that I have created on my MongoDB database.
I created the index through the python3 command line in Gitpod.
The index is made up of "value" sections based on three "keys". The type being "text".
The three keys are: main_component_type, drink_name, and ingredients.
I feel that these keys will provide adequate results as most users are going to search by ingredients. 
The main component type will have the root ingredient also.
The drink name is for returning users who retain names of the drinks from a glance and search by it the next time around.
<br/><br/>

### Default Recipe Image <a name="default_recipe"></a>

![](static/images/readme_images/README010.png)

The default recipe image is used for times when the user may not have a picture hosted online to represent their drink.
By simply clicking on the "Image URL" text link on the "New Recipe" page, the URL input gets populated with a known string and the div containing the input becomes hidden.
<br/><br/>

### Footer <a name="footer"></a>

![](static/images/readme_images/README011.png)

I have kept the footer quite simplistic on purpose here so as not to distract from what is taking place on the main page.
While remaining simplistic all its functions work really well. 
Its contains the following:
1. Heading text
2. A description of the community
3. A link for signing up
4. An auto populated email form
5. social media links.
6. scroll to top JS function link.

<br/><br/>

![](static/images/readme_images/EMAIL.png)
<br/><br/>

## Utilising the 5 Planes of UX Design <a name="ux_design"></a>

**The Strategy Plane** <a name="strategy_plane"></a>

The strategy plane here is concerned with attracting like minded individuals to sign-up with the SS&J community and contribute to the growing recipe collection.
The main business objective here is to build a large community and expose them to weekly special offers.
As the community grows into large numbers I would envision creating additional partnerships with raw materials and blender outlets 
in order to increase revenues generated, by offering discounts to users on behalf of these partners. The use of the users "username" at checkout ensures a return for SS&J.

**The Scope Plane** <a name="scope_plane"></a>

The app, I feel, utilises modern techniques to be in line with what is current, and trys to enhance the users experience by keeping everything familiar. 
The navbar will be a very familiar feature to most users and incorporates the necessary links for logging in and signing up.
The search bar I have kept familiar looking also and the buttons describe exactly what to expect when the user presses them.
The displayed recipes on both the main page and profile pages have intuitive buttons associated with them. The buttons are tooltipped in the profile page for additional info.
Upon all user interactions where a submission occurs (Log In, Log Out, CRUD) the user is presented with flash messages to confirm that their input was successful.
Both the "New Recipe" and "Edit Recipe" pages are designed in a way that reflects an actual physical recipe book. 
I feel this provides a more familiar feel and its nice to keep some of that old school influence in digital format.

**The Structure Plane** <a name="structure_plane"></a>

This app is a multi-page page layout that extends from the base template. I have tried to keep everything simplistic and familiar.
It is navigated from top to bottom with a fixed nav-bar at the top and a footer at the bottom. 
The nav-bar turns into a mobile friendly toggler once below a specific resolution. Underneath the nav-bar is where the “Hero-Image” is located. 
In desktop mode, the hero image is where the header text and info paragraph can be found.
In mobile view, the header text and info paragraph move to below the responsive image. 
I feel the clarity in the text is retained by not re-sizing in conjunction with the image.

The hero image, header text and info paragraph are only visible on the main page. The items common to all pages are the navbar, footer and special offer! modal only. 
Below the info paragraph, on the main page, the recipe search input field can be found and below that, all submitted recipes in the same format.
The format is: drink_name:, created_by:, user_recommends:, image_url:, see full recipe button.

If you are not a user, you will only have access to this main page, the sign-up page and the log in page.
If you are an existing user, after logging in you will have access to your profile page, 
a create new recipe page template and an edit recipe page where existing recipe data is retrieved for editing purposes.

The profile page is similar to the main landing page minus the hero image, text and search bar.
The profile page will display the recipes which have been submitted by you only. 
In the profile page, the functionality is given to the session user who created the recipe to "Read", "Update" or "Delete" any of your recipes.
By clicking on the "New Recipe" tab the user can carry out the "Create" functionality.

**The Skeleton Plane** <a name="skeleton_plane"></a>

The app will have a consistently placed background image on the main page with two sub sections below it (search bar and all recipes displayed).
The use of [colours](#colours), [fonts](#typography) and responsive elements were carefully chosen to add user expected functionality.
Careful consideration was given to making the content well placed, clear and well presented. This was achieved by utilising contrasting colours, 
right size, style fonts and adequate spacing. In order to try and create a professional sense I was quite selective with the images used from Unsplash.com
Again in this project, the Balsamic [wire frames](#wire_frame) have been a fantastic tool to envision what the end result would be.
There have only been subtle changes to the placement of elements and styles from what was originally envisioned through the wireframes.
The page is scrolled top to bottom and all major elements are center aligned with justified text where it fitted with the look required.

**The Surface Plane** <a name="surface_plane"></a>

The colours and imagery used on this website, I feel, are really in line with the recipe ingredients. I have kept greens as my main colour with a contrasting beige (old lace) as the background.
I have used white in the forms so I think the contrast between white and beige works well and allows separation between the background and the input forms.
The rest of the colours chosen are based on the hero image which had been envisioned and chosen before the colour scheme was finalised.
The palette I chose was created at [www.coolers.co](https://coolors.co/) <a name="colours"></a>

![](static/images/readme_images/COOLERS.png)

I have used background shading and opacity shadows to highlight the hero Image header and the hovering and clicking of items throughout, 
the majority being influenced by Materialize CSS classes with subtle additions in my style.css.
I feel the contrasting colours and backgrounds separate the page elements enough so that they remain individual, yet part of a combined theme.
What I was trying to achieve and convey with the app layout was a mature use of colour which reflects the focal point, which is the ingredients themselves (veg, fruit, coffee, etc.).
Hovering over links, buttons and text selectors causes the elements to change colour, alerting the user to the presence of their mouse pointer.
I have included tool tips where I thought it necessary to further clarify an element or the purpose of a feature.
<br/><br/>

## Typography <a name="typography"></a>

The fonts used for the milestone project are: “Handlee” and “Roboto”.

Both fonts were located and used from Google Fonts:[ Handlee ](https://fonts.google.com/specimen/Handlee?query=hand ) [ Roboto ](https://fonts.google.com/specimen/Roboto?query=roboto)

![](static/images/readme_images/FONT.png)

I felt the contrast between Handlee and Roboto works really well. I initiall picked Handlee based on how the site name looked (alomost like a logo).
I like the inviting and playful nature of Handlee for the not so serious stuff and then the use of easily readable Roboto when more thought and input is required by the user.
I have made subtle changes to the font colors, shadows, sizes and spacings for responsiveness as can be seen on the app and in the style.css sheet. 
<br/><br/>

## User stories <a name="user_stories"></a>

**External user’s goal:** <a name="external_user_goal"></a>

The potential app users will be a group of smoothie, shake or juice makers keen on sharing their home made recipes and learning how to create others. 

**App owner's goal:** <a name="app_owner_goal"></a>

The goal of the app is to establish a community and unite like minded individuals with a passion for home made smoothies, shakes and juices.
As part of the ever growing community you have the option to visit a partnering site (this is a ficticious association which provides SS&J with commission on sales) which offer a discount when checking out online if you input your username.
This is achieved currently by pressing the "Special Offer!" button in the Navbar which triggers the modal pop-up. 
This pop-up advertisement is scalable and can be easily altered to reflect new weekly products, and its trigger mechanism could also be altered to a timer after page load through JavasScript.
It is envisioned that as the community grows that commission will also grow, and advertising will also expand to other potential pertners like Tesco for raw ingredient purchase through an SS&J loyalty card.

![](static/images/readme_images/README012.png)

**First Time User Goals** <a name="first_time_user_goals"></a>

- As a First Time User, I want information about the SS&J community (About Text). [Click for Screenshot](#header_description)
- As a First Time User, I want to read all submitted recipes on the main page. [Click for Screenshot](#hero_image)
- As a First Time User, I want to click on any one of the recipes and open it in its own page. [Click for Screenshot](#page_links)
- As a First Time User, I want to be able to navigate efficiently and cleanly through the apps pages. [Click for Screenshot](#page_links)
- As a First Time User, I want to sign-up to the SS&J community. [Click for Screenshot 1](#nav_bar) [Click for Screenshot 2](#page_links)
- As a First Time User, I want to view my unique profile page. [Click to see tab used](#page_links)
- As a First Time User, I want to create one of my own recipes. [Click to see tab used](#page_links)
- As a First Time User, I want to be able to "Like" other users recipes. [Click to see button used](#page_links)

**Returning User Goals** <a name="returning_user_goals"></a>

- As a Returning User, I want to be able to Log In and view my profile with submitted recipes. [Click for Screenshot](#page_links)
- As a Returning User, I want to check the special offers and visit the partnering site to avail of these offers. [Click for Screenshot](#pop_modal)
- As a Returning User, I want to create another one of my own recipes. [Click for Screenshot](#footer) [Click for Screenshot 1](#nav_bar)
- As a Returning User, I want to read all recipes and new user created recipes, then click to open the recipes that I wish read or undertake. [Click for Screenshot](#hero_image)
- As a Returning User, I want to be able to "Like" other users recipes. [Click to see tab used](#page_links)
- As a Returning User, I want to contact the SS&J community directly with any queries. [Click for Screenshot](#footer)

**Frequent User Goals** <a name="frequent_user_goals"></a>

- As a Frequent User, I want to be able to Log In and view my profile with submitted recipes. [Click to see button used](#page_links)
- As a Frequent User, I want to check the new weekly special offers and visit the partnering site to avail of these offers. [Click for Screenshot](#pop_modal)
- As a Frequent User, I want to view all recipes and new user submitted recipes, then click to open the recipes that I wish read or undertake.
- As a Frequent User, I want to be able to "Like" other users recipes. [Click to see button used](#page_links)
- As a Frequent User, I want to see when a particular recipe is displayed, if I have "Liked" it or not. [Click to see button used](#page_links)
- As a Frequent User, I want to create another one of my own recipes. [Click to see tab used](#page_links) [Click for Screenshot 1](#nav_bar)
- As a Frequent User, I want to be able to edit and update one of my existing recipes. [Click to see tab used](#page_links) [Click for Screenshot 1](#nav_bar)
- As a Frequent User, I want to be able to delete one of my existing recipes. [Click to see tab used](#page_links)
- As a Frequent User, I want to contact the SS&J community directly with any queries. [Click for Screenshot](#footer)
<br/><br/>

## Bugs and Bug Fixes <a name="bug_fixes"></a>

During the creation of this project I encountered alot of self inflicted bugs due to unfamiliarity with the new additions in this module.
The majority of these bugs were flagged by the friendly Werkzeug powered traceback interpreter. 
I became very familiar with this form of fault diagnosis and towards the end of the project I could understand exactly where I had gone wrong.
I am happy that I was able to eliminate and overcome any bugs encountered during the creation of this app.

Please see 3 of the major bugs and their commit messages below:

1.) Commit Message: > Bugfix: 0 value Likes displayed instead of DB stored value: "0d8ac5dbcc287158896b6ca08772ab8c71add0da"

2.) Commit Message: > Bugfix: Disable cross user editing of recipes: "667d3a6d36e51ff79bbfd538a6d1b4e37521f646"

3.) Commit Message: > Bugfix: Search query results correctly displaying on main page: "6d3d9f5528427c1bcb45716813cbd9df8bbb4fae" 
<br/><br/>
Google Inspect was used to eliminate styling and format bugs encountered. 
For any other fixes to bugs that were encountered that could not be visualised, 
I used console.log() for JS, print() for Python and displayed Jinja output to a div to visualise the results.
Changes were then made from there to fix code or eliminate the bug completely.
<br/><br/>

## References and Credits Section <a name="references_and_credits"></a>

**Code:** <a name="code"></a>

The JS code for the double password confirmation was found in the following location:
[ Diego Leme https://codepen.io/diegoleme/pen/surIK ](https://codepen.io/diegoleme/pen/surIK)
<br/><br/>

**The following is a list of external stylesheets, scripts, frameworks, modules and dependencies used in the creation of this project:**

Materialize Minified Stylesheet:
[ Materialize ](https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css)

Fontawesome Stylesheet:
[ Fontawesome cdn ](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css) 

Google fonts Stylesheets:
[ Google Font1 ](https://fonts.googleapis.com/css2?family=Handlee&display=swap) 
[ Google Font2 ](https://fonts.googleapis.com/css2?family=Roboto&display=swap)

JavaScript scripts:
[ Materialize ](https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js)
[ JQuery ](https://code.jquery.com/jquery-3.6.0.min.js)

Python Frameworks and Imported Modules:
[ Flask ](https://flask.palletsprojects.com/en/2.0.x/)
[ flask_pymongo ](https://flask-pymongo.readthedocs.io/en/latest/)
[ bson](https://bsonspec.org/) [ bson.objectid ](https://docs.mongodb.com/manual/reference/method/ObjectId/)
[ werkzeug.security ](https://werkzeug.palletsprojects.com/en/2.0.x/utils/)
<br/><br/>

The Contents of My "requirement.txt" file:

click==8.0.1

dnspython==2.1.0

Flask==2.0.1

Flask-PyMongo==2.3.0

itsdangerous==2.0.1

Jinja2==3.0.1

MarkupSafe==2.0.1

pymongo==3.11.4

Werkzeug==2.0.1
<br/><br/>

**Media** <a name="media"></a>

The photos used for the hero Image and the submitted recipes were taken from [https://unsplash.com/ ](https://unsplash.com/).

Please see list of credits below for the owner of each photo: 

* alex-loup-BvwhziJ2Lm4-unsplash – Photo by[ Alex Loup ](https://unsplash.com/@alexloup?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)on[ Unsplash ](https://unsplash.com/)
  
* alexander-mils-ocku3zjNM7k-unsplash – Photo by[ Alexander Mils ](https://unsplash.com/@alexandermils?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)on[ Unsplash ](https://unsplash.com/)
  
* denis-tuksar-n73TTunlskE-unsplash – Photo by[ Denis Tuksar ](https://unsplash.com/@dtuksar?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)on[ Unsplash ](https://unsplash.com/)

* skyler-h-mjYpDxTbojs-unsplash – Photo by[ Skyler H ](https://unsplash.com/@skyler029?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)on[ Unsplash ](https://unsplash.com/)
  
* jugoslocos-8DEIlmz7IfA-unsplash – Photo by[ Jugos locos ](https://unsplash.com/@jugoslocos?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)on[ Unsplash ](https://unsplash.com/)
  
I’d like to say a huge thank you to the photographers who provided the content above via Unsplash for the creation of this ficticious app.
<br/><br/>

**Content:**

The content for this site is based on numerous searches carried out in preparation for its creation. 
The initial recipes were in part, created based on recipes found on the BBC Good Food recipes. 
The remaining recipes are based on smoothies I have created in the past.

I was initially inspired by [ Jamie Oliver's ](https://www.jamieoliver.com/) website and it was the starting point for my colour scheme.
The finished product has changed alot from what was envisioned based on his site but it has, I feel remained true to the wireframes.
<br/><br/>

## User Testing <a name="testing"></a>

**Website Responsiveness through Browser and Device Compatibility** <a name="testing_procedure"></a>

The interactive front-end web application was tested throughout its development, implementation and deployment stages of the project.

For the continued functionality and responsiveness testing of this website I have utilised the following web browsers: Microsoft Edge, Mozilla Firefox and Google Chrome.

To carry out testing on mobile devices I have used Google Chrome as well as Safari on IPad and IPhone.

During all stages of development, HTML, CSS, JavaScript, Jinja, Python method & function verification, console.log() (JS), print() (Python) and Jinja result displayed to a html div, 
was utilised to simulate the required outcomes before implementing the end result on the page. The same methods were used to apply fault diagnosis upon the manifestation of bugs.
At all stages during testing, text was evaluated for spelling, grammer and punctuation. 

Please see the testing procedure table I have created for the SS&J website below:
<br/><br/>

![](static/images/readme_images/FUNCTIONTEST.png)

**Call to Action Functionality Testing Procedure** <a name="testing_user_stories"></a>

The table above was created to ensure no user testing steps were omitted when carrying out finished website checks. As part of my finished manual testing checks I have had a work colleague
navigate through the site using the table created to search for errors. Errors that were found have been re-solved. Some of them are mentioned in the bugs section.
<br/><br/>


**Testing User Story** <a name="testing_user_stories"></a>

The following is user feedback based upon a work colleague of mine visiting the site for the first time.

1. I was greeted by a landing page where it was apparent that I could look at recipes or search for recipes.

2. It was clear from the main page what this company was trying to do and both the descriptions in the picture and the bottom of the page explained it quite well.

3. I could see at the top of the page there was navigation links which brought me to various different locations on the site.

4. It was clear that I could not go further until an account was made so I chose the "Sign-up" option from the navigation bar at the top of the page.

5. I was brought to a page that made it very clear what my task was, enter a username followed by a password and a confirm password entry box.

6. After successfully creating my account I was brought to a profile page and was greeted with a message telling me I was logged in.

7. My profile was empty at first so I then had to submit a recipe. I navigated to the new recipe page and proceeded to fill out the form.
I found this page intuitive and easy to follow. Once the entry form was completed I inserted my recipe, was given a success message and then I navigated back to the profile page where I could view the details I had entered.

8. I decided to try out the "edit recipe" page and changed one of the items in my recipe steps. I clicked update recipe and then navigated back to the profile page to view the change. It had updated my recipe perfectly.

9. I then tried navigating to a displayed recipe and liking another users submission and this worked very well.

10. At the end I decided to delete my recipe to see how to proceedure went. Once I clicked delete I was asked a second time if I wanted to delete. I pressed cancel to see what would happed and I was just brought bac to the profile page.
I went ahead and clicked delet again and this time I went ahead and clicked delete the second time and sure enough my recipe was gone.

11. I then proceeded to log out which brought me back to the log in page.

My final thoughts are that this app does exactly what it needs to do. It displays well and navigates well. All functions work. I would be quite happy to be a returning user to this site. 

Site User: *“Michael J White“
<br/><br/>

**HTML CSS JavaScript and Python Validation** <a name="validation"></a>

Testing Code Validators for all sections of the website were carried out at: 

HTML =[ https://validator.w3.org/ ](https://validator.w3.org/) CSS =[ https://jigsaw.w3.org/css-validator/ ](https://jigsaw.w3.org/css-validator/) JavaScript = [ https://jshint.com/ ](https://jshint.com/) and Python = [ http://pep8online.com/ ](http://pep8online.com/)

Below are screenshots of the results of my Heroku app HTML, CSS stylesheet, JavaScript and python app.py files after being passed through validators. All Sections have Passed with no errors:

### Heroku App HTML

![](static/images/readme_images/HTMLVALIDATE.png)

### style.css

![](static/images/readme_images/CSSVALIDATE.png)

### script.js

![](static/images/readme_images/JSHINT.png)

### app.py

![](static/images/readme_images/PEP8VALIDATE.png)
<br/><br/>

## Future "Nice to Have" Additions to The Website <a name="additions"></a>

At project review meetings with my mentor some ideas for the future were discussed but were beyond my means in terms of time to implement.

I feel that these further implementations would bring more professionalism to the project as well as UX familiarity for the user.

1. Use actual Toastr messages using JS in the future. Maranatha provided me with a link to the following [Toastr](https://codeseven.github.io/toastr/demo.html). I have based my messages with similar styling but they lack the animation sequences.

2. Change the "Skil Level Required" input field to a slider. This would have functioned and looked great but unfortunately time did not allow it. It is something that I plan to incorporate in the future.

3. The addition of pagination for when the recipe list grows. At present there are only 10 recipes so the requirement is not there. It is however something that I would implement in the future editions.

4. A further filtering mechanism on the search box. It would be great to filter items by category or by allergen free with additional check boxes. Again, if time allowed this would have been a great addition and one for the future.

5. As well as having a "Like" button on the recipe display page I would like to implement an "Unlike" button where the likes are decremented and the user name is removed from the "user_likes" list. 
<br/><br/>

## CLI Commands Utilised Throughout The Project <a name="commands"></a>

“python3 app.py“: This command is used to start the app.py file from the GitPod IDE on the port 8080.

“CTRL + c“: This command is used to exit the app.py file from the GitPod port 8080.

“pip3 freeze --local > requirements.txt“: This command is used create a requirements.txt file containing all dependencies for the project.

“echo web: python app.py > Procfile“: This command is used to create your Proc file virtual file system.

“git add /specified file folder/specified file/file extension“: This command is used to add edited files to the staging area before carrying out a commit. 

“git commit -m \*commit message summarising the updates\*”: This command is used to commit the changes made to any files which had been previously added with “git add”. 

“git push”: This command is used to push git commit changes to the GitHub hosting pages and so that they can be viewed on a browser.
<br/><br/>  

## Deployment of this Project <a name="project_deployment"></a></a>

**How to Deploy My Milestone\_Project\_03 on Heroku** <a name="how_to_deploy"></a>

1. Navigate to the GitHub [Repository:[\]https://github.com/Ferdosull/Milestone_Project_03 ](https://github.com/Ferdosull/Milestone_Project_03)

2. Click on the green Gitpod button in the following screenshot.

![](static/images/readme_images/GITHUB001.png)

3. The repository will then open in Gitpods IDE

4. Inside the GitPod, Navigate to the requirements.txt file and make sure all required packages are installed in the IDE.

5. Create a .gitignore file and make sure its contents are the same as what is depicted below:

![](static/images/readme_images/GITIGNORE.png)

6. Create an env.py file and make sure to add it to the .gitignore file if you have not already done so. This prevents sensitive date from being pushed to GitHub.

7. The .env.py file should contain information like the screenshot below, I have removed my specific information from the screenshot for security reasons:

![](static/images/readme_images/ENV.png)

The SECRET_KEY is a value of your choosing and the MONGO_URI is obained from your specific MongoDB account in the following location:

Clusters > Connect > Connect your application and make the correct selections in the input modal. See below:

![](static/images/readme_images/MONGO001.png)

8. Save everything and carry out an initial commit to GitHub.

9. Create a Heroku account if you dont already have one and then create a new app inside heroku.

10. Click on the created app and navigate to the Deploy button.

11. Ensure that you select GitHub for the deployment method before moving down to the "Connect to GitHub section.

12. Navigate to the Repository you are choosing to setup for automatic deployment and click "Connect"

13. Once connected, be sure to enable "Automatic Deployment". Please see image below for visual representation of the steps:

![](static/images/readme_images/HEROKU1.png)

14. To add your environment variables to Heroku navigate to the "Settings" tab of your app and click the "Reveal Config Vars" button.

15. Inside the config vars enter the values stored in your env.py file, click "Add" followed by "Hide Config Vars" Please see image below for visual representation of the steps:

![](static/images/readme_images/HEROKU2.png)

16. Go back to the GitPod IDE and carry out a "git push".

17. Back inside Heroku, after a successful git push, click on the "Open app" button to see your newly deployed app.

![](static/images/readme_images/HEROKU3.png)

18. Save the link from your browser and bookmark.

## My Data Base Layout and Structure <a name="db_structure"></a>

I am using two DB objects within my project collection.

1. Object1 is being used for the recipes and it is depicted below:

![](static/images/readme_images/MONGODBRECIPE.png)

2. Object2 is being used for the Users and passwords also depicted below:

![](static/images/readme_images/MONGODBUSER.png)

## Previous Assessment Comments and How I Have Addressed Them <a name="previous_comments"></a>

As part of my first project review, Maranatha took the time to address the comments received from the last assessment and advised me what to do in order to make sure I dont fall down for the same reasons this time around.

1. “The testing write-up is not high-level and should include other aspects like objective and performance testing.“ Performance testing is not something I have covered and I dont have familiarity with it. 
It is however, something I will be looking into and possibly asking advice for from Student Support going forward to the next module. I have given more detail to the testing section this time so I hope that this is seen as an improvement.

2. “The testing of the stated user stories is also not covered.“ The testing of the stated user stories is now covered in this Readme. Please see link [User Stories](#testing_user_stories)

3. “Understanding of git version control is not established and lacks in conducting commits promptly with a fine descriptive message.“ Maranatha has taken time to make me fully aware of how a commit should be structured and how to keep them in the imperitive mood. I feel I have certainly improved this aspect of the project.

4. “Color contrast needs improvements that restrict the project distinction.“ I have made very concious decisions this time that influenced the colour scheme. This comment was always at the front of my mind while implementing this project. It is my hope that the end result is better this time than the last submission.

## Acknowledgements <a name="acknowledgements"></a>

Again, I'd like to say a special thank you to my mentor Maranatha Ilesanmi. Maranatha has provided excellent constructive feedback at the project review meetings.
I have made many great changes to my project based on Maranatha's input and recommendations. Once again I have learned alot from him and I look forward to his feedback on the next project!