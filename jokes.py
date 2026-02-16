import sys
import pyjokes

LANGUAGES = ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "ru", "sv"]

def read_arg():
    default_lang = "en"

    if len(sys.argv) < 2:
        return default_lang

    arg = sys.argv[1].lower()

    if len(arg) == 3 and arg.startswith("-"):
        lang = arg[1:]
        if lang in LANGUAGES:
            return lang

    return default_lang


def get_single_joke(lang):
    try:
        joke = pyjokes.get_joke(language=lang)
        if isinstance(joke, str) and joke.strip():
            return joke
        else:
            return "Bad joke"
    except Exception:
        return "Bad joke"


def main():
    lang = read_arg()
    joke = get_single_joke(lang)
    print(joke)


if __name__ == "__main__":
    main()
