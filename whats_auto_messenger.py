import os
import time
import pyautogui
import random

# WhatsApp Desktop path (update if needed)
whatsapp_path = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2509.4.0_x64__cv1g1gvanyjgm\WhatsApp.exe"

# Contact details
contact_name = "Hooyo"  # Searching by name

# List of messages
messages = [
    "Hey Hooyo! Hope you're having a great day! 😊",
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
    time.sleep(10)  # Wait for WhatsApp to open fully

def send_message():
    """Sends a random message via WhatsApp Desktop"""
    try:
        message = random.choice(messages)
        print(f"📩 Sending message to {contact_name}: {message}")

        # Open the search bar
        pyautogui.hotkey("ctrl", "f")
        time.sleep(1)

        # Type the contact name and press Enter
        pyautogui.write(contact_name, interval=0.1)  # Adds slight delay to avoid typos
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(3)  # Wait for chat to load

        # Check if the contact name is correct
        pyautogui.screenshot("whatsapp_screen.png")  # Debugging step
        time.sleep(1)

        # Click the chat area (adjust coordinates if needed)
        pyautogui.click(x=300, y=300)
        time.sleep(1)

        # Click the message input box (adjust coordinates based on screen resolution)
        pyautogui.click(x=600, y=900)  
        time.sleep(1)

        # Type and send the message
        pyautogui.write(message, interval=0.05)  # Adds a natural typing effect
        time.sleep(1)
        pyautogui.press("enter")

        print("✅ Message sent!")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the script
open_whatsapp()
send_message()
