import unittest
from translator.pgn_translator import translate_pgn_move_token

invalid_test_cases = [
    {
        "inputs": {"source_language": "foo", "target_language": "es", "token": "e4"},
        "error": "Invalid source language: foo."
    },
    {
        "inputs": {"source_language": "en", "target_language": "foo", "token": "Qf3"},
        "error": "Invalid target language: foo."
    },
]


class TestInvalidLanguages(unittest.TestCase):

    def test_invalid_languages(self):
        for test_inputs in invalid_test_cases:
            inputs = test_inputs["inputs"]
            input_source_lang = inputs["source_language"]
            input_target_lang = inputs["target_language"]
            input_token = inputs["token"]
            with self.assertRaises(ValueError) as cm:
                translate_pgn_move_token(input_source_lang, input_target_lang, input_token)
            self.assertEqual(str(cm.exception), test_inputs["error"])

if __name__ == '__main__':
    unittest.main()
