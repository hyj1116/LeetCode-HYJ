class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 360/12*(hour+minutes/60)
        minutes_angle = minutes / 60*360
        if abs(hour_angle-minutes_angle) < 180:
            return abs(hour_angle-minutes_angle)
        else:
            return 360 - abs(hour_angle-minutes_angle)
