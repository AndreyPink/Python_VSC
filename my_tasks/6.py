# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

# from datetime import datetime
# time_now = datetime.now()
# print(f'{time_now.second//86400}:{(time_now.second%86400)//3600}:{((time_now.second%86400)%3600)//60}:{((time_now.second%86400)%3600)%60}')

seconds = 90061
print(f'{seconds//86400}:{(seconds%86400)//3600}:{((seconds%86400)%3600)//60}:{((seconds%86400)%3600)%60}')

