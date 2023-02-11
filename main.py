import os
import time
import logging

# Logging
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s - %(asctime)s - %(filename)s - %(funcName) - %(message)s')
# logger = logging.getLogger(__name__)
# Get Time
time_year_month_day_hour_minute: int = int(time.strftime('%y%m%d%H%M', time.localtime(time.time())))
time_month_day_hour_minute: int = int(time.strftime('%m%d%H%M', time.localtime(time.time())))
time_week_hour_minute: int = int(time.strftime('%w%H%M', time.localtime(time.time())))
# variable time_week_hour_minute Week(0-6) is Sunday to Saturday
time_day_hour_minute: int = int(time.strftime('%d%H%M', time.localtime(time.time())))

logging.info("variable "+"time_year_month_day_hour_minute"+" value is "+str(time_year_month_day_hour_minute))

# plan_start_list = []
# plan_time_list = []
#
# i = 0
# while 1:
#     input_str = input()
#     if input_str == 'exit':
#         break
#     plan_start_list.append(input_str)
#     if not os.path.exists(plan_start_list[i]):
#         print("Path not found")
#         plan_start_list.remove(input_str)
#     else:
#         i += 1
#
# for a in range(0, len(plan_start_list)):
#     os.system('"'+plan_start_list[a]+'"')
#     # out_str = out.read()
#     # print(out_str)
