import webbrowser
import sys
import pyperclip

parameters = sys.argv

address = ''
if len(parameters) > 1:
    address = ' '.join(parameters[1:])
    print(address)
else:
    RawAddress = pyperclip.paste()
    splitAddress = RawAddress.split()
    address = ' '.join(splitAddress)
    print(address)


# https://www.google.com/maps/place/26+Ash+Grove,+Perth+PH1+1DR/@56.3940755,-3.4833203,17z/data=!3m1!4b1!4m6!3m5!1s0x488624cf2333a217:0x6031fbe57879a4c!8m2!3d56.3940726!4d-3.4807454!16s%2Fg%2F11c259jnl0?entry=ttu
webbrowser.open('https://www.google.com/maps/place/' + address)
