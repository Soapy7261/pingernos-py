from re import sub
from json import load, decoder
from os import getenv
from sys import exit
try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    print('You did not install the dotenv module! You will not be able to use a .env file.')
class Utils:
    @staticmethod #This is a static method, you can call it without creating an instance of the class, but does not have access to the class or its attributes (self)
    def Remove_Colors_From_String(text):
        text = sub(r"§[0-9a-r]", "", text)
        return text
    class Colors:
        blue = 0xadd8e6
        red = 0xf04747
        green = 0x90ee90
        orange = 0xfaa61a
    @staticmethod
    def GetData():
        usejson = True #Set to False to use enviorment variables instead of config.json
        if usejson:
            try:
                with open('config.json', 'r', encoding="UTF-8") as file:
                    return load(file)
            except FileNotFoundError:
                print('config.json not found! Exiting now...')
                exit()
            except decoder.JSONDecodeError:
                print('config.json is not valid! Exiting now...')
                exit()
            except EncodingWarning:
                print('config.json is not encoded in UTF-8! Exiting now...')
                exit()
            except Exception as error:
                print(f'An error occured while reading config.json! Exiting now...\n{error}')
                exit()
        if not usejson:
            #If you don't fill out the environment variables, it will return empty and probably crash, so make sure you fill them out!
            return {
                "Token": getenv('TOKEN'),
                "Prefix": getenv('PREFIX'),
                "Owners": getenv('OWNERS').split(','),
                "Database": {
                    "Host": getenv('DB_HOST'),
                    "User": getenv('DB_USER'),
                    "Password": getenv('DB_PASSWORD'),
                    "Database": getenv('DB_DATABASE'),
                    "Port": getenv('DB_PORT')
                }
            }
