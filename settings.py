from configparser import ConfigParser
import os
config = ConfigParser()
config.read("config.ini")

def set_basic_settings():


    if config["USER"]["language"]=="":
        set_language()

    if config["USER"]["api_hash"]=="" or config["USER"]["api_id"]=="":
        api_id=str(input('>api_id:'))
        api_hash=str(input('>api_hash:'))
        config["USER"]["api_hash"]=api_hash
        config["USER"]["api_id"]=api_id
    with open("config.ini", 'w') as configfile:
        config.write(configfile)
    print(config[config["USER"]["language"]]["settings_basic_end"])

def set_language():
    Languages = ""
    for i in config["INFORM"]["Languages"]:
        if i == 'Ø':
            Languages += '\n'
        else:
            Languages += i

    print(Languages)
    language = input(str(">Select language:"))
    all_language = config.sections()
    all_language.remove('USER')
    all_language.remove('INFORM')
    if language in all_language:
        config["USER"]["language"] = language
    else:
        print("No language in the list")
        set_language()
    with open("config.ini", 'w') as configfile:
        config.write(configfile)
def Delete_session():
    config["USER"]["api_hash"] = ""
    config["USER"]["api_id"] = ""
    with open("config.ini", 'w') as configfile:
        config.write(configfile)
    try:
        os.remove("my_account.session")
    except:
        pass
def start():
    if config["USER"]["api_hash"]=="" or config["USER"]["api_id"]=="" or config["USER"]["language"]=="" :
        set_basic_settings()
    text = ""
    for i in config[config["USER"]["language"]]["settings_start"]:
        if i == 'Ø':
            text += '\n'
        else:
            text += i
    while True:
        print("\n",text)
        comand=str(input(">"))
        print()
        if comand=="del":
            Delete_session()
            print(config[config["USER"]["language"]]["del_end"])
        elif comand=="language":
            set_language()
            print(config[config["USER"]["language"]]["set_languages_end"])
        elif comand=="end":
            break
        else:
            print(config[config["USER"]["language"]]["WTF"])
