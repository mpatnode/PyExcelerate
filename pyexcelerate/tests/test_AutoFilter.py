from ..AutoFilter import AutoFilter
from ..Worksheet import Worksheet
from ..Workbook import Workbook

def test_auto_filter_creation():
    af = AutoFilter(1, 5)
    assert af.start_column == 1
    assert af.end_column == 5

def test_auto_filter_xml():
    af = AutoFilter(1, 5)
    expected_xml = '<autoFilter ref="A1:E10"/>'
    assert af.get_xml(10) == expected_xml

def test_worksheet_auto_filter():
    wb = Workbook()
    ws = wb.new_sheet("Sheet1")
    ws.set_auto_filter(1, 5)
    assert ws._auto_filter is not None
    assert ws._auto_filter.start_column == 1
    assert ws._auto_filter.end_column == 5

def test_worksheet_auto_filter_default_end():
    wb = Workbook()
    ws = wb.new_sheet("Sheet1")
    ws.set_cell_value(1, 1, "Header1")
    ws.set_cell_value(1, 2, "Header2")
    ws.set_cell_value(1, 3, "Header3")
    ws.set_auto_filter(1)
    assert ws._auto_filter is not None
    assert ws._auto_filter.start_column == 1
    assert ws._auto_filter.end_column == 3
