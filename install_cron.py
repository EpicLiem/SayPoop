from crontab import CronTab

user_cron = CronTab(user=True)
sys_cron = CronTab()

job = user_cron.new(command = 'open https://www.youtube.com/watch?v=dQw4w9WgXcQ && osascript -e "set Volume 10"')
job.minute.every(30)


job.enable()
if job.is_valid():
   user_cron.write()
