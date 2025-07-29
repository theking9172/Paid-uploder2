from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus
from vars import SUDO_USERS, ADMIN_USERS

# Channel details
CHANNEL_ID = -1002560767555  # Replace this with your actual channel ID from @getidsbot
CHANNEL_LINK = "https://t.me/+2uO7pFGrYNVkZWNl"  # Keep this for the join button
FORCE_SUB_PHOTO = "https://files.catbox.moe/i2m700"

__all__ = ['force_sub', 'force_subscribe_prompt']

async def check_subscription(client: Client, user_id: int) -> bool:
    try:
        # Fast admin/sudo check - return immediately if true
        if user_id in SUDO_USERS or user_id in ADMIN_USERS:
            return True

        # Try to get chat member status
        try:
            member = await client.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
            return member.status in [
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR
            ]
        except Exception:
            return False
                
    except Exception:
        return False

async def force_subscribe_prompt(client: Client, message):
    try:
        keyboard = [
            [
                InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK),
                InlineKeyboardButton("✅ Verify", callback_data="check_subscription")
            ],
            [
                InlineKeyboardButton("🔄 Refresh", callback_data="refresh_subscription")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await message.reply_photo(
            photo=FORCE_SUB_PHOTO,
            caption=(
                "**⚠️ Access Denied!**\n\n"
                "**🔰 Join Requirements:**\n"
                "1️⃣ Click 'Join Channel' button\n"
                "2️⃣ Join our channel\n"
                "3️⃣ Click 'Verify' button\n"
                "4️⃣ If verification fails, click 'Refresh'\n\n"
                "**🌟 You must join the channel to use this bot!**\n"
                "**⚠️ If you leave the channel, you will lose access!**"
            ),
            reply_markup=reply_markup
        )
    except Exception as e:
        print(f"Force subscribe prompt error: {str(e)}")
        await message.reply_text(
            "**⚠️ Access Denied!**\n\n"
            "**🔰 Join Requirements:**\n"
            "1️⃣ Click 'Join Channel' button\n"
            "2️⃣ Join our channel\n"
            "3️⃣ Click 'Verify' button\n"
            "4️⃣ If verification fails, click 'Refresh'\n\n"
            "**🌟 You must join the channel to use this bot!**\n"
            "**⚠️ If you leave the channel, you will lose access!**",
            reply_markup=reply_markup
        )

def force_sub(func):
    async def wrapper(client: Client, message):
        try:
            # Skip all checks for admins/sudo users
            if message.from_user and (message.from_user.id in SUDO_USERS or message.from_user.id in ADMIN_USERS):
                return await func(client, message)

            # Skip check for channel messages
            if message.chat.type in ["channel", "group", "supergroup"]:
                return await func(client, message)

            user_id = message.from_user.id
            
            # Check if user is subscribed
            if not await check_subscription(client, user_id):
                await force_subscribe_prompt(client, message)
                return
                
            return await func(client, message)
        except Exception as e:
            print(f"Force sub wrapper error: {str(e)}")
            return
    return wrapper

@Client.on_callback_query(filters.regex("^check_subscription$"))
async def verify_callback(client: Client, callback_query):
    try:
        user_id = callback_query.from_user.id
        print(f"Verify button clicked by user {user_id}")
        
        # Check if user is actually subscribed
        is_subscribed = await check_subscription(client, user_id)
        print(f"Subscription check result for user {user_id}: {is_subscribed}")
        
        if is_subscribed:
            print(f"User {user_id} verified successfully")
            # Delete the join message
            await callback_query.message.delete()
            # Send success message
            await callback_query.message.reply_text(
                "**✅ Subscription Verified!**\n\n"
                "**Thank you for joining our channel. You can now use the bot!**\n\n"
                "**Now send /start to use the bot!**\n\n"
                "**⚠️ Remember: If you leave the channel, you will lose access!**"
            )
        else:
            print(f"User {user_id} verification failed - not subscribed")
            # If not subscribed, show alert
            await callback_query.answer(
                "⚠️ You haven't joined the channel yet! Please join first.",
                show_alert=True
            )
    except Exception as e:
        print(f"Verify callback error for user {callback_query.from_user.id}: {str(e)}")
        await callback_query.answer("Error occurred. Please try again.", show_alert=True) 
