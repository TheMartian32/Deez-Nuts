def nutter_butter(text: str):
    return print(f"\n{text} deez nuts.")


def ask_for(prompt, error_msg=None, _type=None):
    """ While the desired prompt is not given, it repeats the prompt. """
    while True:
        inp = input(prompt).strip()
        if not inp:
            if error_msg:
                print(error_msg)
            continue

        if _type:
            try:
                inp = _type(inp)
            except ValueError:
                if error_msg:
                    print(error_msg)
                continue

        return inp


num_times = ask_for("\nHow many things you wanna deez nuts?: ",
                    "can't do that sisski", int)
for _ in range(num_times):
    user_text = ask_for("\nAyo what text you wanna deez nuts?: ",
                        "can't do that broski", str)
    nutter_butter(user_text)
