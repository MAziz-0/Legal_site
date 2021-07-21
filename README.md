<h1 align="center">Nottreal Solicitors</h1>

[View the live project here.](https://nottreal-solicitors.herokuapp.com/)

I have created a web application fit to showcase a faux solicitors firm, Nottreal Solicitors which is inspired by the firms I have worked at in the past. Using my experience in the Legal sector, I created a clean and approachable website that is a centrepiece for clients/potential clients to interact with. The website consists of easily readable information pertaining to the services it provides and articles on Legal and Financial news, with the Message board being the key feature of the website bringing the consultation procedure directly to clients.

<h2 align="center"><img src="https://user-images.githubusercontent.com/41737293/126453913-4c77d2ff-69a3-48c5-8fe0-1812047b7dd3.JPG"></h2>


### Project Specifications

| CRITERIA | MEETS SPECIFICATIONS
|---|:---
| Home page | The user is greeted with a home page which is the website's foundation which introduces the firm through its features section, testimonial section and blog system.
| Services | The Website has separate pages with information on services the firm provides.
| User Authentication | The user can register an account that allows them to log in and log out.
| Blog Articles| Article cards are available on the home page to provide Legal and Financial news.
| Message Board | Once registered and logged in, users can ask questions using the New query page, or they can search pre-existing questions. Questions they have asked have CRUD features implemented, allowing them to manipulate their data.


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to be pulled in by the presentation of the website.
        2. As a First Time Visitor, I want to use the website as intended for it to function.
        3. As a First Time Visitor, I want to register and manipulate my data.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to see that my questions are visible on the message board and get the information I need.
        2. As a Returning Visitor, I want to edit/update or even delete the queries I have posted.
        

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if I can log into my account without issue.
        2. As a Frequent User, I want to check to see if there are any new featurettes in the Article cards
        3. As a Frequent User, I want to navigate the website and find things where they are supposed to be.

-   ### Design
    -   #### Colour Scheme
        The two main colours represent the firm's company branding.
    -   #### Typography
        -   The Segoe UI font is the main font used throughout the whole website. Segoe is standardised and used to achieve readability and professionalism; it is both attractive and appropriate.
    -   #### Imagery
        -   Imagery is vital. The background hero images on the home pag and the About sections are designed to create familiarity with the staff and putting a face behind the brand.

*   ### Wireframes

    -  Wireframe - [View](https://user-images.githubusercontent.com/41737293/126455811-def56c72-13dd-4e5a-8e68-b0bd971de246.JPG)

   
## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [MongoDB](https://en.wikipedia.org/wiki/MongoDB)


### Frameworks, Libraries & Programs Used

1. [Bootstrap](https://getbootstrap.com/)
    -  Bootstrap was used to create for majority of the website.
1. [Flask](https://flask.palletsprojects.com/en/2.0.x//)
    -  Flask was used to create the website's pages by way of routing (Pymongo, Dnspython)
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Heroku:](https://en.wikipedia.org/wiki/Heroku)
    - Heroku is used to store the project's code after being pushed from Git and allows us to deploy the project live.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://user-images.githubusercontent.com/41737293/126455811-def56c72-13dd-4e5a-8e68-b0bd971de246.JPG) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure no syntax errors.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://user-images.githubusercontent.com/41737293/126494547-baee4fec-3f8d-467c-b029-246fd333bbad.JPG)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://user-images.githubusercontent.com/41737293/126495898-e6aef95a-5954-4316-a6d9-25b8e0c9572a.JPG)
- Please note that CSS tested was Custom CSS I created; the free template used for Bootstrap styling did not pass through the validator,which had multiple parsing errors out of my control.

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to be pulled in by the presentation of the website.

        1. Upon entering the site, users are automatically greeted with a clean and inviting home page, introducing the firm and services. There is a Hero Image used next to the firm's name, which displays some of the members of staff.
        2. There is a Learn More button that takes me to a feature section that allows me to read about some of the speciality services available.
        3. There is a testimonial section that shows a positive short review from a previous client.
        
        - [View](https://user-images.githubusercontent.com/41737293/126496961-fe3a5647-8bd1-4fb4-83c8-b3d78e4a5a9f.JPG)

    2. As a First Time Visitor, I want to use the website as intended for it to function.

        1. Each component of the website is straightforward and structured, separated by blocks, the main home page and each relevant service page, a login/register page which then allows the user to access the logged-in user features - Message board feature
        2. I can register an account without any issues, which allows me to see a profile page and the message board system, a flash message alerts me that I have logged in properly.

          - [View](https://user-images.githubusercontent.com/41737293/126497699-6428264d-fc79-4f1f-9499-c8afb20a00b1.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/126497758-d7423de5-2347-4590-a007-ffefd2efca06.JPG)

    3. Logging in, an incorrect username shows a flash message.

          - [View](https://user-images.githubusercontent.com/41737293/126498666-bea654dc-8ffa-436e-b62d-a2ed09508679.JPG)

    3. As a First Time Visitor, I want to register and manipulate my data.

        1. I can register and log in to my account, which allows me to see the New query page and Message Board.
        
          - [View](https://user-images.githubusercontent.com/41737293/126499391-9535b57f-4326-4b0c-8760-3209efea2c9f.JPG)

          - [View](https://user-images.githubusercontent.com/41737293/126499543-991e83ef-ecdc-42d1-85e8-9dcbb6c6147f.JPG)

        2. I can Edit/Update and Delete queries that I have created.

          - [View](https://user-images.githubusercontent.com/41737293/126499603-29b1c4ef-eba7-48f8-bbe2-08e12c8cbbe9.JPG)
   

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to see that my questions are visible on the message board and get the information I need.

          - [View](https://user-images.githubusercontent.com/41737293/126499972-e0545a5e-b3b2-4322-b1bc-c2e6928bb6ba.JPG)

    2. As a Returning Visitor, I want to edit/update or even delete the queries I have posted.

          - [View](https://user-images.githubusercontent.com/41737293/126499603-29b1c4ef-eba7-48f8-bbe2-08e12c8cbbe9.JPG)




-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if I can log into my account without issue.

        1. The user can log in without issue as long as the username and password are correct

    2. As a Frequent User, I want to check to see if there are any new featurettes in the Article cards

        1. Blogs can be updated by guest writers or members of staff; currently, there are three articles regarding highly talked about topics.

    3. As a Frequent User, I want to navigate the website and find things where they are supposed to be.

        1. Navigation bar is simple and straightforward. 
        2. Finding what you need is not difficult as everything is placed visibly and makes sense.
    

### Further Testing

-   The live project has been tested  on a variety of devices such as Desktop and Samsung Note 10 +
-   A large amount of testing was done to ensure that the website is responsive.
-   Friends and family members were requested to review the site and documentation to point out any bugs or user experience issues, and all were content with the browsing experience.

### Known Bugs

-   When navigating the login pages, once logged in, some of the images would stop working, unable to find a fix; as a workaround, I have removed some pictures as they are irrelevant to the feature.

### Heroku

The project was deployed to Heroku using the following steps.

1. First, we need to tell Heroku which applications and dependencies are required to run our app by creating a text file.
2. Procfile is what Heroku looks for to know which file runs the app, and how to run it, so we'll use the echo command to create a Procfile.
3. Log into Heroku and "Create New App" and name the app appropriately. Select the region closest to you and create.
4. We can use Heroku CLI or, to simplify the process, set up Automatic Deployment from our GitHub repository under the deploy tab in Heroku. Search Repository name and then add.

[More info](https://devcenter.heroku.com/articles/heroku-cli)

5. Before we start Automatic deployment, create a Config variable file under "Rev Config Vars" to tell Heroku what variables are needed. Make sure "Procfiles" and all required files have been pushed to the Repository before connecting.
6. Click on connect to Github repository, and now we can click on Automatic deployment, which will push the master to Heroku.
7. Click "View" to launch your new deployed app.

### Forking the GitHub Repository

By forking the GitHub Repository, we copy the original Repository on our GitHub account to view or make changes without affecting the original Repository by using the following steps.

1. Log in to GitHub and locate the relevant Repository.
2. At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original Repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the relevant Repository.
2. Under the repository name, click "Clone or download".
3. To clone the Repository using HTTPS, copy the link under "Clone with HTTPS".
4. Open Git Bash
5. Change the current working directory to where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

## Credits

### Code

-   [Modern Business template](https://startbootstrap.com/template/modern-business): Modern Business template was used to create the base layout for the website.

### Content

-   All Legal content was sourced from various Legal websites, none of the information will be used for commercial purposes as this is a educational project.


### Media

-   The background images came from [Pexels](https://www.pexels.com/)
-   The Bootstrap template came from [StartBootstrap](https://startbootstrap.com/template/modern-business)
-   The Favicon icon came from [Wikimedia](https://commons.wikimedia.org/wiki/File:Eo_circle_purple_letter-n.svg)

### Acknowledgements

-   Python/Flask logic learn from Code Institute Instructional videos 

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.