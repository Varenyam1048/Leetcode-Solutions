class Solution:
    def dayOfYear(self, date: str) -> int:
        
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        
        
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_months[1] = 29  
            
        
        total_days = sum(days_in_months[:month - 1]) + day
        
        return total_days