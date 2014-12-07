The `las` module implements a reader for a LAS (Log ASCII Standard) well log files (LAS 2.0).
For more information about this format, see the Canadian Well Logging Society web page
(http://www.cwls.org/las/).

Example
-------

The following file, "example1.las" is from "LAS Version 2.0: A Digital Standard for
Logs; Updated January 2014":

    ~VERSION INFORMATION
    VERS.                          2.0 :   CWLS LOG ASCII STANDARD -VERSION 2.0
    WRAP.                          NO  :   ONE LINE PER DEPTH STEP
    ~WELL INFORMATION 
    #MNEM.UNIT              DATA                       DESCRIPTION
    #----- -----            ----------               -------------------------
    STRT    .M              1670.0000                :START DEPTH
    STOP    .M              1669.7500                :STOP DEPTH
    STEP    .M              -0.1250                  :STEP 
    NULL    .               -999.25                  :NULL VALUE
    COMP    .       ANY OIL COMPANY INC.             :COMPANY
    WELL    .       ANY ET AL 12-34-12-34            :WELL
    FLD     .       WILDCAT                          :FIELD
    LOC     .       12-34-12-34W5M                   :LOCATION
    PROV    .       ALBERTA                          :PROVINCE 
    SRVC    .       ANY LOGGING COMPANY INC.         :SERVICE COMPANY
    DATE    .       13-DEC-86                        :LOG DATE
    UWI     .       100123401234W500                 :UNIQUE WELL ID
    ~CURVE INFORMATION
    #MNEM.UNIT              API CODES                   CURVE DESCRIPTION
    #------------------     ------------              -------------------------
     DEPT   .M                                       :  1  DEPTH
     DT     .US/M           60 520 32 00             :  2  SONIC TRANSIT TIME
     RHOB   .K/M3           45 350 01 00             :  3  BULK DENSITY
     NPHI   .V/V            42 890 00 00             :  4  NEUTRON POROSITY
     SFLU   .OHMM           07 220 04 00             :  5  SHALLOW RESISTIVITY
     SFLA   .OHMM           07 222 01 00             :  6  SHALLOW RESISTIVITY
     ILM    .OHMM           07 120 44 00             :  7  MEDIUM RESISTIVITY
     ILD    .OHMM           07 120 46 00             :  8  DEEP RESISTIVITY
    ~PARAMETER INFORMATION
    #MNEM.UNIT              VALUE             DESCRIPTION
    #--------------     ----------------      -----------------------------------------------
     MUD    .               GEL CHEM        :   MUD TYPE
     BHT    .DEGC           35.5000         :   BOTTOM HOLE TEMPERATURE
     BS     .MM             200.0000        :   BIT SIZE
     FD     .K/M3           1000.0000       :   FLUID DENSITY
     MATR   .               SAND            :   NEUTRON MATRIX
     MDEN   .               2710.0000       :   LOGGING MATRIX DENSITY
     RMF    .OHMM           0.2160          :   MUD FILTRATE RESISTIVITY
     DFD    .K/M3           1525.0000       :   DRILL FLUID DENSITY
    ~OTHER
         Note: The logging tools became stuck at 625 metres causing the data 
         between 625 metres and 615 metres to be invalid.
    ~A  DEPTH     DT    RHOB        NPHI   SFLU    SFLA      ILM      ILD
    1670.000   123.450 2550.000    0.450  123.450  123.450  110.200  105.600
    1669.875   123.450 2550.000    0.450  123.450  123.450  110.200  105.600
    1669.750   123.450 2550.000    0.450  123.450  123.450  110.200  105.600


Sample python session:

    >>> import las
    >>> rdr = las.LASReader('example1.las')
    >>> rdr.start
    1670.0
    >>> rdr.stop
    1669.75
    >>> rdr.step
    -0.125
    >>> rdr.null
    -999.25
    >>> rdr.well.COMP
    LASItem(name='COMP', units='', data='ANY OIL COMPANY INC.', descr='COMPANY')
    >>> rdr.well.COMP.value
    'ANY OIL COMPANY INC.'
    >>> rdr.well.FLD.value
    'WILDCAT'
    >>> print(rdr.other)
         Note: The logging tools became stuck at 625 metres causing the data 
         between 625 metres and 615 metres to be invalid.


The actual data is stored as a numpy structured array in `rdr.data`:

    >>> rdr.data
    array([(1670.0, 123.45, 2550.0, 0.45, 123.45, 123.45, 110.2, 105.6),
           (1669.875, 123.45, 2550.0, 0.45, 123.45, 123.45, 110.2, 105.6),
           (1669.75, 123.45, 2550.0, 0.45, 123.45, 123.45, 110.2, 105.6)], 
          dtype=[('DEPT', '<f8'), ('DT', '<f8'), ('RHOB', '<f8'), ('NPHI', '<f8'), ('SFLU', '<f8'), ('SFLA', '<f8'), ('ILM', '<f8'), ('ILD', '<f8')])
    >>> rdr.data['RHOB']
    array([ 2550.,  2550.,  2550.])
