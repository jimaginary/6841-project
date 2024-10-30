import numpy as np
import threading
import time

data = [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1]*100

def matmul():
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.matmul(A, B)

size = 512
def oscillator():
    for d in data:
        

        start = time.time()
        if d == 0:
            time.sleep(0.03)
        else:
            threads = []
            for i in range(6):
                thread = threading.Thread(target=matmul)
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
        end = time.time()

        time.sleep(max(0,0.1-(end-start)))

oscillator()





