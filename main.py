import matplotlib.pyplot as plt

month_eff = [(-(1/5)*(x-5.5)**2+7)/2 for x in range(12)]
month_eff = [month/sum(month_eff) for month in month_eff]
months = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']

declared_power = int(input('Podaj moc paneli w watach: '))

year_power = declared_power
month_power = [year_power*month_eff[i] for i in range(12)]

hourly_power = [month/30.5/24*1000 for month in month_power]

plots, (monthly_plot, hourly_plot) = plt.subplots(2, 1)
monthly_plot.title.set_text('Produkcja miesięczna w skali roku')
monthly_plot.set_ylabel('kWh')
monthly_plot.set_xticks([i for i in range(12)], months)
monthly_plot.plot(month_power)
monthly_plot.grid()
hourly_plot.title.set_text('Produkcja na godzinę w skali roku')
hourly_plot.set_ylabel('W')
hourly_plot.set_xticks([i for i in range(12)], months)
hourly_plot.plot(hourly_power)
hourly_plot.grid()
plt.show()
