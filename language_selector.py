from colorama import Fore, Style

def list_supported_languages(session, region):
    translate = session.client('translate', region_name=region)
    response = translate.list_languages()
    languages = {index + 1: language['LanguageName'] for index, language in enumerate(response['Languages'])}
    return languages
from colorama import Fore, Style

def list_supported_languages(session, region):
    translate = session.client('translate', region_name=region)
    response = translate.list_languages()
    languages = {index + 1: (language['LanguageName'], language['LanguageCode']) for index, language in enumerate(response['Languages'])}
    return languages

def select_language(session, region):
    languages = list_supported_languages(session, region)
    print(Fore.CYAN + "Select source language (enter the number):")
    for key, value in languages.items():
        print(f"{key}. {value[0]}")
    source_language_code = languages[int(input(Fore.YELLOW + "Select source language number: "))][1]

    print(Fore.CYAN + "Select target language (enter the number):")
    for key, value in languages.items():
        print(f"{key}. {value[0]}")
    target_language_code = languages[int(input(Fore.YELLOW + "Select target language number: "))][1]

    return source_language_code, target_language_code

if __name__ == "__main__":
    from aws_login import login_to_aws
    session, region = login_to_aws()
    if session and region:
        source_language_code, target_language_code = select_language(session, region)
        print(f"Source Language Code: {source_language_code}, Target Language Code: {target_language_code}")
