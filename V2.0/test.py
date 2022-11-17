import webbrowser
import gen_alg
import tabu_alg

if __name__ == '__main__':
    
    gen_alg.genetics_algorithm()

    # try: 
    #     gen_alg.genetics_algorithm()
    #     tabu_alg.tabu_algorithm()
    
    # except Exception as e:
    #     print(e)
    #     #webbrowser.open('https://stackoverflow.com/search?q=' + str(e), new=2, autoraise=True)
