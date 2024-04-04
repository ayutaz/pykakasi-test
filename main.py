import unittest
import pykakasi

class TestPyKakasi(unittest.TestCase):
    def setUp(self):
        self.kakasi = pykakasi.kakasi()

    def test_convert(self):
        test_cases = [
            {'text': '森 洋平', 'expected': [{'orig': '森', 'hira': 'もり', 'kana': 'モリ', 'hepburn': 'mori', 'kunrei': 'mori', 'passport': 'mori'}, {'orig': ' ', 'hira': ' ', 'kana': ' ', 'hepburn': ' ', 'kunrei': ' ', 'passport': ' '}, {'orig': '洋平', 'hira': 'ようへい', 'kana': 'ヨウヘイ', 'hepburn': 'yohei', 'kunrei': 'youhei', 'passport': 'yohei'}]},
            {'text': 'ありがとうございます', 'expected': [{'orig': 'ありがとう', 'hira': 'ありがとう', 'kana': 'アリガトウ', 'hepburn': 'arigatou', 'kunrei': 'arigatou', 'passport': 'arigatou'}, {'orig': 'ござい', 'hira': 'ござい', 'kana': 'ゴザイ', 'hepburn': 'gozai', 'kunrei': 'gozai', 'passport': 'gozai'}, {'orig': 'ます', 'hira': 'ます', 'kana': 'マス', 'hepburn': 'masu', 'kunrei': 'masu', 'passport': 'masu'}]},
            {'text': '今日は良い天気ですね', 'expected': [{'orig': '今日', 'hira': 'きょう', 'kana': 'キョウ', 'hepburn': 'kyou', 'kunrei': 'kyou', 'passport': 'kyou'}, {'orig': 'は', 'hira': 'は', 'kana': 'ハ', 'hepburn': 'ha', 'kunrei': 'ha', 'passport': 'ha'}, {'orig': '良い', 'hira': 'よい', 'kana': 'ヨイ', 'hepburn': 'yoi', 'kunrei': 'yoi', 'passport': 'yoi'}, {'orig': '天気', 'hira': 'てんき', 'kana': 'テンキ', 'hepburn': 'tenki', 'kunrei': 'tenki', 'passport': 'tenki'}, {'orig': 'です', 'hira': 'です', 'kana': 'デス', 'hepburn': 'desu', 'kunrei': 'desu', 'passport': 'desu'}, {'orig': 'ね', 'hira': 'ね', 'kana': 'ネ', 'hepburn': 'ne', 'kunrei': 'ne', 'passport': 'ne'}]}
        ]

        for case in test_cases:
            result = self.kakasi.convert(case['text'])
            self.assertEqual(result, case['expected'])

if __name__ == '__main__':
    unittest.main()