#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import calendar, json, sys, csv

with open('config.json') as f:
	config = json.load(f)

previous_month = date.today().month - 1 # minus one as we are about to run it for previous month
if previous_month == 0:
	previous_month = 12 # we assume that this is the new year and we want generated file for december (12)
	current_year = date.today().year - 1 # so its december so it's already previous year
else:
	current_year = date.today().year # so it's not previous year so we stick with current

'''
	WHAT ABOUT HOLIDAYS? <-- need to download list of holidays and when they occur, create list of that anc cross check
'''

def get_working_days(month): #return number of working days in month and return table with dates
	dates = []
	_month = calendar.monthcalendar(current_year, month)
	for week in _month:
		if week[0] != 0:
			dates.append(week[0])
		if week[1] != 0:
			dates.append(week[1])
		if week[2] != 0:
			dates.append(week[2])
		if week[3] != 0:
			dates.append(week[3])
		if week[4] != 0:
			dates.append(week[4])
	return dates

def write_km(month, dates):
	months = ['Styczeń', 'Luty', 'Marzec', 'Kwiecien', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpien', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
	with open('kilometrowka-0'+str(month)+'-'+str(current_year)+'.csv', 'wb') as f:
		writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Ewidencja przebiegu pojazdu'])
		writer.writerow(['Imię i nazwisko osoby używającej pojazd (podatnika)', config['name']])
		writer.writerow(['Adres zamieszkania osoby uzywającej pojazd (podatnika)', config['address']])
		writer.writerow(['Za miesiąc:', months[month-1]])
		writer.writerow(['Numer rejestracyjny pojazdu:', config['registration_plate']])
		writer.writerow(['Pojemność silnika:', config['engine_capacity']])
		writer.writerow(['LP.', 'Data wyjazdu', 'Opis trasy (skąd--dokąd)', 'Cel wyjazdu', 'Liczba faktycznie przejechanych km', 'Stawka za 1km', 'Wartość', 'Podpis podatnika', 'Uwagi'])
		iterator = 0
		for day in dates:
			iterator += 1
			writer.writerow([iterator, str(day)+'.'+str(month)+'.'+str(current_year), config['from_to'],'Dojazd do klienta', config['km'], config['1km_price'], float(config['km']) * float(config['1km_price']), '', ''])

if __name__ == "__main__":

	dates = get_working_days(previous_month)
	write_km(previous_month, dates)