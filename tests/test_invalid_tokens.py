import unittest
from translator.pgn_translator import translate_pgn_move_token

invalid_tokens = [
    {
        "inputs": {"source_language": "en", "target_language": "es", "token": "Xf3"},
        "error": "Invalid token: Xf3."
    },
]


class TestInvalidTokens(unittest.TestCase):

    def test_invalid_tokens(self):
        for test_inputs in invalid_tokens:
            inputs = test_inputs["inputs"]
            input_source_lang = inputs["source_language"]
            input_target_lang = inputs["target_language"]
            input_token = inputs["token"]
            with self.assertRaises(ValueError) as cm:
                translate_pgn_move_token(input_source_lang, input_target_lang, input_token)
            self.assertEqual(str(cm.exception), test_inputs["error"])
    
if __name__ == '__main__':
    unittest.main()
