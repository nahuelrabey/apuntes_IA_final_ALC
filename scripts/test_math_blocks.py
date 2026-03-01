import unittest
from fix_math_blocks import fix_math_blocks

class TestMathBlocksFixer(unittest.TestCase):
    def test_basic_block(self):
        input_text = "lorem ipsum\n$$\nx=10\n$$\nlorem ipsum"
        expected = "lorem ipsum\n\n$$\nx=10\n$$\n\nlorem ipsum\n"
        self.assertEqual(fix_math_blocks(input_text), expected)

    def test_blockquote_block(self):
        input_text = "> lorem ipsum\n> $$\n> x=10\n> $$\n> lorem ipsum"
        expected = "> lorem ipsum\n>\n> $$\n> x=10\n> $$\n>\n> lorem ipsum\n"
        self.assertEqual(fix_math_blocks(input_text), expected)
        
    def test_inline_blockquote_block(self):
         input_text = "> **Objetivo:** Determinar minimizan el error: $$\n> EC = \sum (f(x) - y)^2 $$\n> con datos experimentales formales."
         expected = "> **Objetivo:** Determinar minimizan el error:\n>\n> $$\n> EC = \sum (f(x) - y)^2\n> $$\n>\n> con datos experimentales formales.\n"
         self.assertEqual(fix_math_blocks(input_text), expected)
         
    def test_inline_both_sides(self):
         input_text = "Texto $$ x = 2 $$ mas texto."
         expected = "Texto\n\n$$\nx = 2\n$$\n\nmas texto.\n"
         self.assertEqual(fix_math_blocks(input_text), expected)

if __name__ == '__main__':
    unittest.main()
