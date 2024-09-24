import pyautogui

class TypingSimulator:
    def type_phrase(self, phrase: str) -> None:
        """Type a phrase into the search bar."""
        pyautogui.press('/')
        pyautogui.press('backspace')
        pyautogui.typewrite(phrase)
        pyautogui.press('enter')