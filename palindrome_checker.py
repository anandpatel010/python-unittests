import re

class PalindromeChecker:
    def is_palindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        # Compare the cleaned string with its reverse
        return cleaned == cleaned[::-1]
