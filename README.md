# Welcome to You Sunk My Battleship

<p>You Sunk My Battleshp is a tribute to the popular traditional game of <a href="https://en.wikipedia.org/wiki/Battleship_(game)#:~:text=Battleship%20is%20known%20worldwide%20as,device%20apps%20and%20a%20film">Battleships</a>, the ultimate in simple strategy gaming.</p>
<p>Battleships can be played with just a paper and pen but it has grown into much more since it's inception during World War I. Now expanded to board games, electronic games and even a film, it is an enduring classic. This version offers a basic version in which the player must try and "sink" the ships on the board by guessing their position with a limited number of turns.</p>
<p>This game is a demonstration of my Python skills as required by Portfolio 3 Assessment as part of the Code Institute Diploma in Full Stack Software Development.</p>
<br>
<strong>The deployed game can be found <a href="??">here</a></p></strong>
<br>
<p><img width="640px" height=auto src="??" alt="??"></p>
<br>

## How to play
<p>Battleships are placed on a board and hidden from the player. They must guess where on the board they think the battelship is placed. First, typing a number corresponding to the x axis then hitting enter on their keyboard. This is followed by a letter corresponding to the y axis and the enter key. If the guess is correct, they have hit and sunk a battleship!</p>

<p>Players are limited to 8 torpedoes (or turns) in which to try and destroy all the battleships and win teh game.</p>

<p>If they are successful, they will be rewarded with a surprise ASCII display. If they run out of torpedoes, they will be prompted to try again in a new game.</p>
<br>

## Wireframing & Planning
<p>Before development began, <a href="https://lucid.app/documents#/dashboard">Lucid</a>, an online chart builder, was used to map out the game and how best to approach it. It helped to work through the steps needed to make the game make sense to the player and what tasks the code should execute.</p>
<br>
<p><img width="1280px" height=auto src="img/python_battleships_flow.png" alt="battleships game play plan using lucid chart"></p>
<br>

## Features
### Existing
<ul>
<li>Generates board</li>
<li>Places battleships in random positions on board</li>
<li>Keeps score</li>
<li>Limit player turns</li>
</ul>
<br>

### Future
<ul>
<li>Boat number/board size choice</li>
<li>Two player mode</li>
<li>Custom player naming</li>
</ul>
<br>

## Data Model
<p>For this game, two classes were used; one for the board and one for the ships. Using two classes for main elements of the game should allow for additional features to be added later without disrupting the way the game currently runs.</p>

### BattleshipBoard
<p>This class is used to generate the board during the gameplay. As the player adds their guesses to the board it's used up to 8 times in one game.</p>
<br>

### Battleships
<p>This class handles the position of the ships on the board and the players entries including validation and checking if the turn was a "hit". Similar to the BattleshipBoard class, Battleship is used at least 8 times, more if the user repeatedly enters an incorrect value when guessing.</p>
<br>

## Testing
<p>This project was validated using PEP8 for Python 3. PEP8 is the industry standard that provides guidelines for styling Python code. It helps to keep programmes written in Python legible and maintainable.</p>
<p>It should be noted that as the ships on the boards are randomly generated, it is difficult to test real game play of a winning game, especially with real users.</p>
<br>

### Gitpod
<p>Using Gitpod as my workspace provided additional support when building this game. It flags errors and potential areas to improve as the user writes the code. This was particularly useful for ensuring indentation and line length were up to PEP8 standard as the project developed.</p>
<br>

### Online PEP8 checkers
<p>In addition to Gitpod, several online tools such as <a href="https://extendsclass.com/python-tester.html">Extends Class</a> were used to back up Gitpod validation during development. However, some of them were dated and checking against older Python versions. This initially caused some confusion as they flagged code that was currently correct, such as the use of f-strings. Once the error was realised, the project was rechecked using an appropriate version and found no significant errors.</p>
<br>

### UAT
<p>The game was tested in person with two users using a different device for each user. Without access to Apple devices, both used devices running Windows 10 using the Gitpod terminal. Users were encouraged to enter incorrect data. There were no issues found with the game play or how it was executed.</p>

### Code Institute Python Linter
<p>The Code Institute Python Linter was used as the final phase of testing before deployment. It showed some line lengths that could be improved and new variable or split lines were used to shorten them. !!!The project was tested again after deployment...!!!</p>
<br>

## Deployment
<p>This project was deployed using <a href="https://dashboard.heroku.com/apps">Heroku</a> Cloud Platform. It uses the <a href="https://github.com/Code-Institute-Org/python-essentials-template">Code Institute Python template repo</a> to assist with successful deployment, as per project recommendations. To replicate the deployment, please follow the below steps.</p>

### Steps for Deployment
<ul>
    <li>??</li>
</ul>
<br>

## Credits
### Background Support & Referencing:
<ul>
    <li><a href="https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/">Portfolio Project 3 Scope</a> through Code Institute</li>
    <li><a href="https://www.youtube.com/watch?v=alJH_c9t4zw">Python Battleship with Object Oriented Programming</a> by Knowledge Mavens through Youtube</li>
    <li><a href="https://copyassignment.com/battleship-game-code-in-python/">Battleship Game Code in Python</a> by Pranjav Dev through Copy Assignment</li>
    <li><a href="https://bigmonty12.github.io/battleship">Python for Beginners: Battleship2</a> by Austin Montgomery through BigMonty1.github.io</li>
    <li><a href="http://www.figlet.org/examples.html">FIGlet</a> by Plig.net through Figlet.org</li>
</ul>
<br>

### Direct Sourcing:
<ul>
    <li><a href="https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/">Python ASCII art using Pyfiglet Module</a> by Ankthon through Geek for Geeks - This is a straight forward method of inserting ASCII art into the project and there didn't appear to be justification for changing or complicating it.</li>
    <li><a href="https://www.youtube.com/watch?v=alJH_c9t4zw">Python Battleship with Object Oriented Programming</a> by Knowledge Mavens through Youtube - This tutorial helped resolve two issues I couldn't get past on my own. The first was formatting the board with an f-string. Although all the characters were working, the layout of the board was broken. I'm unsure if formatting placeholders are actually the optimal approach but they were the best one at the time of submission. Secondly, after putting together the elements of the game, it would not run. After unusuccessfully rechecking the definitions and functions by printing to the terminal, reviewing this solution demonstrated that the main function to run the script was missing.</li>
    <li><a href="https://www.askpython.com/python/examples/exit-a-python-program">Exit a Python Programm in 3 Easy Ways</a> by AskPython.com - a break was used to stop game play after offering a rematch but this didn't acknowledge the player saying no to the new game. In looking for an alternative method to employ, this resource was discovered. The "quit" function was used as it is built in and doesn't require importing anything else to the game (compared to sys.exit). It is my understanding that this should only be used in scenarios such as student projects, where the code is not part of a larger, commercial project.</li>
<ul>