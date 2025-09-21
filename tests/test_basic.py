import numpy as np
import las


# Do not remove the trailing whitespace in `case1_other`.
case1_other = """\
     Note: The logging tools became stuck at 625 metres causing the data 
     between 625 metres and 615 metres to be invalid.
"""
case1_data2d = np.array([
    [1670.000, 123.25, 2550.0, 0.50, 123.750, 123.500, 110.250, 105.5],
    [1669.875, 123.50, 2551.0, 0.75, 119.750, 120.500, 111.250, 105.5],
    [1669.750, 126.50, 2552.0, 0.50, 120.750, 123.500, -999.25, -999.25],
])

dupnames_data2d = np.array([
    [1670.000, 123.500, 2550.000, 0.500, 123.50, 120.50, 0.750, 0.500],
    [1669.875, 124.000, 2551.000, 0.750, 124.50, 121.50, 1.000, 0.125],
    [1669.750, 124.250, 2552.000, 0.125, 125.50, 122.50, 0.250, 0.375],
])


class LogCheck:

    def check_item(self, item, units, data, value, descr):
        assert item.units == units
        assert item.data == data
        assert item.value == value
        assert item.descr == descr


class TestCase1(LogCheck):

    def test_case1(self):
        log = las.LASReader('las_files/case1.las')
        self.check_case1_log(log, null_subs=None)

    def test_case1_null_subs_nan(self):
        log = las.LASReader('las_files/case1.las', null_subs=np.nan)
        self.check_case1_log(log, null_subs=np.nan)

    def test_case1b(self):
        log = las.LASReader('las_files/case1b.las')
        self.check_case1_log(log, null_subs=None)

    def check_case1_log(self, log, null_subs=None):
        assert log.wrap == False
        assert log.vers == '2.0'
        assert log.start == 1670.0
        assert log.start_units == 'M'
        assert log.stop == 1669.75
        assert log.stop_units == 'M'
        assert log.step == -0.125
        assert log.step_units == 'M'
        assert log.null == -999.25
        np.testing.assert_equal(log.null_subs, null_subs)

        self.check_item(log.version.VERS,
                        units='', data='2.0', value=2.0,
                        descr='CWLS LOG ASCII STANDARD -VERSION 2.0')
        self.check_item(log.version.WRAP,
                        units='', data='NO', value='NO',
                        descr='ONE LINE PER DEPTH STEP')

        assert log.other == case1_other

        if null_subs is not None:
            null_locs = case1_data2d == -999.25
            case1_data2d[null_locs] = np.nan

        np.testing.assert_array_equal(log.data2d, case1_data2d)
        flds = ['DEPT', 'DT', 'RHOB', 'NPHI', 'SFLU', 'SFLA', 'ILM', 'ILD']
        for k, field in enumerate(flds):
            np.testing.assert_array_equal(log.data[field],
                                          case1_data2d[:, k])

        if null_subs is not None:
            case1_data2d[null_locs] = -999.25

        self.check_item(log.well.STRT,
                        units='M', data='1670.0000', value=1670.0,
                        descr='START DEPTH')
        self.check_item(log.well.STOP,
                        units='M', data='1669.7500', value=1669.75,
                        descr='STOP DEPTH')
        self.check_item(log.well.STEP,
                        units='M', data='-0.1250', value=-0.125,
                        descr='STEP')
        self.check_item(log.well.NULL,
                        units='', data='-999.25', value=-999.25,
                        descr='NULL VALUE')
        self.check_item(log.well.COMP,
                        units='',
                        data='ANY OIL COMPANY INC.',
                        value='ANY OIL COMPANY INC.',
                        descr='COMPANY')
        self.check_item(log.well.WELL,
                        units='',
                        data='ANY ET AL 12-34-12-34',
                        value='ANY ET AL 12-34-12-34',
                        descr='WELL')
        self.check_item(log.well.FLD,
                        units='',
                        data='WILDCAT', value='WILDCAT',
                        descr='FIELD')
        self.check_item(log.well.LOC,
                        units='',
                        data='12-34-12-34W5M', value='12-34-12-34W5M',
                        descr='LOCATION')
        self.check_item(log.well.PROV,
                        units='',
                        data='ALBERTA', value='ALBERTA',
                        descr='PROVINCE')
        self.check_item(log.well.SRVC,
                        units='',
                        data='ANY LOGGING COMPANY INC.',
                        value='ANY LOGGING COMPANY INC.',
                        descr='SERVICE COMPANY')
        self.check_item(log.well.DATE,
                        units='',
                        data='13-DEC-86', value='13-DEC-86',
                        descr='LOG DATE')
        self.check_item(log.well.UWI,
                        units='',
                        data='100123401234W500',
                        value='100123401234W500',
                        descr='UNIQUE WELL ID')

        self.check_item(log.curves.DEPT,
                        units='M',
                        data='', value='',
                        descr='1  DEPTH')
        self.check_item(log.curves.DT,
                        units='US/M',
                        data='60 520 32 00', value='60 520 32 00',
                        descr='2  SONIC TRANSIT TIME')
        self.check_item(log.curves.RHOB,
                        units='K/M3',
                        data='45 350 01 00', value='45 350 01 00',
                        descr='3  BULK DENSITY')
        self.check_item(log.curves.NPHI,
                        units='V/V',
                        data='42 890 00 00', value='42 890 00 00',
                        descr='4  NEUTRON POROSITY')
        self.check_item(log.curves.SFLU,
                        units='OHMM',
                        data='07 220 04 00', value='07 220 04 00',
                        descr='5  SHALLOW RESISTIVITY')
        self.check_item(log.curves.SFLA,
                        units='OHMM',
                        data='07 222 01 00', value='07 222 01 00',
                        descr='6  SHALLOW RESISTIVITY')
        self.check_item(log.curves.ILM,
                        units='OHMM',
                        data='07 120 44 00', value='07 120 44 00',
                        descr='7  MEDIUM RESISTIVITY')
        self.check_item(log.curves.ILD,
                        units='OHMM',
                        data='07 120 46 00', value='07 120 46 00',
                        descr='8  DEEP RESISTIVITY')

        self.check_item(log.parameters.MUD,
                        units='',
                        data='GEL CHEM', value='GEL CHEM',
                        descr='MUD TYPE')
        self.check_item(log.parameters.BHT,
                        units='DEGC',
                        data='35.5000', value=35.5,
                        descr='BOTTOM HOLE TEMPERATURE')
        self.check_item(log.parameters.BS,
                        units='MM',
                        data='200.0000', value=200.0,
                        descr='BIT SIZE')
        self.check_item(log.parameters.FD,
                        units='K/M3',
                        data='1000.0000', value=1000.0,
                        descr='FLUID DENSITY')
        self.check_item(log.parameters.MATR,
                        units='',
                        data='SAND:COARSE', value='SAND:COARSE',
                        descr='NEUTRON MATRIX')
        self.check_item(log.parameters.MDEN,
                        units='',
                        data='2710.0000', value=2710.0,
                        descr='LOGGING MATRIX DENSITY')
        self.check_item(log.parameters.RMF,
                        units='OHMM',
                        data='0.2160', value=0.216,
                        descr='MUD FILTRATE RESISTIVITY')
        self.check_item(log.parameters.DFD,
                        units='K/M3',
                        data='1525.0000', value=1525.0,
                        descr='DRILL FLUID DENSITY')


class TestDupNames(LogCheck):

    def test_dupnames(self):
        log = las.LASReader('las_files/dupnames.las')

        self.check_item(log.curves.DEPT,
                        units='M',
                        data='', value='',
                        descr='1  DEPTH')
        self.check_item(log.curves.DT,
                        units='US/M',
                        data='60 520 32 00', value='60 520 32 00',
                        descr='2  SONIC TRANSIT TIME')
        self.check_item(log.curves.RHOB,
                        units='K/M3',
                        data='45 350 01 00', value='45 350 01 00',
                        descr='3  BULK DENSITY')
        self.check_item(log.curves.NPHI,
                        units='V/V',
                        data='42 890 00 00', value='42 890 00 00',
                        descr='4  NEUTRON POROSITY')
        self.check_item(log.curves.SFL,
                        units='OHMM',
                        data='07 220 04 00', value='07 220 04 00',
                        descr='5  SHALLOW RESISTIVITY')
        self.check_item(log.curves.SFL1,
                        units='OHMM',
                        data='07 222 01 00', value='07 222 01 00',
                        descr='6  DUP NAME')
        self.check_item(log.curves.NPHI1,
                        units='V/V',
                        data='42 890 00 00', value='42 890 00 00',
                        descr='7  DUP NAME')
        self.check_item(log.curves.NPHI2,
                        units='V/V',
                        data='42 890 00 00', value='42 890 00 00',
                        descr='8  DUP NAME')

        self.check_item(log.parameters.MUD,
                        units='',
                        data='GEL CHEM', value='GEL CHEM',
                        descr='MUD TYPE')
        self.check_item(log.parameters.MUD1,
                        units='',
                        data='MUCK', value='MUCK',
                        descr='MORE MUD TYPE')

        np.testing.assert_array_equal(log.data2d, dupnames_data2d)
