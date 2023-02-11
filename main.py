'''
    Copyright (C) 2023  zhousheng

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import os
import time
import logging

# LICENSE
print("    <program>  Copyright (C) 2023  zhousheng"
      "    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'."
      "    This is free software, and you are welcome to redistribute it"
      "    under certain conditions; type `show c' for details.")
# Logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Get Time
time_year_month_day_hour_minute: int = int(time.strftime('%y%m%d%H%M', time.localtime(time.time())))
time_month_day_hour_minute: int = int(time.strftime('%m%d%H%M', time.localtime(time.time())))
time_week_hour_minute: int = int(time.strftime('%w%H%M', time.localtime(time.time())))
# variable time_week_hour_minute Week(0-6) is Sunday to Saturday
time_day_hour_minute: int = int(time.strftime('%d%H%M', time.localtime(time.time())))

# Variable Logging
logger.info("Variable "+"time_year_month_day_hour_minute"+" value is "+str(time_year_month_day_hour_minute))
logger.info("Variable "+"time_month_day_hour_minute"+" value is "+str(time_month_day_hour_minute))
logger.info("Variable "+"time_year_month_day_hour_minute"+" value is "+str(time_year_month_day_hour_minute))

plan_start_list = []
plan_time_list = []

i = 0
while 1:
    input_str = input()
    if input_str == 'exit':
        break
    plan_start_list.append(input_str)
    if not os.path.exists(plan_start_list[i]):
        print("Path not found")
        plan_start_list.remove(input_str)
    else:
        i += 1

for a in range(0, len(plan_start_list)):
    os.system('"'+plan_start_list[a]+'"')
    # out_str = out.read()
    # print(out_str)
