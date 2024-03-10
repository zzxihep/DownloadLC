import sys
import lightkurve as lk
from astropy.coordinates import SkyCoord
from . import tess_data
import argparse


def get_objname(ra, dec):
    coo = SkyCoord(ra=ra, dec=dec, unit=(u.deg, u.deg))
    return 'J' + coo.to_string(style='hmsdms', sep='', precision=1)


def main():
    parser = argparse.ArgumentParser(description='Download light curves')
    parser.add_argument('ra', type=float, help='RA of the target')
    parser.add_argument('dec', type=float, help='Dec of the target')
    parser.add_argument('--output', type=str, help='Output object name', default=None)
    parser.add_argument('--format', type=str, help='Output file format', default='csv', choices=['csv', 'fits'])
    parser.add_argument('--survey', type=list, help='Survey to download from', 
        default=['TESS', 'Kepler', 'K2', 'CoRoT', 'SPOC', 'EVEREST', 'K2SFF', 'K2SC', 'K2VARCAT', 'K2CTL', 'K2CFL', 'ZTF', 'ASAS-SN'])
    parser.add_argument('--max_retries', type=int, help='Max retries for downloading', default=5)
    args = parser.parse_args()
    ra = args.ra
    dec = args.dec
    objname = args.output
    if objname is None:
        objname = get_objname(ra, dec)
    outformat = args.format
    surveys = args.survey
    max_retries = args.max_retries
    print('Downloading data for RA:', ra, 'Dec:', dec)
    tess_data.download_lightkurve_lc(ra, dec, objname, outformat, max_retries)
    # lc = lk.search_lightcurve(ra, dec).download_all()


if __name__ == '__main__':
    main()