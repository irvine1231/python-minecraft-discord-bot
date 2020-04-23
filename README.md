# Python Minecraft Discord Bot

## Introduction

This is a python script for a Discord bot. Based on mcipc, the bot can check the status or get the player list of user-specified Minecraft servers.

## Installation

Requires Python **3.8.0** or higher.

### Setting up

1. Install Python and pip on your system.
2. Check the version of the python in the terminal. The version should be higher than **3.8.0.**
    ```bash
    $ python3 --version
    ```
3. Clone the repository and place it in a folder.
    ```bash
	$ git clone https://github.com/irvine1231/python-minecraft-discord-bot.git
	```
3. Navigate to the folder in the terminal.
    ```bash
    $ cd python-minecraft-discord-bot
    ```
4. Install the requirements
    ```bash
    $ pip3 install -r requirements.txt
    ```
5. Duplicate `.env.example` file and name the copy `.env`.
6. Place your discord bot token, minecraft host, and minecraft port inside the `.env` file.

### Minecraft Server Properties

The `enable-query` configuration inside the minecraft `server.properties` file needs to be set to `true`, otherwise the bot won't work.

## Commands

### !ip

Get the hostname or ip defined in the env file.

### !state

Get the current state of the minecraft server.

### !list

Get the current player list of the minecraft server.

## License

The Python Minecraft Discord Bot is open-sourced software licensed under the MIT license.