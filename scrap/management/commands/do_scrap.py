from django.core.management.base import BaseCommand
from scrap.services.scrap_records import ScrapRecords
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("== Start handle command ==")
        records = ScrapRecords().get_records()
        print("== Records ==")
        print(records)
        # return records
