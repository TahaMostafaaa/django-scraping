
import xlsxwriter
import logging
from scrap.models import Record
from django.core.serializers import serialize
from collections import defaultdict
import locale

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
        
        # countries = defaultdict(float)
        # countries = set()
        # adding data

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
        # chartsheet.write_column('A1', list(countries))
        # chartsheet.write_column('Sectors', data[1])
        # chartsheet.write_column('Amount', data[2])
        chart1.add_series({'values': f'={worksheet_name}!$E$2:$E$25',
                            'categories': f'={worksheet_name}!$D$2:$D$25',
                           'name': 'Country & Amount'
                           })
        # chart1.add_series({'values': f'={worksheet_name}!$E$1:$E$25',
        #                    'name': 'Amount'
        #                    })
        # chart1.add_series({'values': f'={worksheet_name}!$B$1:$B$5'})
        # chart1.add_series({'values': f'={worksheet_name}!$C$1:$C$5'})

        # Configure a second series. Note use of alternative syntax to define ranges.
        # chart1.add_series({
        #     'name':       [worksheet_name, 0, 2],
        #     'categories': [worksheet_name, 1, 0, 6, 0],
        #     'values':     [worksheet_name, 1, 2, 6, 2],
        # })

        # # Add a chart title and some axis labels.
        # chart1.set_title({'name': 'Results of Countries loans'})
        # chart1.set_x_axis({'name': 'Loans number'})
        # chart1.set_y_axis({'name': 'Countries'})

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

      


        


