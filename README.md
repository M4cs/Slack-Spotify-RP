# Slack-Spotify Rich Presence
### Lightweight, Fast, and Open Source Rich Presence Program for Spotify and Slack!

<p>
    <p align="center"><center><img src="https://raw.githubusercontent.com/M4cs/Slack-Spotify-RP/master/images/example.gif"></center></p>
<p>

## Overview

Slack-Spotify-RP (SSRP) is a tool that brings the functionality of Spotify Rich Presence to Slack! Now you can display and share what you're listening to with friends in under 3 minutes! It's extremely simple to setup with an easy to use authorization panel and a simple configuration! SSRP is still new and can always be improved upon! If you have any suggestions for features or issues please open up a new GitHub Issue!

## Getting Started

**SSRP is written in Python and requires Python 3.6 or above.**

### Installation:

First clone the repository or download it as a `.zip` file:

```
# To Clone
git clone https://github.com/M4cs/Slack-Spotify-RP
```

Next you need to install the required modules. You should already have the `requests` module if you are a Python developer but I also use a library called `colorama`. If you do not want this on your user's site-packages, use a Virtual Env or Pipenv! Run:

```
cd Slack-Spotify-RP
pip install -r requirements.txt

# or setup Virtual Env
pip install virtualenv
virtualenv .venv

# On *nix
source .venv/bin/activate

# On Windows
.venv\Scripts\activate.bat
```

Now you are all setup to start running and setting up your configuration.

#### Video Tutorial for Configuration Flow (English)

[![](https://img.youtube.com/vi/YbBKw0eh520/mqdefault.jpg)](https://youtu.be/YbBKw0eh520)

## Configuration Guide:

### Default Config:

```json
{
    "spotify_auth_token": "NONE",
    "spotify_refresh_token": "NONE",
    "slack_workspaces": [],
    "update_interval": 5,
    "format": "song - artist | [album]"
}
```

### Config Description:

- **spotify_auth_token -** Access Token Generated from [the SSRP Spotify Authentication Portal](https://ssrp.maxbridgland.com/authorize) for Spotify
- **spotify_refresh_token -** Refresh Token Generated from [the SSRP Spotify Authentication Portal](https://ssrp.maxbridgland.com/authorize) to get new Access Tokens when they expire (1 time per hour)
- **slack_workspaces -** Array of Slack User tokens Generated from [the SSRP Slack Authentication Portal](https://ssrp.maxbridgland.com/authorize_slack). *One per workspace*. Starts with `xoxp`
- **update_interval -** Update interval to update Slack status (seconds)
- **format -** Formatting for Slack Status. Read below for more info on formatting.

**Formatting.** The formatting value allows 3 placeholders: `song`, `album`, `artist`. You can set this however you like but wherever you put one of those words, it will be replaced. Spelling typos will break this!!

## Support Links

**Fastest Method of Support:**

Tweet to me! You can find me on Twitter [@maxbridgland](https://twitter.com/maxbridgland)

**Other Methods of Contact:**

[Discord Support Server](https://discord.gg/NjxjCQQ)

[E-Mail Me](mailto://mabridgland@protonmail.com)

## Contributing

If you'd like to contribute feel free to make a Pull Request. I have no desire to standardize PRs as I doubt I'll get any. If you do end up making one be sure to include:

- Thoughtful commit messages
- A detailed changelog in the PR info
- Updates to dependencies if you add any

## License

This software is licensed under the MBCL (Max Bridgland Copyright-ish License)

You as a user and a contributor willingly accept, by using this software,
that you cannot and WILL NOT redistribute ANY part of this code without
due credit. Due credit means: 1) My name, Max Bridgland, clearly stated
on the main page of the website where it is hosted. 2) A link to this
source code, NOT A FORK, somewhere on the main page of where it is hosted.
3) You do not take credit for any part of this project or the code used
in it.

If you are okay with these terms, you are FREE TO: 1) Fork and contribute to
this project. 2) Make Pull Requests with your changes on them 3) Use this
software for your own personal enjoyment and do not take credit for creating
it. 4) Share links to articles or the direct source of this project. 

You are by NO MEANS allowed to: 1) Redistribute this code as your own 2)
Host the source code of this project under another domain other than GitHub
as a FORKED REPO 3) Profit in any way, shape, or form from use of this
software

This project cannot be used for commercial purposes. Any repos that fork
the project MUST INCLUDE THIS LICENSE in the root of the repository.

If any terms in this license are broken you give me the full right to make
a DMCA claim on your project and take any legal precautions towards copyright
infringement.
