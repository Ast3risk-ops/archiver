No invite link yet because I haven't set up hosting.

Supports being added to servers as well as being used as a user app.

## Self-Hosting

\<better instructions soon\>

1. make a discord app on [the dashboard](https://discord.com/developers/applications)
2. rename .env.example to .env
3. set the values inside (`WEBHOOK_URL` is where errors are sent, make it private!)
4. edit `main.py` and remove all custom emoji `<:emojiname:id>`, thosse are specific to my (soon-to-be) public instance
5. install dependencies with [`pipenv`](https://pipenv.pypa.io):
  ```sh
  pipenv install
  ```
5. start the bot
  ```sh
  pipenv run bot
  ```
6. invite it n stuff (set the scopes of `bot` and `applications.commands` when making your OAuth2 URL)
