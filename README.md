# Discord Utility Bot (Experimental)

> ⚠️ **Warning**  
> This project contains **high-impact administrative commands**.  
> **Only use in private test servers where you have full ownership and explicit permission.**  
> Misuse may violate the Terms of Service of :contentReference[oaicite:0]{index=0} and can result in account or server bans.

## Overview

A simple experimental Discord bot written in Python using `discord.py`.  
The bot listens for prefixed commands and performs server-level administrative actions.

This repository is intended **for learning, experimentation, and controlled environments only**.

---

## Features

- Command-based interaction using a configurable prefix
- Environment variable configuration
- Asynchronous task handling with `asyncio`
- Server-level commands, including:
  - Channel deletion
  - Channel creation (spam testing)
  - Server renaming
  - Member banning (with bypass list)

---

## Configuration

The bot relies on **environment variables**:

| Variable | Description |
|--------|------------|
| `Token` | Your Discord bot token |
| `Command_Prefix` | Prefix used to trigger commands (e.g. `!`) |

You can also configure:
- `MaxSpamChannelCount` – maximum number of channels created
- `BypassedUserIds` – user IDs protected from moderation actions

---

## Commands

| Command | Description |
|-------|-------------|
| `kaboom` | Deletes all channels in the server |
| `spamchannels <name>` | Creates many text channels with the given name |
| `servername <new name>` | Changes the server name |
| `banall` | Bans all members except bypassed IDs |

---

## Usage Notes

- Designed for **testing bot permissions and event handling**
- Requires **administrator-level permissions**
- Not suitable for public servers
- Error handling is minimal by design

---

## Disclaimer

This project is provided **as-is** for educational purposes.  
The author is not responsible for misuse, data loss, or violations of platform rules.

---

## License

No license specified.  
Do not redistribute or deploy without understanding the consequences.
