import webbrowser

import main

if __name__ == '__main__':
    try: 
        main.start()
    except Exception as e:
        webbrowser.open('https://stackoverflow.com/search?q=' + str(e), new=2, autoraise=True)
