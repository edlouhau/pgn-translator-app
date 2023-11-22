import unittest
from translator.pgn_translator import translate_pgn_game

valid_game_case = [
    {
        "inputs": {"source_language": "en", "target_language": "es", 
        "game": "27. Qe3 Qg5 28. Qxg5 hxg5 29. b3 Ke6 30. a3 Kd6"},
        
        "expected_output": "27. De3 Dg5 28. Dxg5 hxg5 29. b3 Re6 30. a3 Rd6"
    },
    {
        "inputs": {"source_language": "en", "target_language": "es", 
        "game": "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 {This opening is called the Ruy Lopez.}"},
        
        "expected_output": "1. e4 e5 2. Cf3 Cc6 3. Ab5 a6 {This opening is called the Ruy Lopez.}"
    },
    {
        "inputs": {"source_language": "en", "target_language": "es", 
        "game": "1. e4 e5 2. Nf3 Nc6 3. Rb5 a6 {This opening is called the Ruy Lopez.} 1. e4 e5 2. Nf3 Nc6 3. Rb5 a6"},
        
        "expected_output": "1. e4 e5 2. Cf3 Cc6 3. Tb5 a6 {This opening is called the Ruy Lopez.} 1. e4 e5 2. Cf3 Cc6 3. Tb5 a6"
    },
]


class TestTranslateGameFromEnglish(unittest.TestCase):

 def test_translate_game_from_english(self):
        for test_inputs in valid_game_case:
            inputs = test_inputs["inputs"]
            input_source_lang = inputs["source_language"]
            input_target_lang = inputs["target_language"]
            input_game = inputs["game"]
            expected_output = test_inputs["expected_output"]
            actual_output = translate_pgn_game(input_source_lang, input_target_lang, input_game)
            self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
