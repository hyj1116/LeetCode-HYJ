import datetime


class Solution:
    def daysBetweenDates(self, date1, date2):
        d1 = date1.split("-")
        d2 = date2.split("-")
        date1 = datetime.datetime(int(d1[0]), int(d1[1]), int(d1[2]))  # 第一個日期
        date2 = datetime.datetime(int(d2[0]), int(d2[1]), int(d2[2]))  # 第二個日期
        interval = date1 - date2                    # 兩日期差距
        if int(d2[0]) > int(d1[0]):
            interval = -interval
        elif int(d2[0]) == int(d1[0]):
            if int(d2[1]) > int(d1[1]):
                interval = -interval
            elif int(d2[1]) == int(d1[1]):
                if int(d2[2]) > int(d1[2]):
                    interval = -interval
        return interval.days                  # 具體的天數


if __name__ == "__main__":
    solution = Solution()
    print(solution.daysBetweenDates("2019-06-29", "2019-06-30"))
