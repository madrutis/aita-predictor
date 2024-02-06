# aita-predictor
## Goal
The goal of this project is to be able to predict the outcome of an [r/aita](https://www.reddit.com/r/AmItheAsshole/) post as one of four labels with accuracy:
- NTA `Not the Asshole`
- YTA `You're the Asshole`
- NAH `No Assholes Here`
- ESH `Everyone Sucks Here`
## Components
### Web Scraper
- The Web Scraper will gather recent posts given a number and store them in a database
### Training
- Once the desired posts are compiled a **________** machine learning algorithm will be trained
### Prediction / Test
- Predict posts using the bag of words, and a single layer perceptron
## Possible extensions of the project
### UI
- Not sure if I want to make a UI to submit posts yet, but it could be useful and a good project to do with django
### Reddit Post Bot
- I could auto-comment on a new post what the bot thinks, and possibly use GPT-4 to generate some reasoning.
