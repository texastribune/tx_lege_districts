# Download and reproject the 2012 plans
wget --no-clobber ftp://ftpgis1.tlc.state.tx.us/DistrictViewer/Congress/PLANC235.zip
wget --no-clobber ftp://ftpgis1.tlc.state.tx.us/DistrictViewer/House/PLANH309.zip
wget --no-clobber ftp://ftpgis1.tlc.state.tx.us/DistrictViewer/Senate/PLANS172.zip
wget --no-clobber ftp://ftpgis1.tlc.state.tx.us/DistrictViewer/SBOE/PLANE120.zip
mkdir -p reprojected
ls -tr *.zip | xargs -I {} unzip -n {}
ls -tr PLAN*/*.shp | xargs -I {} ogr2ogr reprojected/ {} -t_srs "EPSG:4326"
