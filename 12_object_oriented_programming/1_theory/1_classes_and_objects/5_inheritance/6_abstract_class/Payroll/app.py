from module.HourlyEmployee import HourlyEmployee
from module.FulltimeEmployee import FulltimeEmployee
from module.Payroll import Payroll

payroll = Payroll()

payroll.add(FulltimeEmployee('Jennifer', 'Lawrence', 600000))
payroll.add(FulltimeEmployee('Brie', 'Larson', 6000000))
payroll.add(HourlyEmployee('Emma', 'Stone', 200, 600))
payroll.add(HourlyEmployee('Anne', 'Hathaway', 150, 500))
payroll.add(HourlyEmployee('Angelina', 'Jolie', 100, 550))

payroll.display()