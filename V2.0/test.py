import webbrowser
import gen_alg
import tabu_alg

if __name__ == '__main__':
    
    gen_alg.genetics_algorithm()
    #tabu_alg.tabu_algorithm()
    
    # try: 
    #     gen_alg.genetics_algorithm()
    # except Exception as e:
    #     print(e)
    #     #print(gen_alg.genetics_algorithm.__doc__)
    #     #webbrowser.open('https://stackoverflow.com/search?q=' + str(e), new=2, autoraise=True)
