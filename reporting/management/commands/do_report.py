from django.core.management.base import BaseCommand
from reporting.services.report import Report
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.warning("== Start handle report command ==")
        Report().create_report()
