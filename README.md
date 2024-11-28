No invite link yet because I haven't set up hosting.

## Self-Hosting

\<better instructions soon\>

1. make a discord app on [the dashboard](https://discord.com/developers/applications)
2. rename .env.example to .env
3. set the values inside (`WEBHOOK_URL` is where errors are sent, make it private!)
4. install dependencies with [`pipenv`](https://pipenv.pypa.io):
  ```sh
  pipenv install
  ```
5. Start the bot
  ```sh
  pipenv run bot
  ```
6. Invite it n stuff (set the scopes of `bot` and `applications.commands` when making your OAuth2 URL)
