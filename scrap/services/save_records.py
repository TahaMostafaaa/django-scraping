
from models import Record,Country,Sector



class RecordsRepo:


    def save_record(self,record):

        date = record.get("date")
        title = record.get("title")
        signed_amount = record.get("signed_amount")

        sectors = record.get('sectors').split(",")
        sectors_objs = []

        for sector in sectors:
            sectors_objs.append(Sector.objects.get_or_create(name=sector.strip())[0])

        country = Country.objects.get_or_create(name=record.get('country').strip())[0]

        record_obj = Record.objects.create(
            signature_date=date,
            country=country,
            signed_amount_with_currency=signed_amount,
            title=title,
            sectors=sectors_objs
        )

        record_obj.save()


