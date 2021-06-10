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
    6. [Page Links](#page_links)
    7. [Placeholder 7](#t5_buttons)
    8. [placeholder 8](#g_map)
    9. [placeholder 9](#campsite)
    10. [placeholder 10](#footer)
4. [Utilising the 5 Planes of UX Design](#ux_design)
    1. [The Strategy Plane](#strategy_plane)
    2. [The Scope Plane](#scope_plane)
    3. [The Structure Plane](#structure_plane)
    4. [The Skeleton Plane](#skeleton_plane)
    5. [The Surface Plane](#surface_plane)
5. [Typography](#typography)
6. [User Stories](#user_stories)
    1. [External User's Goal](#external_user_goal)
    2. [Site Owner's Goal](#site_owner_goal)
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
11. [Creation of Template and Deployment of Project](#project_deployment)
    1. [Creating a New Project](#new_project)
    2. [Commands Utilised Throughout The Project After Changes](#commands)
    3. [How to Deploy My Milestone\_Project\_03 on Heroku](#how_to_deploy)
    4. [How to Download, View and Edit and Run this project locally](#how_to_download)
12. [Acknowledgements](#acknowledgements)<br/><br/>

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
Maranatha has re-capped and explained the reasons for comments I received from my last Milestone Project and has advised how to improve so that a distinction may be achieved this time around.
I have also added a section in this README file, where I explain what has been implemented in this project to counter act the reasons for falling down in the last project.

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

On this occassion I have decided not to have the nav-bar fixed to the top. Once the page is scrolled it stays at its absolute location. I felt that the minimal appearance I was going for would appear 
crowded in this circumstance if the nav-bar followed. The nav-bar can be separated up into desktop and mobile views as seen below. The "HOME" and VWCC logo both reload the page while the "About" selector 
scrolls the visitor to the info section, which is roughly halfway down the page.
<br/><br/>

### Hero Image <a name="hero_image"></a>

![](static/images/readme_images/README005.png)

The Hero Image that loads upon first display of the page is of an iconic VW campervan, which is keeping in line with the clubs theme. This image is then updated through five other images using button clicks 
to initialte JavaScript targeting of Id's in the html and changing the image source. This is completed with delay transition timers in conjunction with the addion and removal of CSS classes to provide opacity effects.
<br/><br/>

### Header & Description Text <a name="header_description"></a>

![](static/images/readme_images/README006.png)

The Header text, when first landed on the page, is the name of the club, "Volkswagon Choice Camping" and the description text below it is a small summary of what the club provides the site user.
Both the Header and the description text get updated when any of the Top five buttons are pressed. For example, if "Lakeside C&C Park" is clicked/selected the header text and description text will change to 
be in line with the button chosen. Like the hero image, this is also completed with delay transition timers in conjunction with the addion and removal of CSS classes to provide opacity effects.
<br/><br/>


### Page Links <a name="page_links"></a>

![](static/images/readme_images/README007.png)

Underneath the description text are two selectors. "More Info!" and "Visit This Site!". The "More Info!" button is only visible on tablet and mobile devices. Its function is to scroll the visitor to the 
campsite information section associated with the location that is currently being displayed. The "Visit This Site!" button has a href that is updated by JavaScript based also on the location being displayed.
If pressed, it will navigate the user to an external page associated with the campsite selected.
<br/><br/>
