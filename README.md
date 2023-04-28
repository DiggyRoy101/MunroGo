# Project Documentation

## MunroGo

- Warren Hill
- Paula Mejia
- Brian Rabern
- Elijah Ramos
- Diganta Roy

Your challenge, should you choose to accept it, is to conquer Munros in Scotland, a list of Scottish mountains which are named after Sir Hugh T Munro, who surveyed and catalogued them in 1891. MunroGo is a comprehesive guide to all of Scotland's 282 Munros. Gotta bag 'em all!

## Design

    - API design
    - GHI
    - Integrations
        - OpenWeather API
        - Google Maps API
        - Wikipedia API

## Intended market

Munro bagging is a popular pastime in Scotland where walking enthusiasts challenge themselves to climb as many of the peaks as they can - over 6,000 people, called 'compleatists' (or Munroists) have climbed them all so far. We are targeting adventure seekers that wish to plan, review and track Munro climbs.

## Funtionality

- Website requires users to sign up to have access to its functionality.

Users will have access to their dashboard, which displays:
    - Their privately logged climbs
    - Their statistics
    - Their publicly written reviews for Munros
    - A list of climbed Munros by the user
    - A map, integrated through the Google Maps API, which has different colored markers depending on whether users have climbed a Munro or not. Unclimbed Munros will be displayed with a red marker and climbed Munros will be displayed with a green marker. Each marker redirects the detail page for each specific Munro when clicked.

    - From the dashboard, users can also see a page which includes of all their climbs, and another page which displays all their reviews.

Each Munro has its own detail page which includes:
    - A picture of the Munro
    - Its height
    - A summary
    - A map with the marker of the Munro's location, integrated through the Google Maps API
    - The region the Munro is located
    - Its latitude and longitude coordinates
    - Buttons to add a climb or a review for the specific Munro - both of which display a modal when clicked
    - Public reviews by users
    - The current weather conditions at the Munro - implemented through the OpenWeather API

- Users will be able to add a climb from their dashboard, selecting a Munro from a dropdown menu

- A list of all the Munros, which includes the region, height in feet and meters, and which allows the user to select whether a Munro has been climbed and displays a modal to add a climb. Users can search this list using the search bar - filtering by name, region, and height. Users may also navigate to individual Munro detail pages by clicking the Munro's name on the list.

## Project Initialization

To fully enjoy this application on your local machine, please be sure to follow these steps:

1. Clone the repository down to your local machine
2. CD into the new project directory
3. Run docker volume create mongo-data
4. Run docker compose build
5. Run docker compose up
6. Run docker exec -it munro-go-fastapi-1 /bin/bash
7. Run python seed_db.py

Start bagging those Munros!
