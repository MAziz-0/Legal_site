<h1 align="center">Nottreal Solicitors</h1>

[View the live project here.](https://nottreal-solicitors.herokuapp.com/)

I have created a web application fit to showcase a faux solictors firm Nottreal Solicitors which is inspired by the firms I have worked at in the past. Using my experience in the Legal sector I created a clean and approachable website that is a centerpiece for clients/potential clients to interact with. The Website consists of easily readable information pertaining the services it provides and articles on Legal and Financial news with the Message board being the key feature of the website bringing the consultation procedure directly to clients.

<h2 align="center"><img src="https://user-images.githubusercontent.com/41737293/126453913-4c77d2ff-69a3-48c5-8fe0-1812047b7dd3.JPG"></h2>


### Project Specifications

| CRITERIA | MEETS SPECIFICATIONS
|---|:---
| Home page | The user is greeted with a Home page which is the foundation of the website introducing the firm through its features section, a testomonial sections and blog system.
| Services | The website has seperate pages with information on services the firm provides.
| User Authentication | User can register an account which allows them the ability to log in and log out.
| Blog Articles| Article cards are available on the home page to provide Legal and Financial news.
| Message Board | Once registered and logged in, users can ask questions using the New query page or they can search pre-existing questions. Questions they have asked have CRUD features implemented allowing them to manipulate their own data.


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to be pulled in by the presentation of the website.
        2. As a First Time Visitor, I want to use the website as intended for it to function.
        3. As a First Time Visitor, I want to be able to register and manipulate my data.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to see that my question are visible on the message board and I can get the information I need.
        2. As a Returning Visitor, I want to be able to Edit/Update or even delete the queries I have posted.
        

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if I can log into my account without issue.
        2. As a Frequent User, I want to check to see if there are any new featurettes in the Article cards
        3. As a Frequent User, I want always to be able to navigate the website and find things where they are supposed to be.

-   ### Design
    -   #### Colour Scheme
        The two main colours represent the firms company branding.
    -   #### Typography
        -   The Segoe UI font is the main font used throughout the whole website. Segoe is standardised and used to achieve a professional and easy to read website, it is both attractive and appropriate.
    -   #### Imagery
        -   Imagery is vital. The background hero images on the splash screen and About sections are designed to create familiarity with staff and putting a face behind the brand. .

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
    -  Bootstrap was used to create majority of the websites layout.
1. [Flask](https://flask.palletsprojects.com/en/2.0.x//)
    -  Flask was used to create majority of the websites pages by way of routing (Pymongo, dnspython)
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Heroku:](https://en.wikipedia.org/wiki/Heroku)
    - Heroku is used to store the project's code after being pushed from Git and allows us to deploy the project live.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://user-images.githubusercontent.com/41737293/126455811-def56c72-13dd-4e5a-8e68-b0bd971de246.JPG) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://user-images.githubusercontent.com/41737293/126494547-baee4fec-3f8d-467c-b029-246fd333bbad.JPG)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://user-images.githubusercontent.com/41737293/115413571-31d07c00-a1ed-11eb-8a3c-d53d654d40d8.PNG)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to be pulled in by the theme of the website/game.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable Splash screen, which introduces the plot and premise for the game. There is a Hero Image used in the background, which displays the enemy opponent(Itachi).
        2. There is a brief tutorial text which tells the user how to play; not much detail is needed as the game is intuitive enough to pick up without instructions.
        3. The splash screen has an appropriate timeout feature which gave me enough time to read the content and tutorial.
        
          - Screenshot  [View](https://user-images.githubusercontent.com/41737293/115718602-2c9d3980-a373-11eb-9bb3-32d5bd027e2d.JPG)

    2. As a First Time Visitor, I want to play the game as intended for it to function.

        1. Each component of the website is straightforward and structured, separated by a splash screen, the main game and finally, a victory or loss alert.
        2. The timeout features are functional, the cards flips are fluid, and the timer works correctly.

          - Screenshot  [View](https://user-images.githubusercontent.com/41737293/115718905-7d149700-a373-11eb-8f1b-294b13ca5ae6.JPG)

    3. There is an option to "Play again" when winning and "Try again" when losing; GIFs are also used to emphasise the win/loss.
          - Screenshot  [View](https://user-images.githubusercontent.com/41737293/115719038-9f0e1980-a373-11eb-95d2-2fdb8d038d1c.JPG)

    3. As a First Time Visitor, I want to learn more about the developer.

        1. Once the new visitor has won the game or lost the game; there is a link to the developer's portfolio.
        2. Developer links are not as crucial and should not take away from experience; therefore, they are presented once the game session has ended.

          - Screenshot  [View](https://user-images.githubusercontent.com/41737293/115719349-e8f6ff80-a373-11eb-8918-b25f59a16c7d.JPG)
   

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to see if the game is fun being replayed.

        1. The cards are randomised, so each experience is different.
        2. The use of a 30-second timer makes the game fast and exhilarating, which allows for replayability.
        3. A suggestion is made at the end of the game to give more reasons for the player to challenge themself.

          - Screenshot  [View](https://user-images.githubusercontent.com/41737293/115719716-468b4c00-a374-11eb-8bb5-55e415c44ef4.JPG)

    2. As a Returning Visitor, I want to find the best way to find out more about the developer.

        1. A link to the developer's portfolio is readily available whether the game is won or lost.
        2. The portfolio gives a base introduction and provides information on the developer's skillset and links to all socials.

          - Screenshot  [View](https://user-images.githubusercontent.com/41737293/115719947-7cc8cb80-a374-11eb-9842-7ca831a43f6f.JPG)




-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added challenges or updates.

        1. The user can continue to play in a conventional way or without memorising.

    2. As a Frequent User, I want to check to see if there are any new features.

        1. The user would already be comfortable with the game but has access to the developer through the portfolio to see if they make any more updates or features.

    3. As a Frequent User, I want always to have fun playing the game; replayability is crucial.

        1. The memory game is fluid and works well, with a small timer which makes the game difficult if you aren't familiar with the images used as they are not simplified symbols.
        2. There is an option to play the matching game without memorising the cards, making the game more intense and harder to win.
    

### Further Testing

-   The live project has been tested  on a variety of devices such as Desktop and Samsung Note 10 +
-   A large amount of testing was done to ensure that the game is functional
-   Friends and family members were requested to review the site and documentation to point out any bugs or user experience issues, and all were content with the gaming experience.

### Known Bugs

-   On some mobile devices, the title image does not fit correctly, and the cards are cut off if the screen size is too small.
    -   If the screen is too small, the "click to start" is pushed into the title image
-   On Microsoft Edge and Internet Explorer Browsers and some phones, the .gif/.webp format does not display correctly.
    - Unable to get HTML5 Audio or iframe working correctly on mobile devices, only works after the game is restarted using the Try again/Play again alert.

### GitHub Pages

The project was deployed to GitHub Pages using the following steps.

1. Log in to GitHub and locate the relevant Repository.
2. At the top of the Repository (not top of page), find the "Settings" button on the menu.
3. Scroll down the Settings menu until you find the Pages tab. Click on Pages
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Click on the Github Pages tab, which should provide a link to the live project.

### Forking the GitHub Repository

By forking the GitHub Repository, we make a copy of the original Repository on our GitHub account to view or make changes without affecting the original Repository by using the following steps.

1. Log in to GitHub and locate the relevant Repository.
2. At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original Repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the relevant Repository.
2. Under the repository name, click "Clone or download".
3. To clone the Repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
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

-   [SweetAlert2](https://sweetalert2.github.io/): SweetAlert2 used to create beautiful and responsive alerts.

### Content

-   All text content was written by the developer.

-   All materials on this Site(Naruto), including, but not limited to characters, images, illustrations, audio clips, video clips, and compilations, are protected by copyrights, trademarks, and other intellectual property rights which are owned and controlled by VIZ Media, LLC. and its affiliates (collectively, "VIZ Media, SHONEN JUMP, Shojo Beat")


### Media

-   The Full-screen background image came from this [Wallpaperaccess](https://wallpaperaccess.com/uchiha-fan)
-   The Victory .webp came from this [Tenor](https://tenor.com/view/happy-naruto-smile-gif-12599252)
-   The Loss .webp came from this [Cute Wallpaper](https://cutewallpaper.org/21/wallpaper-mangekyou-sharingan-gif/Top-30-Sharingan-GIFs-Find-the-best-GIF-on-Gfycat.gif)
-   The Splash screen background image came from this [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1093657)
-   The Card images came from [Pinterest](https://www.pinterest.co.uk/)
-   The Favicon icon came from [Icon Library](https://icon-library.com/icon/naruto-icon-13.html)

### Acknowledgements

-   Javascript logic inspired by OurCodeSolution (https://ourcodesolution.com/)

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.
