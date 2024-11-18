import datetime

print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Loading libraries...\n[{datetime.datetime.now().strftime('%H:%M:%S')}] The loading speed depends on the power of your device.")

import asyncio
import json
import os
import re
import webbrowser
import time

import psutil
import pyautogui
import pygetwindow
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

def print_error(message):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [ERROR] {message}")

def print_warn(message):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [WARN] {message}")

def print_info(message):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] {message}")

async def windowHandler(windowTitle, checkDelay):
    global window, x, y, width, height
    while True:
        try:
            window = pygetwindow.getWindowsWithTitle(f'{windowTitle}')[0]
            if not window.isMinimized:
                window_info = extract_window_info(str(window))
                if window_info:
                    x, y, width, height, title = window_info
                    y = y + 31
                    x = x + 8
                    width = width - 16
                    height = height - 39
        except:
            print_error("The window was closed. An attempt to update the information.")
        await asyncio.sleep(float(checkDelay))

async def sticker(webhookUrl, checkDelay):
    global att, window, x, y, winth, height
    await asyncio.sleep(float(checkDelay))
    while True:
        if window.isActive:
            try:
                posLower = pyautogui.locateCenterOnScreen(image="assets/sticker-lower.png", confidence=0.74, region=(x, y, width, height), grayscale=False)
                if posLower:
                    pyautogui.screenshot(f"{att}.png", region=(x, y, width, height))
                    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [{att}] find (sticker-lower.png)")
                    try:
                        webhook = DiscordWebhook(url=webhookUrl)
                        embed = DiscordEmbed(title=None,
                                             description=f"[{datetime.datetime.now().strftime('%H:%M:%S')}] You found the sticker! (sticker-lower.png)",
                                             color=0xffffff)
                        with open(f"{att}.png", "rb") as f:
                            webhook.add_file(file=f.read(), filename="image.png")
                        embed.set_image(url="attachment://image.png")
                        webhook.add_embed(embed)
                        webhook.execute()
                    except:
                        print_error("An error occurred while trying to send a Discord Webhook message")
                    os.remove(f"{att}.png")
                    await asyncio.sleep(3.85)
            except:
                try:
                    posLow = pyautogui.locateCenterOnScreen(image="assets/sticker-low.png", confidence=0.75, region=(x, y, width, height), grayscale=False)
                    if posLow:
                        pyautogui.screenshot(f"{att}.png", region=(x, y, width, height))
                        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [{att}] find (sticker-low.png)")
                        try:
                            webhook = DiscordWebhook(url=webhookUrl)
                            embed = DiscordEmbed(title=None,
                                                 description=f"[{datetime.datetime.now().strftime('%H:%M:%S')}] You found the sticker! (sticker-low.png)",
                                                 color=0xffffff)
                            with open(f"{att}.png", "rb") as f:
                                webhook.add_file(file=f.read(), filename="image.png")
                            embed.set_image(url="attachment://image.png")
                            webhook.add_embed(embed)
                            webhook.execute()
                        except:
                            print_error("An error occurred while trying to send a Discord Webhook message")
                        os.remove(f"{att}.png")
                        await asyncio.sleep(3.85)
                except:
                    try:
                        posMedium = pyautogui.locateCenterOnScreen(image="assets/sticker-medium.png", confidence=0.753,region=(x, y, width, height), grayscale=False)
                        if posMedium:
                            pyautogui.screenshot(f"{att}.png", region=(x, y, width, height))
                            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [{att}] find (sticker-medium.png)")
                            try:
                                webhook = DiscordWebhook(url=webhookUrl)
                                embed = DiscordEmbed(title=None,
                                                     description=f"[{datetime.datetime.now().strftime('%H:%M:%S')}] You found the sticker! (sticker-medium.png)",
                                                     color=0xffffff)
                                with open(f"{att}.png", "rb") as f:
                                    webhook.add_file(file=f.read(), filename="image.png")
                                embed.set_image(url="attachment://image.png")
                                webhook.add_embed(embed)
                                webhook.execute()
                            except:
                                print_error("An error occurred while trying to send a Discord Webhook message")
                            os.remove(f"{att}.png")
                            await asyncio.sleep(3.85)
                    except:
                        try:
                            pos = pyautogui.locateCenterOnScreen(image="assets/sticker.png", confidence=0.765,region=(x, y, width, height), grayscale=False)
                            if pos:
                                pyautogui.screenshot(f"{att}.png", region=(x, y, width, height))
                                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [{att}] find (sticker.png)")
                                try:
                                    webhook = DiscordWebhook(url=webhookUrl)
                                    embed = DiscordEmbed(title=None,
                                                         description=f"[{datetime.datetime.now().strftime('%H:%M:%S')}] You found the sticker! (sticker.png)",
                                                         color=0xffffff)
                                    with open(f"{att}.png", "rb") as f:
                                        webhook.add_file(file=f.read(), filename="image.png")
                                    embed.set_image(url="attachment://image.png")
                                    webhook.add_embed(embed)
                                    webhook.execute()
                                except:
                                    print_error("An error occurred while trying to send a Discord Webhook message")
                                os.remove(f"{att}.png")
                                await asyncio.sleep(3.85)
                        except:
                            pass
            att += 1
        await asyncio.sleep(float(checkDelay))

async def ohSticker(webhookUrl, checkDelay):
    global att, window, x, y, winth, height
    await asyncio.sleep(float(checkDelay))
    while True:
        if window.isActive:
            try:
                pos = pyautogui.locateCenterOnScreen(image="assets/oh.png", confidence=0.675, region=(x, y, width, height), grayscale=True)
                if pos:
                    pyautogui.screenshot(f"{att}.png", region=(x, y, width, height))
                    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [{att}] Oh, you found something! (oh.png)")
                    try:
                        webhook = DiscordWebhook(url=webhookUrl)
                        embed = DiscordEmbed(title=None,
                                             description=f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Oh! Something found the sticker (oh.png)",
                                             color=0xff0000)
                        with open(f"{att}.png", "rb") as f:
                            webhook.add_file(file=f.read(), filename="image.png")
                        embed.set_image(url="attachment://image.png")
                        webhook.add_embed(embed)
                        webhook.execute()
                    except:
                        print_error("An error occurred while trying to send a Discord Webhook message")
                    os.remove(f"{att}.png")
                    await asyncio.sleep(3.85)
            except:
                pass
            att += 1
        await asyncio.sleep(float(checkDelay))

async def find(webhookUrl, checkDelay, windowTitle):
    global att
    att = 1
    tasks = [asyncio.create_task(sticker(webhookUrl, checkDelay)),
             asyncio.create_task(ohSticker(webhookUrl, checkDelay)),
             asyncio.create_task(windowHandler(windowTitle, checkDelay))]
    await asyncio.gather(*tasks)

def start(webhookUrl, nameProc, windowTitle, checkDelay):
    global version
    try:
        app_found = False
        for proc in psutil.process_iter():
            try:
                if proc.name() == nameProc:
                    app_found = True
                    break
            except:
                print_error("An error occurred during the process check!")
                time.sleep(3)
                return

        if not app_found:
            print_error("The game process was not found. Start the game and restart this script!")
            time.sleep(3)
            return

        else:
            print_info("The game process has been successfully found!")

            window = pygetwindow.getWindowsWithTitle(f'{windowTitle}')[0]

            if window.isMinimized:
                window.restore()
                print_warn("The window was automatically opened because it was minimized!")

            if not window.isMinimized:
                window_info = extract_window_info(str(window))
                if window_info:
                    x, y, width, height, title = window_info
                    y = y + 31
                    x = x + 8
                    width = width - 16
                    height = height - 39
                    try:
                        webhook = DiscordWebhook(url=webhookUrl)
                        embed = DiscordEmbed(title=f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Sticker Informer is connected!",
                                              description=f"Application Version: `{version}`\nCheck delay: `{checkDelay}`",
                                              color=0x0047ab)
                        webhook.add_embed(embed)
                        webhook.execute()
                    except:
                        print_error("Connection error to the Discord webhook!")
                        time.sleep(3)
                        return
                    print_info(f"The window was found on X:{x} Y:{y} W:{width} H:{height}")
                    if os.path.exists("assets/oh.png") and os.path.exists("assets/sticker.png") and os.path.exists("assets/sticker-low.png") and os.path.exists("assets/sticker-medium.png") and os.path.exists("assets/sticker-lower.png"):
                        asyncio.run(find(webhookUrl, checkDelay, windowTitle))
                    else:
                        print_error("The contents of the \"assets\" folder are corrupted!")
                        time.sleep(3)
                        return
    except Exception as e:
        print_error(f"An unknown error has occurred! {e}")
        time.sleep(3)
        return

def extract_window_info(window_str):
    pattern = r"left=\"(-?\d+)\", top=\"(-?\d+)\", width=\"(\d+)\", height=\"(\d+)\", title=\"(.*)\""
    match = re.search(pattern, window_str)
    if match:
        left, top, width, height, title = match.groups()
        return int(left), int(top), int(width), int(height), title
    else:
        return None

def check_version():
    global version
    version = 1.2
    try:
        response = requests.get('https://api.github.com/repos/mochensky/Sticker-Informer/releases/latest')
        latest_version = response.json()['tag_name']
        if float(version) < float(latest_version):
            print_info(f"Your version {version} is outdated. The latest version is {latest_version}!")
            update_choice = input(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [INFO] Do you want to update to the latest version? (y/n) ")
            if update_choice.lower() == 'y':
                webbrowser.open("https://github.com/mochensky/Sticker-Informer/releases/latest")
                print_info("Update link opened in your browser.")
                exit()
            else:
                print_info("Update skipped.")
        else:
            print_info(f"Your version {version} is up to date!")
    except requests.exceptions.RequestException as e:
        print_error(f"An error occurred while checking the version: {e}")
        time.sleep(3)
        return

if __name__ == "__main__":
    try:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Successfully loaded!\n[{datetime.datetime.now().strftime('%H:%M:%S')}] For more information on usage, see: https://github.com/mochensky/Sticker-Informer/blob/main/README.md")

        check_version()

        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] ↓ Link to the discord webhook. Enter \"-\" to set the value from config.json.")
        webhookUrl = input(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Webhook url: ")
        nameProc = "RobloxPlayerBeta.exe"
        windowTitle = "Roblox"
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] ↓ The frequency of the screen check. The more powerful your device is, the less you can bet. 1.0 is recommended")
        checkDelay = input(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Check delay: ")

        if webhookUrl == "-":
            try:
                with open("config.json", "r") as f:
                    data = json.load(f)
                    webhookUrl = data["webhookUrl"]
            except FileNotFoundError:
                print_warn("config.json was not found, let's create it.")
                data = {"webhookUrl": "https://discord.com/api/webhooks/serverID/webhookUrl"}
                with open("config.json", "w") as f:
                    json.dump(data, f, indent=4)
                print_info("config.json has been created successfully.")
        else:
            data = {"webhookUrl": webhookUrl}
            with open("config.json", "w") as f:
                json.dump(data, f, indent=4)

        try:
            checkDelay = float(checkDelay)
        except:
            print_error("checkDelay format error. Int and float values are accepted!")
            time.sleep(3)
            exit()

        start(webhookUrl, nameProc, windowTitle, checkDelay)
    except KeyboardInterrupt:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] [WARN] The program has been stopped.")
        exit()