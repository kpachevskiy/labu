# coding=utf-8
from spyre import server
import pandas as pd
import os


class laba2(server.App):
    title = "DATA"
    d={
        '1.csv':'Cherkasy','2.csv':'Chernihiv','3.csv':'Chernivtsi','4.csv':'Crimea','5.csv':'Dnipropetrovsk','6.csv':'Donetsk',
        '7.csv':'Ivano-Frankivsk','8.csv':'Kharkiv', '9.csv':'Kherson','10.csv':'Khmelnytskyy', '11.csv':'Kiev','12.csv':'Kiev_City',
        '13.csv':'Kirovohrad','14.csv':'Luhansk','15.csv':'Lviv','16.csv':'Mykolayiv',
    '17.csv':'Odesa','18.csv':'Poltava','19.csv':'Rivne','20.csv':'Sevastopol','21.csv':'Sumy',
          '22.csv':'Ternopil','23.csv':'Transcarpathia','24.csv':'Vinnytsya','25.csv':'Volyn','26.csv':'Zaporizhzhya'
    }
    inputs = [
        {
            "type": "dropdown",
            "id": "file",
            "label": "Provience file",
            "options": [{"label": d[filename], "value": filename} for filename in os.listdir("data")],
            "key": 'file',
            "action_id": "update"
        },
        {
            "type": "dropdown",
            "id": "year",
            "label": "Year",
            "options": [{"label": year, "value": year} for year in range(1981, 2018)],
            "key": "year",
            "action_id": "update",
        },
        {
            "type": "dropdown",
            "id": "week1",
            "label": "Week to start",
            "options": [{"label": week1, "value": week1} for week1 in range(1, 53)],  # fix 1981 and 2017
            "key": "week1",
            "action_id": "update",
        },
        {
            "type": "dropdown",
            "id": "week2",
            "label": "Finishing week",
            "options": [{"label": week2, "value": week2} for week2 in range(1, 53)],
            "key": "week2",
            "action_id": "update",
        },
        {
            "type": "dropdown",
            "id": "index",
            "label": "Researchable index",
            "options": [
                {"label": "VHI", "value": "VHI"},
                {"label": "TCI", "value": "TCI"},
                {"label": "VCI", "value": "VCI"},
                {"label": "SMT", "value": "SMT"},
                {"label": "SMN", "value": "SMN"},
            ],
            "key": "index",
            "action_id": "update",
        }
    ]
    outputs = [
        {
            "type": "table",
            "id": "table_year",
            "control_id": "update",
            "tab": "Table"
        },
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update",
            "tab": "Plot",
        }
    ]
    controls = [
        {
            "type": "hidden",
            "id": "update",
        }
    ]
    tabs = ["Table", "Plot"]

    def getData(self, params):
        filename = params["file"]
        #filename2 = params["file2"]
        year = int(params["year"])
        sweek = int(params["week1"])
        fweek = int(params["week2"])
        df = pd.read_csv("data/%s" %(filename), index_col=False, engine='python', header=1)
        #df2 = pd.read_csv("data/%s" % (filename2), index_col=False, engine='python', header=1)
        df = df.ix[df.year == year]
        #df2 = df2.ix[df2.year == year]

        return df[(df.week >= sweek) & (df.week <= fweek)] #+ df2[(df2.week >= sweek) & (df2.week <= fweek)]

    def getPlot(self, params):
        df = self.getData(params).set_index('week')
        type_index = params["index"]
        df = df[[type_index]]
        plt_obj = df.plot()
        plt_obj.set_ylabel(type_index)
        plt_obj.set_title(type_index + " for week range you chose")
        plt_obj.grid()
        return plt_obj.get_figure()
app = laba2()
app.launch()