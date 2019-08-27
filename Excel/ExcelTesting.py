from openpyxl import Workbook
import openpyxl

class WorksheetReader:
    def __init__(self, worksheet=None, workbook=None, worksheet_name=None, fieldnames = None):
        if worksheet != None:
            self._worksheet = worksheet
        elif workbook != None and worksheet_name != None:
            worksheet = None
            for sheet in workbook.worksheets:
                if sheet.title == worksheet_name:
                    worksheet = sheet
                    break
            if worksheet == None:
                raise Exception(f'No worksheet named "{worksheet_name}" in workbook')
            self._worksheet = worksheet
        self._fieldnames = fieldnames
        self._row_num = 1

    @property
    def FieldNames(self):
        return self._fieldnames

    @FieldNames.setter
    def FieldNames(self, value):
        self._fieldnames = value

    def __iter__(self):
        return self

    def __next__(self):
        rowdata = dict()
        col_num = 1
        for field in self._fieldnames:
            rowdata[field] = self._worksheet.cell(row=self._row_num, column=col_num).value
            col_num += 1
        if all(val[1] == None for val in rowdata.items()):
            raise StopIteration
        self._row_num += 1
        return rowdata


if __name__ == '__main__':

    wb = openpyxl.load_workbook('complaints.xlsx')
    fieldNames = ['peid', "AnalysisId", "Priority", "Group", "Status", "Contry", "AgeEntered", "Age", "NotifiedDate",
              "Created", "ProductDescription", "Description", "RFR", "DataReceived"]

    reader = WorksheetReader(workbook=wb, worksheet_name='WIP CDR (Cleveland)', fieldnames=fieldNames)
    fields = [x for x in reader]
    print(fields)

