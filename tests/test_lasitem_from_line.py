import las


class TestLASItemFromLine:

    def assert_items_equal(self, item1, item2):
        assert item1.name == item2.name
        assert item1.units == item2.units
        assert item1.data == item2.data
        assert item1.value == item2.value
        assert item1.descr == item2.descr

    def test_values(self):
        expected = las.LASItem('FOO', units='BAR', data='100', descr='BAZ')
        cases = ["FOO.BAR 100:BAZ",
                 "  FOO.BAR 100:BAZ",
                 "FOO  .BAR 100:BAZ",
                 "FOO.BAR  100   :BAZ",
                 "FOO.BAR  100:   BAZ",
                 "FOO.BAR  100:BAZ   "]
        for line in cases:
            item = las.LASItem.from_line(line)
            self.assert_items_equal(item, expected)

    def test_no_data(self):
        expected = las.LASItem('FOO', units='BAR', data='', descr='BAZ')
        cases = ["FOO.BAR :BAZ",
                 "  FOO.BAR :BAZ",
                 "FOO  .BAR :BAZ",
                 "FOO.BAR    :BAZ",
                 "FOO.BAR :   BAZ",
                 "FOO.BAR :BAZ   "]
        for line in cases:
            item = las.LASItem.from_line(line)
            self.assert_items_equal(item, expected)

    def test_no_units(self):
        expected = las.LASItem('FOO', units='', data='100', descr='BAZ')
        cases = ["FOO. 100:BAZ",
                 "  FOO. 100:BAZ",
                 "FOO  .  100:BAZ",
                 "FOO. 100  :BAZ",
                 "FOO. 100:   BAZ",
                 "FOO. 100:BAZ   "]
        for line in cases:
            item = las.LASItem.from_line(line)
            self.assert_items_equal(item, expected)

    def test_colon_in_data(self):
        # According to the 2014 "clarification" document, there may be colons
        # in the data.  The *last* colon in the line separates the data from
        # the description.  Others are part of the data.

        expected = las.LASItem('FOO', units='BAR', data='ABC:123', descr='BAZ')
        cases = ["FOO.BAR  ABC:123:BAZ",
                 "FOO.BAR  ABC:123  :  BAZ",
                 "FOO .BAR ABC:123:  BAZ"]
        for line in cases:
            item = las.LASItem.from_line(line)
            self.assert_items_equal(item, expected)

        expected = las.LASItem('FOO', units='', data='ABC:123', descr='BAZ')
        cases = ["FOO.  ABC:123:BAZ",
                 "FOO.  ABC:123  :  BAZ",
                 "FOO. ABC:123:  BAZ",
                 "FOO  . ABC:123:  BAZ"]
        for line in cases:
            item = las.LASItem.from_line(line)
            self.assert_items_equal(item, expected)
