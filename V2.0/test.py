import webbrowser
import gen_alg


if __name__ == '__main__':
    
    gen_alg.genetics_algorithm()  # type: ignore
    
    # try: 
    #     gen_alg.genetics_algorithm()
    # except Exception as e:
    #     print(e)
    #     #webbrowser.open('https://stackoverflow.com/search?q=' + str(e), new=2, autoraise=True)
