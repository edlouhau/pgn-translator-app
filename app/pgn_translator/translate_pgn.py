import re
from deep_translator import GoogleTranslator

languages = {
    "en": ["P", "N", "B", "R", "Q", "K"],  # English
    "es": ["P", "C", "A", "T", "D", "R"],  # Spanish
    "cs": ["P", "J", "S", "V", "D", "K"],  # Czech
    "da": ["B", "S", "L", "T", "D", "K"],  # Danish
    "nl": ["O", "P", "L", "T", "D", "K"],  # Dutch
    "et": ["P", "R", "O", "V", "L", "K"],  # Estonian
    "fi": ["P", "R", "L", "T", "D", "K"],  # Finnish
    "fr": ["P", "C", "F", "T", "D", "R"],  # French
    "de": ["B", "S", "L", "T", "D", "K"],  # German
    "hu": ["G", "H", "F", "B", "V", "K"],  # Hungarian
    "is": ["P", "R", "B", "H", "D", "K"],  # Icelandic
    "it": ["P", "C", "A", "T", "D", "R"],  # Italian
    "no": ["B", "S", "L", "T", "D", "K"],  # Norwegian
    "pl": ["P", "S", "G", "W", "H", "K"],  # Polish
    "pt": ["P", "C", "B", "T", "D", "R"],  # Portuguese
    "ro": ["P", "C", "N", "T", "D", "R"],  # Romanian
    "sv": ["B", "S", "L", "T", "D", "K"],  # Swedish
}


def translate_pgn_game(source_language, target_language, game):
    if source_language not in languages.keys():
        raise ValueError(f"Invalid source language: {source_language}.")
    if target_language not in languages.keys():
        raise ValueError(f"Invalid target language: {target_language}.")
    
    languages_piece_letters = languages[source_language]
    piece_letters = "".join(languages_piece_letters)

    pattern = f'[{piece_letters}]?[a-h]?[1-8]?[x]?[a-h][1-8][+#]?[?!]*'
    piece_move = re.findall(pattern,game)
    all_moves = " ".join(piece_move)
    
    source_and_target_language_map = {}
    for source, target in zip(languages[source_language], languages[target_language]):
        source_and_target_language_map[source] = target

    for token_character in source_and_target_language_map.keys():
        source_lang_character = token_character
        target_lang_character = source_and_target_language_map[token_character]
        all_moves = all_moves.replace(source_lang_character, target_lang_character)
    
    all_moves = all_moves.split()
    
    def replace(_):
        return all_moves.pop(0)

    game = re.sub(pattern,replace,game) 
    return(game)


def translate_pgn_move_token(source_language, target_language, move_token):
    if source_language not in languages.keys():
        raise ValueError(f"Invalid source language: {source_language}.")
    if target_language not in languages.keys():
        raise ValueError(f"Invalid target language: {target_language}.")

    piece_letters = languages[source_language] + languages[target_language]
    if move_token and move_token[0].isupper() and move_token[0] not in piece_letters:
        raise ValueError(f"Invalid token: {move_token}.")

    source_and_target = {}
    for source, target in zip(languages[source_language], languages[target_language]):
        source_and_target[source] = target

    for token_character in source_and_target.keys():
        move_token = move_token.replace(token_character, source_and_target[token_character])

    return move_token

def translate_tags_comments(source_language, target_language, game):
    """
    Finds the tags and comments in the game, translates them, and replaces them.
    """
    tags_comments_pattern = r'\{[\s\S]*?\}|\[[\s\S]*?\]'
    
    def translate_natural_lang(match):
        translator = GoogleTranslator(source=source_language, target=target_language)
        return translator.translate(match.group())
    
    game = re.sub(tags_comments_pattern, lambda x: translate_natural_lang(x), game)
    return game

def translate_comments(source_language, target_language, game):
    """
    Finds the comments in the game, translates them, and replaces them.
    """
    tags_comments_pattern = r'\{[\s\S]*?\}'
    
    def translate_natural_lang(match):
        translator = GoogleTranslator(source=source_language, target=target_language)
        return translator.translate(match.group())
    
    game = re.sub(tags_comments_pattern, lambda x: translate_natural_lang(x), game)
    return game