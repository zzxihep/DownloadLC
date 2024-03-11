import wget
from astropy import units as u


def download_ztf_lc(ra, dec, objname, outformat, max_retries, radius=5*u.arcsec):
    if outformat not in ['csv', 'tsv']:
        raise ValueError('Invalid output format')
    outname_g = objname + '_ztf_g_lc.' + outformat
    outname_r = objname + '_ztf_r_lc.' + outformat
    outname_i = objname + '_ztf_i_lc.' + outformat
    rad_deg = radius.to(u.deg).value

    # url_g = "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE+{:.6f}+{:.6f}+{}&BANDNAME=g&NOBS_MIN=5&BAD_CATFLAGS_MASK=32768&FORMAT=csv".format(ra, dec, rad_deg)

    url_g = "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE+{:.6f}+{:.6f}+{}&BANDNAME=g&NOBS_MIN=5&FORMAT=csv".format(ra, dec, rad_deg)

    url_r = "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE+{:.6f}+{:.6f}+{}&BANDNAME=r&NOBS_MIN=5&FORMAT=csv".format(ra, dec, rad_deg)

    url_i = "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE+{:.6f}+{:.6f}+{}&BANDNAME=i&NOBS_MIN=5&FORMAT=csv".format(ra, dec, rad_deg)

    wget.download(url_g, out=outname_g)
    wget.download(url_r, out=outname_r)
    wget.download(url_i, out=outname_i)

    return outname_g, outname_r, outname_i