import sys
from ... import ND2MultiDim

def main():
    if len(sys.argv) != 2:
        raise RuntimeError("Exactly one argument, the nd2 file!")
    nd2 = ND2MultiDim(sys.argv[1])

    for point in nd2.multipoints:
        print("%.3f\t%.3f\t%.3f" % (point['x'], point['y'], point['z'],))

if __name__ == '__main__':
	main()

