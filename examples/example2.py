import io
import numpy as np
import matplotlib.pyplot as plt
import las
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

url = "http://www.kgs.ku.edu/software/DEWL/HELP/pc_read/Shamar-1.las"
f = io.StringIO(urlopen(url).read().decode('iso-8859-1'))
log = las.LASReader(f, null_subs=np.nan)

plt.figure(figsize=(9, 5))
plt.plot(log.data['DEPT'], log.data['GR'])
plt.xlabel(log.curves.DEPT.descr + " (%s)" % log.curves.DEPT.units)
plt.ylabel(log.curves.GR.descr + " (%s)" % log.curves.GR.units)
plt.title(log.well.WELL.data + ', ' + log.well.DATE.data)
plt.grid()
plt.show()
