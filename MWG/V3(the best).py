import itertools
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich import print as rprint
from rich.progress import Progress, SpinnerColumn
from rich.panel import Panel
import time
import os
import random
import string

def display_banner():
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║                                                           ║ 
    ║                                                           ║
    ║         ██████   ██████    █████   ███   █████    █████████  
    ║    ░░██████ ██████    ░░███   ░███  ░░███      ███░░░░░███║
    ║     ░███░█████░███     ░███   ░███   ░███     ███     ░░░ ║
    ║     ░███░░███ ░███     ░███   ░███   ░███    ░███         ║
    ║     ░███ ░░░  ░███     ░░███  █████  ███     ░███    █████║
    ║     ░███      ░███      ░░░█████░█████░      ░░███  ░░███ ║
    ║     █████     █████ ██    ░░███ ░░███      ██ ░░█████████                
    ║    ░░░░░     ░░░░░ ░░      ░░░   ░░░      ░░   ░░░░░░░░░                  
    ║                                                                              
    ║                 MASTER WORDLIST GENERATOR v4.0                                     
    ║                                                               ░░░░░░███████ ]▄▄▄▄▄▄▄▄  
    ║                                                               ▂▄▅█████████▅▄▃▂       
    ║                                                              [███████████████████].      
    ║                                                               ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..          
    ║     [R]andom Mode (Recomanded)  |  [L]ogical Mode                       
    ║                 No password can Stop you                               
    ║                                     
    ║
    
    ║Made by: WhitexHunter║               MWG>Cupp
    ╚═══════════════════════════════════════════════════════════╝    
    """
    console = Console()
    console.print(Panel(banner, style="bold blue"))
    console.print("[yellow]⚠️  For authorized security testing only. Use responsibly.[/yellow]\n")

class AdvancedWordlistGenerator:
    def __init__(self):
        self.console = Console()
        self.info = {}
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.common_numbers = ["123", "1234", "12345", "123456", "12", "1", "2", "01", "02"]
        self.years = [str(year) for year in range(1960, 2025)]
        
    def get_user_input(self):
        # Basic Personal Information
        self.console.print("\n[cyan]═══ Basic Personal Information ═══[/cyan]")
        self.info['firstname'] = Prompt.ask("[cyan]First name").lower()
        self.info['lastname'] = Prompt.ask("[cyan]Last name").lower()
        self.info['middlename'] = Prompt.ask("[cyan]Middle name").lower()
        self.info['nicknames'] = Prompt.ask("[cyan]Nicknames (comma separated)").lower()
        self.info['birthdate'] = Prompt.ask("[cyan]Birthdate (DDMMYYYY)")
        self.info['birthplace'] = Prompt.ask("[cyan]Birth place").lower()
        self.info['nationality'] = Prompt.ask("[cyan]Nationality").lower()

        # Extended Family Information
        self.console.print("\n[cyan]═══ Extended Family Information ═══[/cyan]")
        self.info['mother_name'] = Prompt.ask("[cyan]Mother's full name").lower()
        self.info['mother_maiden'] = Prompt.ask("[cyan]Mother's maiden name").lower()
        self.info['mother_birthdate'] = Prompt.ask("[cyan]Mother's birthdate (DDMMYYYY)")
        self.info['father_name'] = Prompt.ask("[cyan]Father's full name").lower()
        self.info['father_birthdate'] = Prompt.ask("[cyan]Father's birthdate (DDMMYYYY)")
        self.info['grandma_name'] = Prompt.ask("[cyan]Grandmother's name(s) (comma separated)").lower()
        self.info['grandpa_name'] = Prompt.ask("[cyan]Grandfather's name(s) (comma separated)").lower()

        # Siblings Information
        self.console.print("\n[cyan]═══ Siblings Information ═══[/cyan]")
        self.info['siblings'] = Prompt.ask("[cyan]Siblings' names (comma separated)").lower()
        self.info['siblings_birthdates'] = Prompt.ask("[cyan]Siblings' birthdates (comma separated)")
        self.info['siblings_nicknames'] = Prompt.ask("[cyan]Siblings' nicknames (comma separated)").lower()

        # Partner Information
        self.console.print("\n[cyan]═══ Partner Information ═══[/cyan]")
        self.info['partner'] = Prompt.ask("[cyan]Partner's full name").lower()
        self.info['partner_nickname'] = Prompt.ask("[cyan]Partner's nickname").lower()
        self.info['partner_birthdate'] = Prompt.ask("[cyan]Partner's birthdate (DDMMYYYY)")
        self.info['anniversary'] = Prompt.ask("[cyan]Anniversary date (DDMMYYYY)")
        self.info['meeting_date'] = Prompt.ask("[cyan]First meeting date (DDMMYYYY)")

        # Children Information
        self.console.print("\n[cyan]═══ Children Information ═══[/cyan]")
        self.info['children'] = Prompt.ask("[cyan]Children's names (comma separated)").lower()
        self.info['children_nicknames'] = Prompt.ask("[cyan]Children's nicknames (comma separated)").lower()
        self.info['children_birthdates'] = Prompt.ask("[cyan]Children's birthdates (comma separated)")
        self.info['children_schools'] = Prompt.ask("[cyan]Children's schools (comma separated)").lower()

        # Company Information
        self.console.print("\n[cyan]═══ Company Information ═══[/cyan]")
        self.info['company_name'] = Prompt.ask("[cyan]Company name")
        self.info['department'] = Prompt.ask("[cyan]Department").lower()
        self.info['employee_id'] = Prompt.ask("[cyan]Employee ID")
        self.info['work_phone'] = Prompt.ask("[cyan]Work phone")
        self.info['work_email'] = Prompt.ask("[cyan]Work email")
        self.info['job_title'] = Prompt.ask("[cyan]Job title").lower()
        self.info['start_date'] = Prompt.ask("[cyan]Start date (DDMMYYYY)")
        self.info['supervisor'] = Prompt.ask("[cyan]Supervisor's name").lower()

        # Contact Information
        self.console.print("\n[cyan]═══ Contact Information ═══[/cyan]")
        self.info['phone'] = Prompt.ask("[cyan]Personal phone")
        self.info['alt_phone'] = Prompt.ask("[cyan]Alternative phone")
        self.info['email'] = Prompt.ask("[cyan]Personal email")
        
        # Address Information
        self.info['street'] = Prompt.ask("[cyan]Street address").lower()
        self.info['city'] = Prompt.ask("[cyan]City").lower()
        self.info['state'] = Prompt.ask("[cyan]State").lower()
        self.info['zip'] = Prompt.ask("[cyan]ZIP code")
        self.info['country'] = Prompt.ask("[cyan]Country").lower()

        # Favorites & Preferences
        self.console.print("\n[cyan]═══ Favorites & Preferences ═══[/cyan]")
        self.info['favorite_color'] = Prompt.ask("[cyan]Favorite color").lower()
        self.info['favorite_number'] = Prompt.ask("[cyan]Favorite number")
        self.info['favorite_food'] = Prompt.ask("[cyan]Favorite food").lower()
        self.info['favorite_movie'] = Prompt.ask("[cyan]Favorite movie").lower()
        self.info['favorite_song'] = Prompt.ask("[cyan]Favorite song").lower()
        self.info['hobby'] = Prompt.ask("[cyan]Hobbies (comma separated)").lower()
        self.info['sports_team'] = Prompt.ask("[cyan]Favorite sports team").lower()
        self.info['pet_name'] = Prompt.ask("[cyan]Pet names (comma separated)").lower()

        # Education
        self.console.print("\n[cyan]═══ Education Information ═══[/cyan]")
        self.info['school_name'] = Prompt.ask("[cyan]School name").lower()
        self.info['graduation_year'] = Prompt.ask("[cyan]Graduation year")
        self.info['student_id'] = Prompt.ask("[cyan]Student ID")
        self.info['major'] = Prompt.ask("[cyan]Major/Field of study").lower()

        # Social Media
        self.console.print("\n[cyan]═══ Social Media ═══[/cyan]")
        self.info['username'] = Prompt.ask("[cyan]Common username").lower()
        self.info['gaming_name'] = Prompt.ask("[cyan]Gaming username").lower()

        # Remove empty values
        self.info = {k: v for k, v in self.info.items() if v}

    def process_date(self, date_str):
        if not date_str or len(date_str) != 8:
            return []
        
        day = date_str[:2]
        month = date_str[2:4]
        year = date_str[4:]
        short_year = year[2:]
        
        return {
            'day': day,
            'month': month,
            'year': year,
            'short_year': short_year,
            'ddmm': f"{day}{month}",
            'mmyy': f"{month}{short_year}",
            'ddmmyy': f"{day}{month}{short_year}",
            'mmddyyyy': f"{month}{day}{year}",
            'yyyymmdd': f"{year}{month}{day}"
        }

    def logical_mode(self):
        combinations = set()
        name = self.info.get('firstname', '')
        lastname = self.info.get('lastname', '')
        
        # Process all dates
        dates = {}
        for date_field in ['birthdate', 'anniversary', 'partner_birthdate', 'start_date']:
            if date_field in self.info:
                dates[date_field] = self.process_date(self.info[date_field])

        # Apply 200 patterns
        if name and lastname:
            # Basic name combinations
            combinations.update([
                f"{name}{lastname}",
                f"{lastname}{name}",
                f"{name}.{lastname}",
                f"{lastname}.{name}",
                f"{name}_{lastname}",
                f"{name}{lastname}123",
                f"{name}.{lastname}2024",
                f"{name}@{lastname}",
                f"{name}#{lastname}",
                f"{name}&{lastname}",
                f"{name}{lastname}!",
            ])

        # Add birthday combinations if available
        if 'birthdate' in dates:
            bd = dates['birthdate']
            combinations.update([
                f"{name}{bd['year']}",
                f"{name}{bd['ddmm']}",
                f"{lastname}{bd['year']}",
                f"{name}{bd['mmddyyyy']}",
                f"{lastname}{bd['yyyymmdd']}"
            ])

        # Add phone combinations if available
        if 'phone' in self.info:
            phone = self.info['phone']
            phone_last4 = phone[-4:] if len(phone) >= 4 else phone
            combinations.update([
                f"{name}{phone}",
                f"{phone}{name}",
                f"{name}{phone_last4}",
                f"{lastname}{phone_last4}",
            ])

        # Add company combinations
        if 'company_name' in self.info:
            company = self.info['company_name']
            combinations.update([
                f"{name}@{company}",
                f"{name}.{company}",
                f"{name}{company}2024"
            ])

        # Generate more complex combinations based on all available information
        for word1 in self.info.values():
            if isinstance(word1, str) and word1:
                # Add single word variations
                combinations.add(f"{word1}123")
                combinations.add(f"{word1}2024")
                combinations.add(f"{word1}!")
                
                # Add reversed variations
                combinations.add(f"{word1[::-1]}")
                combinations.add(f"{word1[::-1]}123")

                # Mix with other words
                for word2 in self.info.values():
                    if isinstance(word2, str) and word2 and word1 != word2:
                        combinations.add(f"{word1}{word2}")
                        combinations.add(f"{word1}.{word2}")
                        combinations.add(f"{word1}_{word2}")
                        combinations.add(f"{word1}{word2}123")

        return combinations

    def random_mode(self):
        combinations = set()
        words = [v for v in self.info.values() if isinstance(v, str) and v]
        
        for _ in range(1000000):  # Generate 1 million combinations
            if random.random() < 0.3:  # 30% pure random
                length = random.randint(8, 16)
                chars = string.ascii_letters + string.digits + self.special_chars
                combinations.add(''.join(random.choice(chars) for _ in range(length)))
            else:
                # Create combinations from available information
                num_elements = random.randint(2, 4)
                elements = []
                
                for _ in range(num_elements):
                    element = random.choice([
                        lambda: random.choice(words) if words else "",
                        lambda: random.choice(self.common_numbers),
                        lambda: random.choice(self.special_chars),
                        lambda: random.choice(self.years)
                    ])()
                    if element:
                        elements.append(str(element))
                
                if elements:
                    separator = random.choice(['', '_', '.', '-', '@', '#'])
                    combination = separator.join(elements)
                    
                    # Apply random transformations
                    if random.random() < 0.3:
                        combination = combination.capitalize()
                    if random.random() < 0.2:
                        combination = combination.upper()
                    
                    combinations.add(combination)

        return combinations

    def generate_wordlist(self, mode='logical'):
        if mode == 'logical':
            return self.logical_mode()
        else:
            return self.random_mode()

def main():
    display_banner()
    
    generator = AdvancedWordlistGenerator()
    generator.get_user_input()
    
    console = Console()
    
    mode = Prompt.ask(
        "\n[cyan]Select mode",
        choices=["logical", "random", "both"],
        default="both"
    )
    
    all_combinations = set()
    
    with Progress(
        SpinnerColumn(),
        *Progress.get_default_columns(),
        transient=True
    ) as progress:
        
        if mode in ['logical', 'both']:
            task = progress.add_task("[cyan]Generating logical combinations...", total=100)
            logical_combinations = generator.generate_wordlist(mode='logical')
            all_combinations.update(logical_combinations)
            progress.update(task, completed=100)
            
        if mode in ['random', 'both']:
            task = progress.add_task("[cyan]Generating random combinations...", total=100)
            random_combinations = generator.generate_wordlist(mode='random')
            all_combinations.update(random_combinations)
            progress.update(task, completed=100)
    
    # Save results
    output_file = f"wordlist_{mode}_{int(time.time())}.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(all_combinations):
            if 6 <= len(word) <= 32:  # Filter by length
                f.write(f"{word}\n")
    
    console.print(f"\n[green]✓[/green] Generated {len(all_combinations):,} unique combinations")
    console.print(f"[green]✓[/green] Saved to: {output_file}")
    
    # Show sample
    console.print("\n[cyan]Sample of generated words:[/cyan]")
    sample_size = min(20, len(all_combinations))
    for word in random.sample(list(all_combinations), sample_size):
        console.print(f"[grey70]{word}[/grey70]")

if __name__ == "__main__":
    main()
#Enjoy ;) 