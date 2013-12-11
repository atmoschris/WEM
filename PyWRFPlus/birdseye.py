from figure import Figure
import pdb
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class BirdsEye(Figure):
    def __init__(self,config,wrfout,):
        self.C = config
        self.W = wrfout
        self.fig = plt.figure()
        self.time_idx = self.W.get_plot_time_idx(self.C.plottime)
    
    def plot2D(self):
        pass

    def basemap_setup(self):
        nc = self.W.nc   # For brevity
        cen_lat = float(nc.CEN_LAT)
        cen_lon = float(nc.CEN_LON)
        truelat1 = float(nc.TRUELAT1)
        truelat2 = float(nc.TRUELAT2)

        x_dim = len(nc.dimensions['west_east'])
        y_dim = len(nc.dimensions['south_north'])
        dx = float(nc.DX)
        dy = float(nc.DY)
        width_m = dx*(x_dim-1)
        height_m = dy*(y_dim-1)

        m = Basemap(
            projection='lcc',width=width_m,height=height_m,
            lon_0=cen_lon,lat_0=cen_lat,lat_1=truelat1,
            lat_2=truelat2,resolution='i',area_thresh=500
            )
        m.drawcoastlines()
        m.drawstates()
        m.drawcountries()

        # Draw meridians etc with wrff.lat/lon spacing
        # Default should be a tenth of width of plot, rounded to sig fig

        xlong = nc.variables['XLONG'][0]
        xlat = nc.variables['XLAT'][0]
        #pdb.set_trace()
        x,y = m(xlong,xlat)
        return m, x, y

    
