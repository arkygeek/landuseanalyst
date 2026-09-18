"""GeoTIFFs written by the pure-Python engine must be readable immediately."""

import os

import numpy as np
import pytest
from osgeo import gdal


def _writeReference(thePath: str) -> None:
    myDs = gdal.GetDriverByName("GTiff").Create(thePath, 20, 10, 1, gdal.GDT_Float32)
    myDs.SetGeoTransform((744000.0, 30.0, 0.0, 3612000.0, 0.0, -30.0))
    myDs.SetProjection('PROJCS["WGS 84 / UTM zone 36N",GEOGCS["WGS 84",DATUM["WGS_1984",'
                       'SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],'
                       'UNIT["degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],'
                       'PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",33],'
                       'PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],'
                       'PARAMETER["false_northing",0],UNIT["metre",1]]')
    myDs.GetRasterBand(1).WriteArray(np.zeros((10, 20), dtype=np.float32))
    myDs = None


@pytest.mark.usefixtures("qtApp")
def test_write_mask_coregistered_is_immediately_readable(tmp_path):
    from la.lib.lagrass import LaGrass

    myReference = str(tmp_path / "ref.tif")
    _writeReference(myReference)
    myMask = np.zeros((10, 20), dtype=np.uint8)
    myMask[2:5, 3:9] = 1

    myGrass = LaGrass.__new__(LaGrass)   # no DEM layer needed for the writer
    myOut = str(tmp_path / "mask.tif")
    LaGrass._writeMaskCoregistered(myGrass, myMask, myReference, myOut)

    myDs = gdal.Open(myOut)
    assert myDs is not None, "GeoTIFF was not finalised (dataset handle still held)"
    assert myDs.RasterXSize == 20 and myDs.RasterYSize == 10
    assert int(myDs.GetRasterBand(1).ReadAsArray().sum()) == 18
    assert myDs.GetGeoTransform()[0] == pytest.approx(744000.0)
    myDs = None
    assert os.path.getsize(myOut) > 0
