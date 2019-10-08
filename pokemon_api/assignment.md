# Front-End Developmet Task: Pokemon API
This is a development assignment for ECS. Before attempting this assignment, please take note of our [general instructions](../readme.md) and any additional instructions which may have been provided by the ECS recruiter. Reading the instructions carefully is part of the assignment.

## User Story
Pokemon Centres in the Jhoto region are considering migrating all of their internal systems to a web-based interface. You have been asked to implement a small demo that shows how a web-application can connect with an existing API. 

You must implement this user story:
  * As a user, I want to click a button which causes the details of a randomly chosen Pokemon to be displayed in a browser.
  * Each time I click on the button the screen will change and display the details of the new pokemon. 

It is widely believed that the Jhoto region is home to 151 species of Pokemon, all of which can be retrieved from the The [Pokemon API](https://pokeapi.co/).

For example:
 * [Bulbasaur](https://pokeapi.co/api/v2/pokemon/1)
 * [Mew](https://pokeapi.co/api/v2/pokemon/151)
 
As you can see, all 151 Pokemon in the Jhoto region are identified by an integer ID with a minimum value of 1 and a maximum of 151. It is rumored that higher-numbered Pokemon exist in other regions but these are outside the scope of this assignment.

## Task 1

* Display the 
  * name
  * the image (front-default sprite)
  * and stats of a pokemon
    * speed
    * defense & special defense
    * attack & special attack
    * HP
    * Weight
    
* Create a simple interface based on the wireframe provided or your own concept.

## Example

1. The user can see a button and an empty section below it.
2. The user clicks on the button.
3. The empty section below the button is replaced with details about a single randomly chosen Pokemon.

## Task 2

  * Create a sidebar on the left side of the screen with a list of 10 random pokemons
    * Each name is clickable
  * Create a main section, on the right of the sidebar
    * the main section should display the details of the selected pokemon.
    * Each time you select a new pokemon from the list, the main section should be refreshed and display the details of the new pokemon
  * When I refresh the page
    * the last selected pokemon should be displayed again
    * but the sidebar should list a complete new list of 10 random pokemon

# Tools
You may use any tools or IDE (including online IDEs). 

Regarding the framework, you can choose between:

  * Vanilla JS
  * Typescript
  * React
  * React + Typescript

If you chose any other framework we may not be able to assess your submission.

# Follow up questions
1. Force click the generate button and see how the app behaves.
2. Refresh the page and see if the details of the pokemon are saved and redisplayed or not.
3. What can be improved if given more time.
4. Any ideas to take advantage of what have been done so far and build something bigger/better/awesomer.
