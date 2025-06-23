from audio.speech import speak, listen
from decouple import config
from aim.conv import converse
from act.actions import (
    open_notepad, open_word, open_excel, open_ppt, open_calculator,
    open_website, open_cmd, open_camera, take_screenshot
)

BOT_NAME = config("VA_NAME")


status_callback = None
stop_requested = False

def run_assistant(callback=None):
    global stop_requested, status_callback
    stop_requested = False
    status_callback = callback

    def update(text):
        print(text)
        if status_callback:
            status_callback(text)

    update(f"I am your {BOT_NAME}. How may I help you?")
    speak(f"I am your {BOT_NAME}.How may I help you?")

    while not stop_requested:
        update("🎤 Listening...")
        query = listen()

        if query is None:
            continue

        update("🧠 Recognizing...")
        query = query.lower()
        intent = converse(query)

        if 'open' in query and 'notepad' in query:
            intent = 'ACTION_OPEN_NOTEPAD'
        elif 'open' in query and 'calculator' in query:
            intent = 'ACTION_OPEN_CALCULATOR'
        elif 'open' in query and 'word' in query:
            intent = 'ACTION_OPEN_WORD'
        elif 'open' in query and 'excel' in query:
            intent = 'ACTION_OPEN_EXCEL'
        elif 'open' in query and ('powerpoint' in query or 'ppt' in query):
            intent = 'ACTION_OPEN_PPT'
        elif 'open' in query and 'cmd' in query:
            intent = 'ACTION_OPEN_CMD'
        elif 'open' in query and 'camera' in query:
            intent = 'ACTION_OPEN_CAMERA'
        elif 'screenshot' in query or 'take screenshot' in query:
            intent = 'ACTION_TAKE_SCREENSHOT'
        elif 'open' in query and 'website' in query:
            intent = 'ACTION_OPEN_WEBSITE'
        elif any(word in query for word in ['exit', 'shutdown', 'stop', 'goodbye', 'quit']):
            intent = 'ACTION_EXIT'

        update(f"Query: {query}")
        update(f"Intent: {intent}")

        if not intent.startswith('ACTION_'):
            speak(intent)
            update(intent)
            continue

        try:
            action_msg = f"⚙️ {intent.replace('ACTION_', '').replace('_', ' ').title()}"
            update(action_msg)

            if intent == 'ACTION_OPEN_NOTEPAD':
                open_notepad()
            elif intent == 'ACTION_OPEN_WORD':
                open_word()
            elif intent == 'ACTION_OPEN_EXCEL':
                open_excel()
            elif intent == 'ACTION_OPEN_PPT':
                open_ppt()
            elif intent == 'ACTION_OPEN_CALCULATOR':
                open_calculator()
            elif intent == 'ACTION_OPEN_WEBSITE':
                open_website()
            elif intent == 'ACTION_OPEN_CMD':
                open_cmd()
            elif intent == 'ACTION_OPEN_CAMERA':
                open_camera()
            elif intent == 'ACTION_TAKE_SCREENSHOT':
                take_screenshot()
            elif intent == 'ACTION_EXIT':
                speak("Shutting down. Goodbye!")
                stop_requested = True

        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, something went wrong while trying to execute the command.")


if __name__ == '__main__':
    run_assistant()
