import asyncio
from random import choice

from telethon import TelegramClient
from telethon.events import NewMessage

APP_ID = 21595595
API_HASH = '4f254e2cf003f527f94da5109d17b332'

HEART = '🤍'
COLORED_HEARTS = ['💗', '💓', '💖', '💘', '❤️', '💞']
MAGIC_PHRASES = ['.huy']
EDIT_DELAY = 0.01

PARADE_MAP = '''
000000000
000111000
001010100
001010100
001000100
001111100
001000100
001000100
001000100
001000100
001000100
001000100
001000100
001000100
001000100
001101100
010010010
010010010
010010010
001101100
000000000
'''

client = TelegramClient('tg-account', APP_ID, API_HASH)


def generate_parade_colored():
    output = ''
    for c in PARADE_MAP:
        if c == '0':
            output += HEART
        elif c == '1':
            output += choice(COLORED_HEARTS)
        else:
            output += c
    return output


async def process_love_words(event: NewMessage.Event):
    await client.edit_message(event.peer_id.user_id, event.message.id, 'You')
    await asyncio.sleep(1)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'You should')
    await asyncio.sleep(1)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'You should-(on)')
    await asyncio.sleep(1)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'You should-(on) love')
    await asyncio.sleep(1)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'You should-(on) love dick💗')


async def process_build_place(event: NewMessage.Event):
    output = ''
    for i in range(8):
        output += '\n'
        for j in range(11):
            output += HEART
            await client.edit_message(event.peer_id.user_id, event.message.id, output)
            await asyncio.sleep(EDIT_DELAY / 2)


async def process_colored_parade(event: NewMessage.Event):
    for i in range(50):
        text = generate_parade_colored()
        await client.edit_message(event.peer_id.user_id, event.message.id, text)

        await asyncio.sleep(EDIT_DELAY)


@client.on(NewMessage(outgoing=True))
async def handle_message(event: NewMessage.Event):
    if event.message.message in MAGIC_PHRASES:
        await process_build_place(event)
        await process_colored_parade(event)
        await process_love_words(event)


if __name__ == '__main__':
    print('[*] Подключение к клиенту...')
    print('[*] Пожалуйста подождите')
    print('[*] Код работает без Root прав')
    client.start()
    client.run_until_disconnected()
