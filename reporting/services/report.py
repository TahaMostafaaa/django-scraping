
import xlsxwriter
import logging
from scrap.models import Record

logger = logging.getLogger(__name__)

class Report:


    def generate_excel(self,workbook_name: str, worksheet_name: str, headrers_list: list, data):

        # create workbook
        workbook = xlsxwriter.Workbook(f'{workbook_name}.xlsx')

        # create worksheet
        worksheet = workbook.add_worksheet(worksheet_name)
        money_format = workbook.add_format({'num_format': '€#,##0'})

        # adding headers
        for idx,header in enumerate(headrers_list):
            worksheet.write(0,idx,str(header).capitalize())
        

        for idx1,entry in enumerate(data):
            for idx2, header in enumerate(headrers_list):
                if header == 'signed_amount':
                    worksheet.write_number(idx1+1, idx2,float(entry[header][1:].replace(',', '')) ,money_format)
                else:
                    worksheet.write(idx1+1,idx2,entry[header])
                # countries.add(entry.get('country'))
        
        chartsheet = workbook.add_chartsheet("Chart")
        workbook.add_format({'bold': 1})

        chart1 = workbook.add_chart({'type': 'column'})

        # Configure the first series.

        chart1.add_series({'values': f'={worksheet_name}!$E$2:$E$25',
                            'categories': f'={worksheet_name}!$D$2:$D$25',
                           'name': 'Country & Amount'
                           })


        # Set an Excel chart style.
        chart1.set_style(11)

        # Add the chart to the chartsheet.
        chartsheet.set_chart(chart1)

        # Display the chartsheet as the active sheet when the workbook is opened.
        chartsheet.activate()

        workbook.close() 
    


    def create_report(self):
        records = Record.objects.all()
        data_list = self.records_to_dictionary(records)
        
        self.generate_excel('DelphosIQ','Data',['#','date','title','country','signed_amount','sectors'],data_list)


    def records_to_dictionary(self,records):
        if not records:
            return None
        
        recordsList = []
        for idx,record in enumerate(records):
            dictionary = {}
            dictionary["#"] = idx+1
            dictionary["date"] = record.signature_date.strftime("%d %B %Y")
            dictionary["title"] = record.title
            dictionary["country"] = record.country.name
            dictionary["signed_amount"] = record.signed_amount
            sector_string = ''
            for sector in record.sectors.all():
                sector_string += f'{sector.name},'
            dictionary["sectors"] = sector_string
            recordsList.append(dictionary)

        return recordsList

      


        


