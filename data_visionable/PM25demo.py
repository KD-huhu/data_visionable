import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager


class Draw_plot():

    def get_values(df):
        # set string through periodIndex to pandas
        period = pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"],freq="H")
        df["datetime"] = period
        # print(df.head(10))

        # set datetime as index
        df.set_index("datetime",inplace=True)

        # Conduct downsampling
        df = df.resample('7D').mean()
        # print(df.head())
        # delete nan
        data = df["PM_US Post"]

        # get values
        _x = data.index
        _y = data.values
        x = [i.strftime("%Y-%m-%d") for i in _x]

        return _x,_y,x



if __name__ == '__main__':
    # Set Chinese font
    my_font = font_manager.FontProperties(fname='C:/Windows/fonts/STSONG.TTF')

    # read cvs file
    file_path = []
    file_path.append('./PM2.5/BeijingPM20100101_20151231.csv')
    file_path.append('./PM2.5/ChengduPM20100101_20151231.csv')
    file_path.append('./PM2.5/GuangzhouPM20100101_20151231.csv')
    file_path.append('./PM2.5/ShanghaiPM20100101_20151231.csv')
    file_path.append('./PM2.5/ShenyangPM20100101_20151231.csv')
    name_list = ['北京','成都','广州','上海','沈阳']

    # set figure size
    plt.figure(figsize=(20, 8), dpi=80)

    for i in range(5):
        df = pd.read_csv(file_path[i])
        _x, _y, x = Draw_plot.get_values(df)
        # draw
        plt.plot(range(len(x)), _y,label=name_list[i])

    # draw legand
    plt.legend(prop=my_font)

    # Adjust X-axis scale
    plt.xticks(range(0, len(_x), 10), _x[::10], fontproperties=my_font, rotation=45)

    # Set axis legend
    plt.xlabel("日期", fontproperties=my_font)
    plt.ylabel("PM2.5", fontproperties=my_font)
    plt.title('PM2.5数据', fontproperties=my_font)

    # draw grid
    plt.grid(alpha=0.3)

    # show
    plt.show()