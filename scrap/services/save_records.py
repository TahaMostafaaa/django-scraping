
from scrap.models import Record,Country,Sector
import logging

logger = logging.getLogger(__name__)

class RecordsRepo:


    def save_record(self,record):

        date = record.get("date")
        title = record.get("title")
        signed_amount = record.get("signed_amount")

        sectors = record.get('sectors').split(",")
        # sectors_objs = set()

        country = Country.objects.get_or_create(name=record.get('country'))[0]


        record_obj = Record.objects.create(
            signature_date=date,
            country=country,
            signed_amount=signed_amount,
            title=title,
            # sectors=sectors_objs
        )
        for sector in sectors:
            record_obj.sectors.add(Sector.objects.get_or_create(name=sector)[0])

        record_obj.save()


