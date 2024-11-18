import re

class PlutoLexicalAnalyzer:
    """
    A lexical analyzer for the Pluto programming language.
    """
    def __init__(self):
        # Define the token specifications
        self.token_specifications = [
            ('LANG', r'Lang\.'),  # Language declaration
            ('NUM', r'Num'),  # Integer type
            ('DECI', r'Deci'),  # Float type
            ('ALPHA', r'Alpha'),  # Character type
            ('FLAG', r'Flag'),  # Boolean type
            ('IS', r'Is'),  # If condition
            ('ES', r'Es'),  # Else condition
            ('TAB', r'Tab'),  # For loop
            ('JAB', r'Jab'),  # While loop
            ('GT', r'>'),  # Greater than
            ('LT', r'<'),  # Less than
            ('GE', r'>='),  # Greater than or equal to
            ('LE', r'<='),  # Less than or equal to
            ('EQ', r'=='),  # Equality operator
            ('NE', r'!='),  # Not equal operator
            ('PLUS', r'\+'),  # Addition operator
            ('MINUS', r'-'),  # Subtraction operator
            ('MULT', r'\*'),  # Multiplication operator
            ('DIV', r'/'),  # Division operator
            ('LBRACE', r'\{'),  # Left brace
            ('RBRACE', r'\}'),  # Right brace
            ('CHAR', r"'[a-zA-Z0-9]'"),  # Single character in single quotes
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers
            ('NUMBER', r'\d+(\.\d+)?'),  # Integer or float numbers
            ('ASSIGN', r'='),  # Assignment operator
            ('END', r';'),  # Statement terminator
            ('SKIP', r'[ \t]+'),  # Skip spaces and tabs
            ('NEWLINE', r'\n'),  # Line endings
            ('MISMATCH', r'.'),  # Any other character
        ]
        self.token_regex = self._compile_regex()

    def _compile_regex(self):
        """
        Compiles the token regex from the token specifications.
        """
        return re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specifications))

    def tokenize(self, code):
        """
        Tokenizes the input Pluto code and returns a list of tokens.
        """
        line_no = 1
        tokens = []
        for match in self.token_regex.finditer(code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'NEWLINE':
                line_no += 1
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected character {value!r} at line {line_no}')
            else:
                tokens.append((kind, value, line_no))
        return tokens

# Example Usage
if __name__ == "__main__":
    # Example Pluto code
    pluto = """
    Lang. Pluto
    Num x = 10;
    Deci y = 20.5;
    Num result = x + y * 2;
    Is result > 30 {
        Alpha z = 'A';
    } Es {
        Flag flag = True;
    }
    """

    # Create an instance of the lexical analyzer
    analyzer = PlutoLexicalAnalyzer()

    try:
        # Tokenize the code
        tokens = analyzer.tokenize(pluto)
        for token in tokens:
            print(token)
    except SyntaxError as e:
        print(e)
