import time
import multiprocessing 
import datetime

start =  time.time();
def calc_square(numbers):
    for n in numbers:
        print ('sqaure ' + str(n * n));
    
def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*3));



if __name__ == "__main__":
    arr = [2,3,8,9]

    p1 = multiprocessing.Process(target=calc_cube, args=(arr,))
    p2 = multiprocessing.Process(target=calc_square, args=(arr,))

    
    p1.start();
    p2.start();

    p1.join();
    p2.join();

    print("--- %s seconds ---" % (time.time() * 1000 * 60 - start))

    print ('done')


currentDT = datetime.datetime.now()

print (str(currentDT))


'''print(localtime)'''
