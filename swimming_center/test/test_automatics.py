from datetime import datetime, timedelta

import sys
import os
# import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
from config import WorkingHours, TicketOptions
from database import TICKETS

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
from automatics import Automatic

if __name__ == "__main__":
    
    def dt_to_ts(dt: datetime) -> int:
        return int(dt.timestamp())
    
    a1 = Automatic(1001)
    print(a1)
    
    t = a1.sell(TicketOptions.SHORT_TERM, 50, False, dt_to_ts(datetime(2026, 7, 13, 6, 32, 45)), False)
    print(t)