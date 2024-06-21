from colorama import Fore, Style

def translate_text(session, source_language_code, target_language_code):
    translate = session.client('translate')
    text = input(Fore.YELLOW + "Enter text to translate: ")

    result = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
    )

    print(Fore.GREEN + f"Translated text: {result['TranslatedText']}")


