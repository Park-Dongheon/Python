class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')
        
def palindrome(word):
    try:
        if word != word[::-1]:
            raise NotPalindromeError
        print(word)
    except Exception as e:
        raise

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
