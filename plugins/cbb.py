import pyrogram

from plugins.help_text import rename_cb, cancel_extract
from plugins.rename_file import force_name
from plugins.rename_video import force_name


@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button1" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)

    if "rename_button2" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)
        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
