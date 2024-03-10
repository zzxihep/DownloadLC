import sys
import lightkurve as lk


def main():
    ra = float(sys.argv[1])
    dec = float(sys.argv[2])
    print('Downloading data for RA:', ra, 'Dec:', dec)
    # lc = lk.search_lightcurve(ra, dec).download_all()


if __name__ == '__main__':
    main()