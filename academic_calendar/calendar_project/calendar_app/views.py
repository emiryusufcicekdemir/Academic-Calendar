from django.shortcuts import render
from calendar import HTMLCalendar
from datetime import date

def event_list_by_month(request, year=None, month=None):
    # Varsayılan yıl ve ay
    today = date.today()
    year = year or today.year
    month = month or today.month

    # Ay ve yıl sınırlarını kontrol et
    if not (1 <= month <= 12):
        month = today.month

    # Önceki ve sonraki ay/yıl hesaplama
    prev_month = month - 1 if month > 1 else 12
    prev_year = year - 1 if month == 1 else year
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year

    # Türkçe ay ve gün isimleri
    TURKISH_MONTHS = {
        1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan", 5: "Mayıs",
        6: "Haziran", 7: "Temmuz", 8: "Ağustos", 9: "Eylül",
        10: "Ekim", 11: "Kasım", 12: "Aralık"
    }
    TURKISH_DAYS = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]

    # Ay ismini al
    month_name = TURKISH_MONTHS[month]

    # Takvim oluştur ve başlıkları düzelt
    calendar = HTMLCalendar().formatmonth(year, month)
    for i, english_day in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
        calendar = calendar.replace(english_day, TURKISH_DAYS[i])

    # Şablona gönderilecek veriler
    context = {
        'year': year,
        'month': month,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
        'calendar': calendar,
        'month_name': month_name,
    }

    return render(request, 'calendar_app/calendar.html', context)
