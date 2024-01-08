import unittest
from translator.pgn_translator import translate_tags_comments


valid_tags_comments_case = [
    {
        "inputs": {"source_language": "en", "target_language": "es", 
        "game": "[Date '1992.11.04'] 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 {This opening is called the Ruy Lopez.}"},
        
        "expected_output": "[Fecha '1992.11.04'] 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 {Esta apertura se llama Ruy López.}"
    },
    {
        "inputs": {"source_language": "en", "target_language": "es", 
        "game": "[Date '1992.11.04'] 1. e4 e5 2. Nf3 Nc6 3. Rb5 a6 {This opening is called the Ruy Lopez.} Date '1992.11.04' This opening is called the Ruy Lopez."},
        
        "expected_output": "[Fecha '1992.11.04'] 1. e4 e5 2. Nf3 Nc6 3. Rb5 a6 {Esta apertura se llama Ruy López.} Date '1992.11.04' This opening is called the Ruy Lopez."
    },
]


class TestTranslateTagsComments(unittest.TestCase):

  def test_translate_tags_comments(self):
        for test_inputs in valid_tags_comments_case:
            inputs = test_inputs["inputs"]
            input_source_lang = inputs["source_language"]
            input_target_lang = inputs["target_language"]
            input_game = inputs["game"]
            expected_output = test_inputs["expected_output"]
            actual_output = translate_tags_comments(input_source_lang, input_target_lang, input_game)
            self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
