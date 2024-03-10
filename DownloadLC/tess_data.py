import lightkurve as lk
from astropy.coordinates import SkyCoord
import astropy.units as u


def search_lc(coo, max_retries=5):
    for ind in range(1, max_retries+1):
        try:
            search_res = lk.search_lightcurve(coo, radius=5*u.arcsec)
            return search_res
        except Exception as e:
            print(f'Error: {e}')
            print(f'Retrying for {ind} time, for {coo}, max retries {max_retries}')
            continue
    return None


def download_lc(res, max_retries=5):
    for ind in range(1, max_retries+1):
        try:
            print(f'Downloading {res}')
            lc = res.download()
            return lc
        except Exception as e:
            print(f'Error: {e}')
            print(f'Retrying for {ind} time, for {res}, max retries {max_retries}')
            continue
    return None


def download_lightkurve_lc(ra, dec, objname, outformat, max_retries=5):
    coo = SkyCoord(ra=ra, dec=dec, unit=(u.deg, u.deg))
    results = search_lc(coo, max_retries)

    results = lk.search_lightcurve(coo, max_retries)

    if results is None:
        raise ValueError('No light curve found')

    print(results)

    for result in results:
        mission = result.mission[0]
        author = result.author.data[0]
        dist = result.distance.value[0]
        tmission = mission.replace(' ', '-')
        outname = f'{objname}_{tmission}_{author}_dist{dist}.{outformat}'
        lc = download_lc(result, max_retries)
        if lc is None:
            print(f'Error in downloading {result}')
            continue
        if outformat == 'fits':
            try:
                print(f'Writing {outname} to fits')
                lc.to_fits(outname, overwrite=True)
            except Exception as e:
                print(f'Error in writing {outname} to fits')
                print(f'Error: {e}')
                outname = outname.replace('.fits', '.csv')
                print(f'Writing {outname} to csv')
                lc.to_csv(outname, overwrite=True)
        else:
            print(f'Writing {outname} to csv')
            lc.to_csv(outname, overwrite=True)