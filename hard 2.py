
import calendar
day={1:'первое', 2:'второе', 3:'третье', 4:'четрвертое', 5:'пятое', 6:'шестое', 7:'седьмое', 8:'восьмое', 9:'девятое', 10:'десятое', 11:'одинадцатое', 12:'двенадцатое', 13:'тринадцатое', 14:'четырнадцатое', 15:'пятнадцатое'}
month={1:'января', 2:'февраля', 3:'марта', 4:'апреля', 5:'мая', 6:'июня', 7:'июля', 8:'августа', 9:'сентября', 10:'октября', 11:'ноября', 12:'декабря'}
date=input('Введите дату в формате dd.mm.yyyy: ')

if (len(date)==10):
	dayInt=(date[0:2])
	dayInt=int(dayInt.lstrip("0"))
	monthInt=(date[3:5])
	monthInt=int(monthInt.lstrip("0"))
	yearInt=(date[6:])
	yearInt=int(yearInt.lstrip("0"))



	if ((0<yearInt and yearInt<9999)) and (1<=monthInt and monthInt<=12) and ((calendar.monthrange(yearInt,monthInt))[1] >= dayInt):

		print(day[dayInt],' ',month[monthInt],' ',yearInt)

	else:
		print("Error")
else:
	print("Error")

input()
