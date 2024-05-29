import datetime
from datetime import datetime  
import pytz  

aware_us_central = datetime.now(pytz.timezone('US/Central'))  
print('US Central DateTime', aware_us_central) 