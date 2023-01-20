from django.core.management.base import BaseCommand
from scrap.services.scrap_records import ScrapRecords
from scrap.services.save_records import RecordsRepo
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.warning("== Start handle command ==")
        records = ScrapRecords().get_records()
        logger.warning("== Start Saving records ==")
        for record in records:
            RecordsRepo().save_record(record)
        print(records)
        # return records
