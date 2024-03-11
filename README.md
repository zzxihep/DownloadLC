# DownloadLC
Auto download light curves from several publicly available sky survey.

## Avilable surveys
- [x] [ASAS-SN](https://asas-sn.osu.edu/)
- [x] [ZTF](https://www.ztf.caltech.edu/)
- [x] [TESS](https://heasarc.gsfc.nasa.gov/docs/tess/)

## Dependencies
<!-- - [x] [astroquery](https://astroquery.readthedocs.io/en/latest/) -->
<!-- - [x] [pandas](https://pandas.pydata.org/) -->
<!-- - [x] [numpy](https://numpy.org/) -->
- [x] [astropy](https://www.astropy.org/)
- [x] [pyasassn](https://github.com/asas-sn/skypatrol)
- [x] [lightkurve](https://docs.lightkurve.org/)
- [x] [wget](https://pypi.org/project/wget/)

## Installation
```bash
pip install git+https://github.com/zzxihep/DownloadLC.git
```

or clone the repository and install it locally
```bash
git clone https://github.com/zzxihep/DownloadLC.git
cd DownloadLC
python setup.py install
```

## Usage

The package provides a command line tool `downloadlc` to download light curves from different surveys.

```bash

usage: downloadlc [-h] --survey {asassn,ztf,tess} --ra RA --dec DEC --radius RADIUS

downloadlc --survey asassn --ra 0.0 --dec 0.0 --radius 1.0

optional arguments:
  -h, --help            show this help message and exit
  --survey {asassn,ztf,tess}
                        Survey name
  --ra RA               Right ascension in degree
  --dec DEC             Declination in degree
  --radius RADIUS       Search radius in degree
```