import tkinter as tk
import os

master = tk.Tk()
master.title("Json Converter")
iso_code = tk.StringVar(master)
var = tk.StringVar(master)
varA = tk.StringVar(master)
varB = tk.StringVar(master)


def write_file():
    file = open('FbCtf.json', 'a+')
    file.write('\n\n{"levels": [{"type": "%s",'  # 1  
               '\n"title": "%s"'  # 2
               '\n"active": "%s"'  # 3
               '\n"description": "%s"'  # 4 
               '\n"entity_iso_code": "%s"'  # 5
               '\n"category": "%s"'  # 6
               '\n"points": "%s"'  # 7
               '\n"bonus": "%s"'  # 8
               '\n"bonus_dec": "%s"'
               '\n"bonus_fix": "%s"'
               '\n"flag": "%s"'
               '\n"hint": "%s"'
               '\n"penalty": "%s"'
               '}]}' % (
                   varA.get(), e1.get(), iso_code.get(), e2.get(), country.get(),
                   varB.get(),
                   points.get(),
                   bonus.get(),
                   minus.get(),
                   hPP.get(),
                   ans.get(),
                   hint.get(),
                   hintMin.get()))
    file.close()


def remove_file():
    if os.path.exists("FbCtf.json"):
        os.remove("FbCtf.json")
    else:
        print("The file does not exist")


tk.Label(master,
         text="Type").grid(row=0)
set1 = tk.OptionMenu(master, varA, "Quiz", "Flag", "Base").grid(row=0, column=1)
varA.set('Select One')

tk.Label(master,
         text="Title").grid(row=1)

e1 = tk.Entry(master)
e1.grid(row=1, column=1)

tk.Radiobutton(master,
               text="ON",
               padx=10,
               variable=iso_code,
               value="True").grid(row=2, column=0)

tk.Radiobutton(master,
               text="OFF",
               padx=10,
               variable=iso_code,
               value="False").grid(row=2, column=1)

tk.Label(master,
         text="Question").grid(row=3)

e2 = tk.Entry()
e2.grid(row=3, column=1)

tk.Label(master,
         text="Country").grid(row=4)
choices = {
    'AFGHANISTAN': 'AF', 'ALBANIA': 'AL', 'ALGERIA': 'DZ', 'ANGOLA': 'AO', 'ARGENTINA': 'AR',
    'ARMENIA': 'AM', 'AUSTRALIA': 'AU', 'AUSTRIA': 'AT', 'AZERBAIJAN': 'AZ', 'BAHAMAS': 'BS',
    'BANGLADESH': 'BD', 'BELARUS': 'BY', 'BELGIUM': 'BE', 'BELIZE': 'BZ', 'BENIN': 'BJ',
    'BHUTAN': 'BT', 'BOLIVIA': 'BO', 'BOSNIA & HERZEGOVINA': 'BA', 'BOTSWANA': 'BW',
    'BRAZIL': 'BR', 'BRUNEI': 'BN', 'BULGARIA': 'BG', 'BURRKINA FASO': 'BF', 'BURUNDI': 'BI',
    'CAMBODIA': 'KH', 'CAMEROON': 'CM', 'CANADA': 'CA', 'CENTRAL AFRICAN REPUBLIC': 'CF', 'CHAD': 'TD',
    'CHILE': 'CL', 'CHINA': 'CN', 'COLOMBIA': 'CO', 'CONGO-BRAZZAVILLE': 'CG', 'CONGO-KINSHASA': 'CD',
    'COSTA RICA': 'CR', 'CROATIA': 'HR', 'CUBA': 'CU', 'CYPRUS': 'CY', 'CZECH REPUBLIC': 'CZ',
    'CÔTE DIVOIRE': 'CI', 'DENMARK': 'DK', 'DJIBOUTI': 'DJ', 'DOMINICAN REPUBLIC': 'DO', 'ECUADOR': 'EC',
    'EGYPT': 'EG', 'EL SALVADOR': 'SV', 'EQUATORIAL GUJNEA': 'GQ', 'ERITREA': 'ER', 'ESTONI': 'AEE',
    'ETHOPHIA': 'ET', 'FALKLAND ISLANDS': 'FK', 'FIJI': 'FJ', 'FINLAND': 'FI', 'FRANCE': 'FR',
    'FRENCHGUIANA': 'GF', 'FRENCH SOUTHERN TERRITORIES': 'TF', 'GABON': 'GA', 'GAMBIA': 'GM',
    'GEORGIA': 'GE', 'GERMANY': 'DE', 'GHANA': 'GH', 'GREECE': 'GR', 'GREENLAND': 'GL', 'GUATEMALA': 'GT',
    'GUINEA': 'GN', 'GUINEA-BISSAU': 'GW', 'GUYANA': 'GY', 'HAITI': 'HT', 'HONDURAS': 'HN', 'HUNGARY': 'HU',
    'ICELAND': 'IS', 'INDIA': 'IN', 'INDONESIA': 'ID', 'IRAN': 'IR', 'IRAQ': 'IQ', 'IRELAND': 'IE', 'ISREAL': 'IL',
    'ITALY': 'IT', 'JAMAICA': 'JM', 'JAPAN': 'JP', 'JORDAN': 'JO', 'KAZAKHSTAN': 'KZ', 'KENYA': 'KE', 'KOSOVO': 'XK',
    'KUWAIT': 'KW', 'KYRGYZSTAN': 'KG', 'LADS': 'LA', 'LATVIA': 'LV', 'LEBANON': 'LB', 'LESOTHO': 'LS', 'LIBERIA': 'LR',
    'LIBYA': 'LY', 'LUTHUANIA': 'LT', 'LUXEMBOURG': 'LU', 'MACEDONIA': 'MK', 'MADAGASCAR': 'MG', 'MALAWI': 'MW',
    'MALAYSIA': 'MY', 'MALI': 'ML', 'MAURITANIA': 'MR', 'MEXICO': 'MX', 'MOLDOVA': 'MD', 'MONGOLIA': 'MN',
    'MONTENEGRO': 'ME',
    'MOROCCO': 'MA', 'MOZAMBIQUE': 'MZ', 'MYANMAR(BURMA)': 'MM', 'NAMBIA': 'NA', 'NEPAL': 'NP', 'NETHERLANDS': 'NL',
    'NEW CALEDONIA': 'NC', 'NEW ZELAND': 'NZ', 'NICARAGUA': 'NI', 'NIGER': 'NE', 'NIGERIA': 'NG', 'NORTh KOREA': 'KP',
    'NORWAY': 'NO', 'OMAN': 'OM', 'PAKISTAN': 'PK', 'PALESTINIAN TERRITORIES': 'PS', 'PANAMA': 'PA',
    'PAPUA NEW GUINEA': 'PG',
    'PARAGUAY': 'PY', 'PERU': 'PE', 'PHILIPPINES': 'PH', 'POLAND': 'PL', 'PORTUGAL': 'PT', 'PUERTO RICO': 'PR',
    'QATAR': 'QA', 'ROMANIA': 'RD', 'RUSSIA': 'RU', 'RWANDA': 'RW', 'SAUDI ARABIA': 'SA', 'SENEGAL': 'SN',
    'SERBIA': 'RS', 'SIERRA LEONE': 'SL', 'SLOVAKIA': 'SK', 'SLOVENIA': 'SI', 'SOLOMAN ISLANDS': 'SB', 'SOMALIA': 'SO',
    'SOUTH AFRICA': 'ZA', 'SOUTH KOREA': 'KR', 'SOUTH SUDAN': 'SS', 'SPAIN': 'ES', 'SRI LANKA': 'LK', 'SUDAN': 'SD',
    'SURINAME': 'SR', 'SVALBARD & JAN MAYEN': 'SJ', 'SWAZILAND': 'SZ', 'SWEDEN': 'SE', 'SWITZWELAND': 'CH',
    'SYRIA': 'SY',
    'TAIWAN': 'TW', 'TAJIKISTAN': 'TJ', 'TANZANIA': 'TZ', 'THAILAND': 'TH', 'TIMOR-LESTE': 'TL', 'TOGO': 'TG',
    'TRINIDAD & TOBAGO': 'TT', 'TUNISA': 'TN', 'TURKEY': 'TR', 'TURKMENISTAN': 'TM', 'UGANDA': 'UG', 'UKRAIN': 'UA',
    'UNITED ARAB EMERATES': 'AE', 'UNITED KINGDOM': 'GB', 'UNITED STATES': 'US', 'URUGUAY': 'UY', 'UZBEKISTAN': 'UZ',
    'VANUATU': 'VU', 'VENEZUELA': 'VE', 'VIETNAM': 'VN', 'WESTERN SAHARA': 'EH', 'YEMEN': 'YE', 'ZAMBIA': 'ZM',
    'ZIMBABWE': 'ZW'
}

option = tk.OptionMenu(master, var, *choices).grid(row=4, column=1)
country = tk.StringVar()
var.set('Select One')


def change_country(*args):
    country_ = choices[var.get()]
    country.set(country_)


var.trace('w', change_country)

tk.Label(master,
         text="Category").grid(row=5)
set2 = tk.OptionMenu(master, varB, "None", "Quiz", "Flag", "Base").grid(row=5, column=1)
varB.set('Select One')

tk.Label(master,
         text="Points").grid(row=6)
points = tk.Spinbox(master, from_=0, to=100)
points.grid(row=6, column=1)


tk.Label(master,
         text="Bonus").grid(row=7)
bonus = tk.Spinbox(master, from_=0, to=100)
bonus.grid(row=7, column=1)

tk.Label(master,
         text="-Dec").grid(row=8)
minus = tk.Spinbox(master, from_=0, to=100)
minus.grid(row=8, column=1)

tk.Label(master,
         text="Highest Possible Points").grid(row=9)
hPP = tk.Spinbox(master, from_=0, to=100)
hPP.grid(row=9, column=1)

tk.Label(master,
         text="Answer").grid(row=10)
ans = tk.Entry(master)
ans.grid(row=10, column=1)

tk.Label(master,
         text="Hint").grid(row=11)
hint = tk.Entry(master)
hint.grid(row=11, column=1)

tk.Label(master,
         text="Hint Penalty").grid(row=12)
hintMin = tk.Spinbox(master, from_=0, to=100)
hintMin.grid(row=12, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=13,
                                    column=3)


tk.buttonWrite = tk.Button(master)
tk.buttonWrite.config(text='Write To File', command=write_file)
tk.buttonWrite.grid(row=13, column=0)

tk.buttonDelete = tk.Button(master)
tk.buttonDelete.config(text='Remove File', command=remove_file)
tk.buttonDelete.grid(row=13, column=1)

tk.mainloop()
