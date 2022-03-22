# News-diff

#### Video Demo: [https://youtu.be/mIZNFJ3F5qw](https://youtu.be/mIZNFJ3F5qw)

This Python script checks the news at [corriere.it](https://corriere.it) and publish any change in the title or in the subtitle at [@corriere_diff](https://t.me/corriere_diff) on Telegram. Inspired by [@nyt_diff](https://twitter.com/nyt_diff) on Twitter

## Installation

If you want to run the script you can just build the Docker image. Make sure you have everything you find on config.py in your environment variables. Also note that the script is set up to use a PostgreSQL database that runs on Heroku, so you may want to edit the [src/models.py](src/models.py) file to use a different database.

## License

[MIT](LICENSE)
