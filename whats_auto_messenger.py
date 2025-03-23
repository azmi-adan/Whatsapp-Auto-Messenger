import os
import time
import pyautogui
import random

# WhatsApp Desktop path (update if needed)
whatsapp_path = "<YOUR_WHATSAPP_PATH>"

# Contact details
contact_name = "<CONTACT_NAME>"  # Searching by name

# List of messages
messages = [
    f"Hey {contact_name}! Hope you're having a great day! 😊",
    "Remember to stay focused and keep pushing forward! 💪",
    "Just a reminder: Success is built on consistency! 🚀",
    "Take a deep breath, relax, and keep going! 🌿",
    "Hard work always pays off. Stay patient! 🔥",
    "Don't forget to take breaks and take care of yourself! ☕",
]

def open_whatsapp():
    """Opens WhatsApp Desktop"""
    print(f"📩 Opening WhatsApp Desktop...")
    os.startfile(whatsapp_path)  
    time.sleep(10)  # Wait for WhatsApp to open

def send_message():
    """Sends a random message via WhatsApp Desktop"""
    try:
        message = random.choice(messages)
        print(f"📩 Sending message to {contact_name}: {message}")

        # Ensure WhatsApp is in focus
        pyautogui.hotkey("alt", "tab")  # Switch to WhatsApp
        time.sleep(2)

        # Open the search bar
        pyautogui.hotkey("ctrl", "f")
        time.sleep(2)

        # Type the contact name and press Enter
        pyautogui.write(contact_name)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(3)  # Wait for chat to load

        # Force-click the chat area to remove focus from search
        pyautogui.click(x=300, y=300)  # Adjust coordinates if needed
        time.sleep(2)

        # Click the message input box (adjust coordinates if needed)
        pyautogui.click(x=600, y=900)  
        time.sleep(2)

        # Type the message
        pyautogui.write(message)
        time.sleep(2)

        # Press "Enter" to send
        pyautogui.press("enter")

        print("✅ Message sent!")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the script
open_whatsapp()
send_message()