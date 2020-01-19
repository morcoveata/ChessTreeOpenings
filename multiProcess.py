import os
import multiprocessing
# from multiprocessing import Pool
#
# processes = ('ChessClient.py')
# other = ('chessTreeOpening.py',)
#
#
# def run_process(process):
# 	os.system('python {}'.format(process))
#
#
# pool = Pool(processes=2)
# pool.map(run_process, processes)
# pool.map(run_process, other)


##################
# os.system("python2 chessTreeOpening.py &")
# os.system("python2 ChessClient.py &")




def worker(file):
    # your subprocess code


if __name__ == '__main__':
    files = ["path/to/file1.py","path/to/file2.py","path/to/file3.py"]
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
