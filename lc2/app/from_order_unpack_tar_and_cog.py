from os import walk
from espaLib.order import Order
from espaLib.order import TarScene


def unpack_the_order(order):
    """ untars and maybe creates cogs from an order directory (espa) """
    testdir = mypath + '/' + order

    o = Order(order)
    print("OWNER:",o.owner)
    print("Order Date:",o.order_date)

    print(testdir)
    (dirs, files) = get_files_from_dir(testdir)

    #print(dirs)

    for tarball in files:
        print(tarball)
        ts = TarScene(testdir, tarball)
        print(ts.sensor, ts.path, ts.row, ts.year)
    
        ts.untar(tarball)
        print(ts.target_dir)



def get_files_from_dir(dir):
    f = []
    for (dirpath, dirnames, filenames) in walk(dir):
        f.extend(filenames)
        break
    return (dirnames, filenames)


mypath = '/mnt/alex1129'
(dirs, files) = get_files_from_dir(mypath)


for order in dirs:
    print(order)
    unpack_the_order(order)
