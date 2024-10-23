from . import Range
from .Utility import to_unicode

class AutoFilter(object):
    __slots__ = ("start_column", "end_column")

    def __init__(self, start_column, end_column):
        self.start_column = start_column
        self.end_column = end_column

    def __bool__(self):
        return self.start_column is not None and self.end_column is not None

    def __nonzero__(self):
        return self.__bool__()

    def __eq__(self, other):
        return (self.start_column == other.start_column and
                self.end_column == other.end_column)

    def get_xml(self, num_rows):
        ref = f"{Range.Range.coordinate_to_string((1, self.start_column))}:{Range.Range.coordinate_to_string((num_rows, self.end_column))}"
        return to_unicode(f'<autoFilter ref="{ref}"/>')
