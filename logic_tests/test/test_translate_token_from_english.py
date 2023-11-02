import unittest
from src.main import translate_pgn_move_token

valid_test_cases = [
    {
        "inputs": {"source_language": "en", "target_language": "es", "token": "e4"},
        "expected_output": "e4"
    },
    {
        "inputs": {"source_language": "en", "target_language": "es", "token": "Nf3"},
        "expected_output": "Cf3"
    },
    {
        "inputs": {"source_language": "en", "target_language": "es", "token": "Bf3"},
        "expected_output": "Af3"
    },
    {
        "inputs": {"source_language": "en", "target_language": "es", "token": "Rf3"},
        "expected_output": "Tf3"
    },
    {
        "inputs": {"source_language": "en", "target_language": "es", "token": "Qf3"},
        "expected_output": "Df3"
    },
    {
        "inputs": {"source_language": "en", "target_language": "es", "token": "Kf3"},
        "expected_output": "Rf3"
    },
]


class TestTranslateTokenFormEnglish(unittest.TestCase):

    def test_translate_token_from_english(self):
        for test_inputs in valid_test_cases:
            inputs = test_inputs["inputs"]
            input_source_lang = inputs["source_language"]
            input_target_lang = inputs["target_language"]
            input_token = inputs["token"]
            expected_output = test_inputs["expected_output"]
            actual_output = translate_pgn_move_token(input_source_lang, input_target_lang, input_token)
            self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
