# Philly Bike Action Administration, Bridges, and Planning
Website for [https://apps.bikeaction.org/](https://apps.bikeaction.org/).

## How to run
### Prerequisites
- Docker
  - I recommend just downloading [Docker Desktop](https://www.docker.com/products/docker-desktop/).
  It downloads the docker backend and gives a 
  GUI to manage the Docker containers.

### Install Dependencies
```shell
pip install -r ./requirements.txt
```

### Environment Variables
Assuming you only need to run the website
and do not need to test any APIs (like 
Discord or Mailchimp),
make a file called `.env` in the parent 
directory.

Add these lines:
```
DATABASE_URL = "postgresql://pbaabp:pbaabp@localhost:5432/pbaabp"
DISCORD_BOT_TOKEN = "test"
WP_LOGIN_EMAIL = "test"
WP_LOGIN_PASS = "test"
MAILCHIMP_API_KEY = "test"
MAILCHIMP_AUDIENCE_ID = "test"
DISCORD_OAUTH_CLIENT_ID = "test"
DISCORD_OAUTH_CLIENT_SECRET = "test"
RECAPTCHA_PRIVATE_KEY = "test"
RECAPTCHA_PUBLIC_KEY = "test"
```

## Start the website
Run this make command:
```shell
make migrate
make serve
```