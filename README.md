# Field Boundaries

This repository contains sample code to generate Areas of Interest (AOI) from Green Leaf Area Index (GLAI) rasters generated using the [LAI4SR](https://github.com/lukasValentin/lai4sr) project used in the [master thesis](https://github.com/neffjulian/remote_sensing) of @neffjulian.

It uses the official field parcel boundaries provided by [GeoDienste.ch](https://www.geodienste.ch/services/lwb_nutzungsflaechen), preposssed in the [LAI4SR](https://github.com/lukasValentin/lai4sr) project containing the median GLAI per field parcel geometry (see image below).

Based on the median GLAI value per parcel, parcel pairs are selected that show a large gradient in median GLAI. In detail, for each parcel
1. a spatial buffer of 10 m is generated
2. its neighboring parcels are identified by selecting all parcels that intersect the buffered parcel geometry
