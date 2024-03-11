from oyasassn.client import SkyPatrolClient
from astropy import units as u
import shutil


def download_asassn_lc(ra, dec, objname, radius=5*u.arcsec):
    print('Downloading ASASSN data')
    # outname = objname + '_asassn_lc.csv'
    rad_deg = radius.to(u.deg).value
    client = SkyPatrolClient()
    res = client.cone_search(ra, dec, rad_deg, download=True, threads=8)
    fouts = res.save('/tmp/', file_format='csv')
    for ind in range(1, len(fouts)):
        lcname = fouts[ind]
        outname = objname + '_{}_asassn_lc.csv'.format(ind-1)
        print('moving', lcname, 'to', outname)
        shutil.move(lcname, outname)


def download_asassn_lcs(ras, decs, objnames, radius=5*u.arcsec):
    print('Downloading ASASSN data')
    rad_deg = radius.to(u.deg).value
    client = SkyPatrolClient()
    for ra, dec, objname in zip(ras, decs, objnames):
        res = client.cone_search(ra, dec, rad_deg, download=True, threads=8)
        fouts = res.save('/tmp/', file_format='csv')
        for ind in range(1, len(fouts)):
            lcname = fouts[ind]
            outname = objname + '_{}_asassn_lc.csv'.format(ind-1)
            print('moving', lcname, 'to', outname)
            shutil.move(lcname, outname)