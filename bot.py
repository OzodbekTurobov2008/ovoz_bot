from aiogram import Bot, Dispatcher
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart,Command, or_f
from aiogram import F
from aiogram.types import (Message,InlineQuery,InlineKeyboardButton, InlineQueryResultCachedVoice,)
from data import config
import asyncio
import logging
import sys
from menucommands.set_bot_commands  import set_default_commands
from baza.sqlite import Database
from filterss.admin import IsBotAdminFilter
from filterss.check_sub_channel import IsCheckSubChannels
from keyboard_buttons import admin_keyboard
from aiogram.fsm.context import FSMContext #new
from states.reklama import Adverts, AudioState, AdminMSG
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboard_buttons.admin_keyboard import users_button
import time
from aiogram.fsm.context import FSMContext


ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
from aiogram.filters import Command, CommandObject  
CHANNELS = config.CHANNELS

dp = Dispatcher()

commands = ["/start", "/about", "/help", "/admin"]

@dp.message(CommandStart())
async def start_command(message:Message,state:FSMContext):
 
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id)
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz🙂\nBu bot orqali siz hohlagan ovozingizni topishingiz mumkin!✅", reply_markup=users_button)
        await state.clear()
    except:
        await message.answer(text="Assalomu alaykum", reply_markup=users_button)
        await state.clear()


@dp.message(F.text == 'Assalamu alaykum')
async def get_file_id(message:Message):
    await message.answer_audio(audio="AwACAgIAAxkBAAMXZsMpTpOvz-AJyVCetZVAkUIcRI8AAq03AAIlMLlIsUbLhywDJ2M1BA")

# 
@dp.message(F.text == 'Assalamu alaykum2')
async def get_file_id(message:Message):
    await message.answer_audio(audio="AwACAgIAAxkBAAMhZsMpvTGY587TLAuiwjSAUeAJdc8AAuREAAIP6rBIwIkipU4OiHM1BA")

# 
@dp.message(F.text == 'Bugun sening kuning..😂')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAMkZsMqZ-A91mVuJiK8Stm1iMH-ScAAAn8CAALBpZVQGgOolaXZhU81BA")

#
@dp.message(F.text == 'Nima gaap')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAMnZsMrI83zvZOT8gRIf8Q4_T3B2-0AAo8CAALT9L1RKkqrszuC4DM1BA")

#
@dp.message(F.text == 'Rostan seryozniy?')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAMqZsMrdqoFuj1INNsZn1Y3M97BWVEAAogCAAJR5JRQyfpKj9Pu1yM1BA")

#
@dp.message(F.text == 'Tugadi🤒')
async def get_file_id(message:Message):
      
      await message.answer_audio(audio="AwACAgQAAxkBAAMtZsMr14gTcnE0Q-yE_6CDMQQ0MlEAAlECAAIieI1QDJ4Lg1Fgtt81BA")

#
@dp.message(F.text == 'Auf')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAANdZsMtjuxXy7bFMEpTaq2bPxtMnnAAAmsCAAJ1B41QJYiQiQAB6NmxNQQ")   

#
@dp.message(F.text == 'Tovba qildim')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAANgZsMt5o1Ss3RmqEW7-iZDCpMgspEAAo0CAAIRgI1QDldEwoTRKN81BA")   

#
@dp.message(F.text == 'Maqtov yorliq berilar..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAANjZsMuQLoRY9ktSDr2UJ8mb_5v6dMAAqUCAAJaA5VQI2QGbRL2_nY1BA")   

#
@dp.message(F.text == 'Kulishni boshqachasi...')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAANmZsMuwS1cfRdZmeAuf4r99K_mihYAAnECAAJGAAGVUNMVdryx5FakNQQ")   

#
@dp.message(F.text == 'Oh bunaqalar ko\'payib ketyapti..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAOCZsMv9MN6f3CREwceV1n9o1pVFiMAAn8CAALSHJVQes8rSkAe8ZM1BA")   

#
@dp.message(F.text == 'Shu gapizga monovuni..😂')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAOFZsMwhREzK4dS6hRoocEfAAEc2G2UAAKDAgAC3mZ0Uy5gcCnayffCNQQ")   

#
@dp.message(F.text == 'Qarsaklar bo\'lsin..😂')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAOIZsMw-MTjx4bXTuQfSmB7frDJ8hYAApICAAJ4LoxQdd2PoWDyv7E1BA")   

#
@dp.message(F.text == 'Assalomalekum')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAOLZsMxcTFchCGr92hXlMND0GKrXS0AAqACAAJIh41QAxgPbLgh9sk1BA")   

#
@dp.message(F.text == 'Akang kuchaydi uje😎')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAOOZsMzXShx7ykg6EyIDYy_rvFN1mkAAnYCAAKPTBxQ_xf-lBXFkTI1BA")   

#
@dp.message(F.text == 'Yoqooool..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAORZsMztdEOf3NQ8w4WZv-XZM7XcT4AAlICAAI-CI1QMV__GgfTPpc1BA")   

#
@dp.message(F.text == 'Saviyang yo\'q biliming yo\'q..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAOUZsM0Fii3iNK3Nd0cB0AeGWV-EGcAApACAAKczqRQjTXgOlFfvqM1BA")   

#
@dp.message(F.text == 'Menda uu..😎')
async def get_file_id(message:Message):
   
    await message.answer_audio(audio="AwACAgQAAxkBAAOXZsM0g6b6cJtMa0ZQJh6q1VRLDxIAAlcjAAKuu1lTccqKkYF8rlQ1BA")   

#
@dp.message(F.text == 'Nimalar deyapsan tasqara..🧟‍♀️')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgIAAxkBAAPQZsM3TlrX6F-8M2u8uEfft-taklYAArMOAAJpiZBIlitIUK6MkVw1BA")   

#
@dp.message(F.text == 'Boshing lat yemaganmi?..😂')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgIAAxkBAAOdZsM1dmVBys9CV4_NegvjtjGEf2kAAkQOAAJpiZBI0FOlgDe1qe01BA")   

#
@dp.message(F.text == 'Uzur ketib qopti..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAOgZsM11hYdB0b-7cNQX8zVIk7vPnQAAnQCAALHgpRQ95g9eiPQxxg1BA")   

#
@dp.message(F.text == 'Tilingga shakar ukajonim..😇')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAPTZsM38z42p6yNrrqMcwaD802h38oAAoMCAALpUJRQywoq2XZpRwg1BA")   

#
@dp.message(F.text == 'Ma\'no nima?')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgIAAxkBAAPjZsNAOPxxwn4aeAdjklyk7Kd9tL8AAmNUAAJpQxlKiN2vAe5Sq1w1BA")   

#
@dp.message(F.text == 'Bo\'ldi bas qil')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAPlZsNAghcrDMEbjmT4J-LRW4OUqZsAAnUCAAK195RQC0oMmCmDNOI1BA")   

#
@dp.message(F.text == 'uxlaa')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgIAAxkBAAPxZsNBPQl8oC96qN1D1XITA1uqn_UAArsGAAKJf2hLnT2YP4hsBMI1BA")   

#
@dp.message(F.text == 'Sizdayam pul ko\'payib ketti..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAIBaWbDRjBxFbO3jDYiKBTDdE0YAAEr8AAClAIAAujbjFHFhpdmcJdfxTUE")   

#
@dp.message(F.text == 'Tug\'ulgan kun tabrigi')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAIBsWbDSTGzgOfLcnQ3nt5KS_1IxhrtAAKNAgAC5IBFU4SayJd5qSoSNQQ")   

#
@dp.message(F.text == 'Soqqani qil uka..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAIBvmbDSdgKIZoRx708HONM73uwLgdPAAJ-AgACuYSMUITDpPjaLqm-NQQ")   

#
@dp.message(F.text == 'Oh no oh no')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAIBv2bDShNKk3i_4WV11w5UPiKSL0LDAAKcAgAClN6lUBfaEmnC9c-NNQQ")   

#
@dp.message(F.text == 'Tfu sizga..😂')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAIBwGbDSk2lXOk4SbavwH7EWSmR6JZjAAJwAgACegyVUKTA-A1vnELmNQQ")   

#
@dp.message(F.text == 'Pasportingga erkak deb yozgan..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAIBwmbDSpcbAtKMA2Z2w760E4_PN8JTAAKVAgACQh6NUOn4818MdN2BNQQ")   

#
@dp.message(F.text == 'Pulni kuchi hammasi..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAIBw2bDStugb61CLXdEIi0PrNYMxJ0nAAJOAgACzf2VUMIpcUdfC0SeNQQ")   

#
@dp.message(F.text == 'Aka yozme qo\'yoring..')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgIAAxkBAAIBxGbDSzLqFpAk-yaF7SmpkdRm-HHOAALaCQACxLQISflkeMhFjhjSNQQ")   

#
@dp.message(F.text == 'Kim edi bu?')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgIAAxkBAAIBxWbDTFN0TbaZ6fT4Onv4rx5knHx5AAIWWgACJaUgSjNQTrxXN6NfNQQ")   

#
@dp.message(F.text == 'Dadam o\'ldiradi')
async def get_file_id(message:Message):
    
    await message.answer_audio(audio="AwACAgQAAxkBAAIDwWbDd5FRXJC41GgvOCz_m8pa3h80AAJhBAACpSXEUlITcoAHEwQ9NQQ")   

#
@dp.message(F.text == 'Uff kechasiyam tinchli yõğa😕')
async def get_file_id(message:Message):

    await message.answer_audio(audio="AwACAgQAAxkBAAID2mbEJT3DRnZvAAGrBtOHcc4gxWJJuQACmQgAAslfcFFH9l5-oR-tijUE")   

#
@dp.message(F.text == 'Narmalni bola busen buladiyu uka...')
async def get_file_id(message:Message):

    await message.answer_audio(audio="AwACAgQAAxkBAAIEW2bEYFkHBC0xxDpJK5Al8ViDU-EJAAK3BAACMZXVUcLspu4BSqo0NQQ")   


@dp.message(F.text == 'Buncha tasqarasan')
async def get_file_id(message:Message):
    # audio_id = message.voice.file_id
    # print(audio_id)
    await message.answer_audio(audio="AwACAgIAAxkBAAIJPmbJoJhoGPct-8HcvLuXBEZ_TTl8AAKzDgACaYmQSJYrSFCujJFcNQQ")   


#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("""
🔥Buyruqlar 
Botdan foydalanish ...
/about - Bot haqida 
/start - Botni ishga tushurish
                         
Admin bilan bog'lanmoqchi bo'lsangiz \n👤Admin tugmasini bosing va\n✉️ Xabaringizni yozib qoldiring!""")


@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bot dan shikoyatingiz yoki taklifingiz bo'lsa📜\n👤Admin tugmasini bosing va \nxabaringizni yozib qoldiring✅\n\nBotdan foydalanish tartibi👇🏻\n👉🏻@voise_ovozqani_bot yozib o'zingizga kerakli ovozlarni toping🙂")


@dp.inline_query()
async def inline_voice_search(inline_query: InlineQuery):
    title = inline_query.query
    audiolar = await db.search_audios_title(title)

    results = [
        InlineQueryResultCachedVoice(
            id=f"{audio[0]}",
            voice_file_id=audio[1],
            title=audio[2]
            
        ) for audio in audiolar[:20]
    ]
    await inline_query.answer(results=results)

@dp.inline_query()
async def inline_voice_search(inline_query: InlineQuery):
    title = inline_query.query.strip()

    results = []
    print("***************",title,"***************")
    if not title:
        # No query entered, offer all audio files
        try:
            all_audios = await db.select_all_audios()
            print("***************",all_audios,"***************")
            for item in all_audios[:20]:
                voice_file_id = item[1]
                try:
                    result = InlineQueryResultCachedVoice(
                        id=str(item[0]), 
                        voice_file_id=voice_file_id, 
                        title=item[2]
                    )
                    results.append(result)
                except Exception as e:
                    print(f"Error creating InlineQueryResultCachedVoice for ID {item[0]} with voice_file_id {voice_file_id}: {e}")
                
        except Exception as e:
            print(f"Error fetching all audio files: {e}")
    else:
        # Query entered, search for matching audio files
        try:
            audiolar = await db.search_audios_title(title)
            for audio in audiolar[:20]:
                voice_file_id = audio[1]
                if voice_file_id and isinstance(voice_file_id, str) and voice_file_id.startswith("AwACAg"):
                    try:
                        result = InlineQueryResultCachedVoice(
                            id=str(audio[0]),
                            voice_file_id=voice_file_id,
                            title=audio[2]
                        )
                        results.append(result)
                    except Exception as e:
                        print(f"Error creating InlineQueryResultCachedVoice for ID {audio[0]} with voice_file_id {voice_file_id}: {e}")
                else:
                    print(f"Invalid or malformed voice_file_id: {voice_file_id}")
        except Exception as e:
            print(f"Error searching audio titles: {e}")

    if not results:
        await inline_query.answer(results=[], cache_time=0, switch_pm_text="No results found", switch_pm_parameter="start")
    else:
        try:
            await inline_query.answer(results=results, cache_time=0)
        except Exception as e:
            print(f"Error sending inline query answer: {e}")



@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message:Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index,channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal",url=ChatInviteLink.invite_link))
    inline_channel.adjust(1,repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} kanallarga azo bo'ling!",reply_markup=button)


@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)



@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)



@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin!")


@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.5)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi!")
    await state.clear()


#audio qo'shish


@dp.message(F.text=="audio qo'shish",IsBotAdminFilter(ADMINS))
async def auido_adds(message:Message,state:FSMContext):
    await message.answer("Audio nomini kiriting!")
    await state.set_state(AudioState.title)



@dp.message(F.text,AudioState.title)
async def auido_title(message:Message,state:FSMContext):
    await message.answer("Audio yuboring!")
    title = message.text
    await state.set_state(AudioState.voice_file_id)
    await state.update_data(title=title)


@dp.message(F.voice,AudioState.voice_file_id)
async def auido_voice(message:Message,state:FSMContext):
    data = await state.get_data()
    title = data.get("title")
    voice_file_id = message.voice.file_id
    db.add_audio(voice_file_id=voice_file_id,title=title)

    await message.answer("Tabriklaymiz Audio muvaffaqiyatli bazaga qo'shildi!✅")
    await state.clear()

#-----------------------=========
from aiogram import Bot,Dispatcher,types
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,CallbackQuery,ContentType
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import logging
import sys
from keyboard_buttons import admin_keyboard
from menucommands.set_bot_commands  import set_default_commands
from aiogram.fsm.state import StatesGroup, State


class AdminStates(StatesGroup):
    waiting_for_admin_message = State()
    waiting_for_reply_message = State()


# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define admin states
class AdminStates(StatesGroup):
    waiting_for_admin_message = State()
    waiting_for_reply_message = State()

# Function to create inline keyboard for reply
def create_inline_keyboard(user_id):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text="Javob berish",
        callback_data=f"reply:{user_id}"
    )


    return keyboard_builder.as_markup()



# Admin message handler
@dp.message(F.text == "👤Admin bilan bog'lanish")
async def admin_message(message: Message, state: FSMContext):
    await message.answer("👨‍💼Admin uchun xabar yuboring!")
    await state.set_state(AdminStates.waiting_for_admin_message)

# Admin message handler
@dp.message(AdminStates.waiting_for_admin_message, F.content_type.in_([
    ContentType.TEXT, ContentType.AUDIO, ContentType.VOICE, ContentType.VIDEO,
    ContentType.PHOTO, ContentType.ANIMATION, ContentType.STICKER, 
    ContentType.LOCATION, ContentType.DOCUMENT, ContentType.CONTACT,
    ContentType.VIDEO_NOTE
]))

async def handle_admin_message(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""  # Some users may not have a last name

    # Use username if available, otherwise use first name + last name
    if username:
        user_identifier = f"@{username}"
    else:
        user_identifier = f"{first_name} {last_name}".strip()  # Remove any extra spaces




    video_note = message.video_note
    inline_keyboard = create_inline_keyboard(user_id)
    for admin_id in ADMINS:
        try:
            if video_note:
                print('adfs', message.video_note.file_id)
                # Echo the video note back to the user
                await bot.send_video_note(
                    admin_id,
                    video_note.file_id,
                    reply_markup=inline_keyboard
                )
            elif message.text:
                await bot.send_message(
                    admin_id,
                    f"👤Foydalanuvchi: {user_identifier}\n📜Xabar: {message.text}",
                    reply_markup=inline_keyboard
                )
            elif message.audio:
                await bot.send_audio(
                    admin_id,
                    message.audio.file_id,
                    caption=f"👤Foydalanuvchi: {user_identifier}\n🎙Audio xabar",
                    reply_markup=inline_keyboard
                )
            elif message.voice:
                await bot.send_voice(
                    admin_id,
                    message.voice.file_id,
                    caption=f"👤Foydalanuvchi: {user_identifier}\n⏺Voice xabar",
                    reply_markup=inline_keyboard
                )
            elif message.video:
                await bot.send_video(
                    admin_id,
                    message.video.file_id,
                    caption=f"👤Foydalanuvchi: {user_identifier}\n▶️Video xabar",
                    reply_markup=inline_keyboard
                )
            elif message.photo:
                await bot.send_photo(
                    admin_id,
                    message.photo[-1].file_id,  # using the highest resolution photo
                    caption=f"👤Foydalanuvchi: {user_identifier}\n🏞Rasm xabar",
                    reply_markup=inline_keyboard
                )
            elif message.animation:
                await bot.send_animation(
                    admin_id,
                    message.animation.file_id,
                    caption=f"👤Foydalanuvchi: {user_identifier}\n📜GIF xabar",
                    reply_markup=inline_keyboard
                )
            elif message.sticker:
                await bot.send_sticker(
                    admin_id,
                    message.sticker.file_id,
                    reply_markup=inline_keyboard
                )
            elif message.location:
                await bot.send_location(
                    admin_id,
                    latitude=message.location.latitude,
                    longitude=message.location.longitude,
                    reply_markup=inline_keyboard
                )
            elif message.document:
                await bot.send_document(
                    admin_id,
                    message.document.file_id,
                    caption=f"👤Foydalanuvchi: {user_identifier}\n🗂Hujjat xabar",


                    reply_markup=inline_keyboard
                )
            elif message.contact:
                await bot.send_contact(
                    admin_id,
                    phone_number=message.contact.phone_number,
                    first_name=message.contact.first_name,
                    last_name=message.contact.last_name or "",
                    reply_markup=inline_keyboard
                )
        except Exception as e:
            logging.error(f"Error sending message to admin {admin_id}: {e}")

    await state.clear()
    await bot.send_message(user_id, "Admin sizga javob berishi mumkin!✅")

# Callback query handler for the reply button
@dp.callback_query(lambda c: c.data.startswith('reply:'))
async def process_reply_callback(callback_query: CallbackQuery, state: FSMContext):
    user_id = int(callback_query.data.split(":")[1])
    await callback_query.message.answer("Sizning javobingiz foydalanuvchiga yuborildi!✅")
    await state.update_data(reply_user_id=user_id)
    await state.set_state(AdminStates.waiting_for_reply_message)
    await callback_query.answer()





# Handle admin reply and send it back to the user
@dp.message(AdminStates.waiting_for_reply_message)
async def handle_admin_reply(message: Message, state: FSMContext):
    data = await state.get_data()
    original_user_id = data.get('reply_user_id')

    if original_user_id:
        try:
            if message.text:
                await bot.send_message(original_user_id, f"Admin javobi✅\n{message.text}")
            elif message.voice:
                await bot.send_voice(original_user_id, message.voice.file_id)

            elif message.video_note:
                await bot.send_video_note(original_user_id, message.video_note.file_id)

            elif message.audio:
                await bot.send_audio(original_user_id, message.audio.file_id)
            
            elif message.sticker:
                await bot.send_sticker(original_user_id, message.sticker.file_id)
            
            elif message.video:
                await bot.send_video(original_user_id, message.video.file_id)


            await bot.send_message(ADMINS[0], "Foydalanuvchiga habaringiz yuborildi!✅")            
            await state.clear()  # Clear state after sending the reply
        except Exception as e:
            logger.error(f"Error sending reply to user {original_user_id}: {e}")
            await message.reply("Xatolik: Javob yuborishda xato yuz berdi.")
    else:
        await message.reply("Xatolik: Javob yuborish uchun foydalanuvchi ID topilmadi.")



@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)


#bot ishga tushganini xabarini yuborish
@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from middlewares.throttling import ThrottlingMiddleware

    # Spamdan himoya qilish uchun klassik ichki o'rta dastur. So'rovlar orasidagi asosiy vaqtlar 0,5 soniya
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))

async def main() -> None:
    global bot,db
    bot = Bot(TOKEN)
    db = Database(path_to_db="data/main.db")
    db.create_table_users()
    db.create_table_audios()
    await set_default_commands(bot)
    await dp.start_polling(bot)
    setup_middlewares(dispatcher=dp, bot=bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())