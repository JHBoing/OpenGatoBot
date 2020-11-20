#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

import logging
import random
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

load_dotenv()

COMMANDS = [
    "PS",
    "GAT",
    "G4T",
    "MIAU",
    "MEOW",
    "SACHE",
    "🐭",
    "🐹",
    "🐀",
    "🐁",
    "🐶",
]

ANSWERS = [
    "mew",
    "meow",
    "MEOW",
    "MEOOOOW",
    "meow meow",
    "*ignorando*",
    "👀",
]


def respond(update: Update, context: CallbackContext) -> None:
    """If the message is in commands list, reply with an answer from answers array."""
    user_message = update.message.text.upper()
    user_message = user_message.split(' ')
    for word in user_message:
        if word.startswith('HTTPS'):
            continue
        if any(command in word for command in COMMANDS):
            update.message.reply_text(ANSWERS[random.randrange(0, len(ANSWERS))])
            break


def main():
    """Start the bot."""
    print("STARTING GATO BOT")
    updater = Updater(os.getenv("TELEGRAM_TOKEN"), use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()