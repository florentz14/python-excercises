# -------------------------------------------------
# File Name: person_age.py
# Author: Florentino
# Date: 3/20/26
# Description: Person age calculation class using utils.py utilities.
#              Calculates age and birthday information from birth date.
# -------------------------------------------------

from datetime import datetime, date, timedelta
from typing import Optional
from utils import format_human_date, human_date_diff, date_diff
from tabulate import tabulate

class PersonAge:
    """A class to calculate age and birthday information for a person."""
    
    def __init__(self, name: str, birth_date: date) -> None:
        """
        Initialize a PersonAge object.
        
        Args:
            name (str): Person's full name
            birth_date (date): Date of birth
        """
        self.name = name
        self.birth_date = birth_date
        self._today = date.today()
    
    @property
    def age(self) -> int:
        """Calculate current age in years."""
        years = self._today.year - self.birth_date.year
        
        # Adjust if birthday hasn't occurred yet this year
        if (self._today.month < self.birth_date.month or 
            (self._today.month == self.birth_date.month and 
             self._today.day < self.birth_date.day)):
            years -= 1
        
        return years
    
    @property
    def age_in_months(self) -> int:
        """Calculate age in total months."""
        years_part = self.age * 12
        months_part = self._today.month - self.birth_date.month
        
        if self._today.day < self.birth_date.day:
            months_part -= 1
        
        return years_part + months_part
    
    @property
    def age_in_days(self) -> int:
        """Calculate age in total days."""
        return (self._today - self.birth_date).days
    
    @property
    def is_birthday_today(self) -> bool:
        """Check if today is the person's birthday."""
        return (self._today.month == self.birth_date.month and 
                self._today.day == self.birth_date.day)
    
    @property
    def days_until_birthday(self) -> int:
        """Calculate days until next birthday."""
        try:
            this_year_birthday = date(self._today.year, self.birth_date.month, self.birth_date.day)
        except ValueError:
            # Handle leap year babies - use February 28th in non-leap years
            this_year_birthday = date(self._today.year, 2, 28)
        
        if this_year_birthday < self._today:
            # Birthday already passed this year, calculate for next year
            try:
                next_birthday = date(self._today.year + 1, self.birth_date.month, self.birth_date.day)
            except ValueError:
                # Handle leap year babies for next year
                next_birthday = date(self._today.year + 1, 2, 28)
        else:
            # Birthday hasn't passed yet this year
            next_birthday = this_year_birthday
        
        return (next_birthday - self._today).days
    
    @property
    def next_birthday_date(self) -> date:
        """Get the date of the next birthday."""
        try:
            this_year_birthday = date(self._today.year, self.birth_date.month, self.birth_date.day)
        except ValueError:
            # Handle leap year babies - use February 28th in non-leap years
            this_year_birthday = date(self._today.year, 2, 28)
        
        if this_year_birthday < self._today:
            try:
                return date(self._today.year + 1, self.birth_date.month, self.birth_date.day)
            except ValueError:
                # Handle leap year babies for next year
                return date(self._today.year + 1, 2, 28)
        else:
            return this_year_birthday
    
    @property
    def age_on_next_birthday(self) -> int:
        """Get the age the person will be on their next birthday."""
        return self.age + 1
    
    def get_zodiac_sign(self) -> str:
        """Calculate zodiac sign based on birth date."""
        month, day = self.birth_date.month, self.birth_date.day
        
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Aquarius"
        else:
            return "Pisces"
    
    def get_birth_day_of_week(self) -> str:
        """Get the day of the week when the person was born."""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[self.birth_date.weekday()]
    
    def get_age_details(self) -> str:
        """Get detailed age breakdown using utils."""
        birth_datetime = datetime.combine(self.birth_date, datetime.min.time())
        today_datetime = datetime.combine(self._today, datetime.min.time())
        
        diff = date_diff(birth_datetime, today_datetime)
        
        return (f"Age: {self.age} years, {diff['months']} months, {diff['days']} days "
                f"({self.age_in_months} months total, {self.age_in_days} days total)")
    
    def get_birthday_info(self) -> str:
        """Get birthday information using utils."""
        if self.is_birthday_today:
            return f"🎉 HAPPY BIRTHDAY {self.name.upper()}! 🎉 Today you turn {self.age}!"
        
        days_until = self.days_until_birthday
        if days_until == 1:
            return f"🎂 Birthday tomorrow! You'll turn {self.age_on_next_birthday}."
        elif days_until <= 7:
            return f"🎈 Birthday in {days_until} days! You'll turn {self.age_on_next_birthday}."
        elif days_until <= 30:
            return f"📅 Birthday in {days_until} days. You'll turn {self.age_on_next_birthday}."
        else:
            return f"📅 Birthday in {days_until} days ({human_date_diff(datetime.combine(self.next_birthday_date, datetime.min.time()))})."
    
    def get_birth_date_formatted(self) -> str:
        """Get formatted birth date using utils."""
        birth_datetime = datetime.combine(self.birth_date, datetime.min.time())
        return format_human_date(birth_datetime, include_time=False)
    
    def get_time_since_birth(self) -> str:
        """Get human-readable time since birth using utils."""
        birth_datetime = datetime.combine(self.birth_date, datetime.min.time())
        return f"Born {human_date_diff(birth_datetime)}"
    
    def get_table_row(self) -> list:
        """Get person data as a table row."""
        birthday_status = "🎉 TODAY!" if self.is_birthday_today else f"{self.days_until_birthday} days"
        return [
            self.name,
            self.get_birth_date_formatted(),
            self.age,
            f"{self.age_in_months} months",
            f"{self.age_in_days} days",
            self.get_zodiac_sign(),
            birthday_status,
            self.get_time_since_birth()
        ]
    
    @staticmethod
    def get_table_headers() -> list:
        """Get table headers for person data."""
        return [
            "Name",
            "Birth Date",
            "Age (Years)",
            "Age (Months)",
            "Age (Days)",
            "Zodiac",
            "Next Birthday",
            "Time Since Birth"
        ]
    
    def get_complete_info(self) -> str:
        """Get complete person information."""
        info_lines = [
            f"👤 Name: {self.name}",
            f"📅 Birth Date: {self.get_birth_date_formatted()} ({self.get_birth_day_of_week()})",
            f"⭐ Zodiac Sign: {self.get_zodiac_sign()}",
            f"📊 {self.get_age_details()}",
            f"⏰ {self.get_time_since_birth()}",
            f"🎂 {self.get_birthday_info()}"
        ]
        
        return "\n".join(info_lines)
    
    @staticmethod
    def display_people_table(people: list) -> None:
        """Display multiple people in a formatted table."""
        if not people:
            print("No people to display.")
            return
        
        headers = PersonAge.get_table_headers()
        rows = [person.get_table_row() for person in people]
        
        print("\n" + "=" * 120)
        print("📊 PEOPLE AGE INFORMATION TABLE")
        print("=" * 120)
        print(tabulate(rows, headers=headers, tablefmt="grid", stralign="left"))
        print("=" * 120)
    
    def display_detailed_info(self) -> None:
        """Display detailed information for this person in table format."""
        detailed_data = [
            ["Name", self.name],
            ["Birth Date", f"{self.get_birth_date_formatted()} ({self.get_birth_day_of_week()})"],
            ["Zodiac Sign", self.get_zodiac_sign()],
            ["Current Age", f"{self.age} years"],
            ["Age in Months", f"{self.age_in_months} months"],
            ["Age in Days", f"{self.age_in_days} days"],
            ["Next Birthday", self.next_birthday_date.strftime("%Y-%m-%d")],
            ["Days Until Birthday", f"{self.days_until_birthday} days"],
            ["Age on Next Birthday", f"{self.age_on_next_birthday} years"],
            ["Time Since Birth", self.get_time_since_birth()],
            ["Birthday Status", "🎉 TODAY!" if self.is_birthday_today else "Not today"]
        ]
        
        print(f"\n{'='*60}")
        print(f"📋 DETAILED INFORMATION: {self.name.upper()}")
        print(f"{'='*60}")
        print(tabulate(detailed_data, headers=["Field", "Value"], tablefmt="grid", stralign="left"))
        print(f"{'='*60}")
        
        if self.is_birthday_today:
            print(f"\n🎉 HAPPY BIRTHDAY {self.name.upper()}! 🎉")
            print(f"   Today you turn {self.age} years old!")
        else:
            print(f"\n🎂 {self.get_birthday_info()}")
    
    def __str__(self) -> str:
        """String representation of PersonAge."""
        return f"{self.name} (Age: {self.age}, Born: {self.get_birth_date_formatted()})"


def main():
    """Main function to test PersonAge class."""
    print("=== Person Age Calculator Demo ===\n")
    
    # Create test people with different birth dates
    people = [
        PersonAge("Alice Johnson", date(1990, 5, 15)),      # Past birthday this year
        PersonAge("Bob Smith", date(1985, 12, 25)),        # Future birthday this year
        PersonAge("Charlie Brown", date(date.today().year, date.today().month, date.today().day)),  # Birthday today!
        PersonAge("Diana Prince", date(2000, 2, 29)),     # Leap year baby
        PersonAge("Eve Wilson", date(1975, 8, 30)),       # Born long ago
    ]
    
    # Display people in table format
    PersonAge.display_people_table(people)
    
    # Display detailed information for first person
    print("\n📋 DETAILED VIEW - First Person:")
    people[0].display_detailed_info()
    
    # Test specific scenarios
    print("\n=== Special Cases ===")
    
    # Test leap year calculation
    leap_year_person = PersonAge("Leap Baby", date(2000, 2, 29))
    print("\n🎂 Leap Year Baby - Detailed View:")
    leap_year_person.display_detailed_info()
    
    # Test birthday today
    birthday_person = people[2]
    if birthday_person.is_birthday_today:
        print(f"\n🎉 Today's Birthday:")
        print(f"   {birthday_person.get_birthday_info()}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
