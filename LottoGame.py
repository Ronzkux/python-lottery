import random

def get_unique_numbers_lotto():
    numbers = []
    while len(numbers) < 7:
        num = input("Välj nummer mellan (1-40): ").strip()
        if num.isdigit() and 1 <= int(num) <= 40 and int(num) not in numbers:
            numbers.append(int(num))
        else:
            print("Felaktig svar. Välj nummer mellan 1 och 40.")
    return sorted(numbers)

def get_unique_numbers(min_num, max_num, count, type_name):
    numbers = []
    while len(numbers) < count:
        num = input(f"Välj {type_name} mellan ({min_num}-{max_num}): ").strip()
        if num.isdigit() and min_num <= int(num) <= max_num and int(num) not in numbers:
            numbers.append(int(num))
        else:
            print(f"Felaktig svar. Välj {type_name} mellan {min_num} och {max_num}.")
    return sorted(numbers)

# Låter användaren själv insätta nummer.
def get_user_numbers_lotto(num_rows):
    user_numbers = []
    for _ in range(num_rows):
        main_numbers = get_unique_numbers(1, 40, 7, "huvud")
        extra_number = get_unique_numbers(1, 40, 1, "extra")[0]
        user_numbers.append(main_numbers + [extra_number])
    return user_numbers

def get_user_numbers_eurojackpot(num_rows):
    user_numbers = []
    for _ in range(num_rows):
        main_numbers = get_unique_numbers(1, 50, 5, "huvud")
        extra_numbers = get_unique_numbers(1, 12, 2, "extra")
        user_numbers.append(main_numbers + extra_numbers)
    return user_numbers

def get_user_numbers_vikinglotto(num_rows):
    user_numbers = []
    for _ in range(num_rows):
        main_numbers = get_unique_numbers(1, 48, 6, "huvud")
        extra_number = get_unique_numbers(1, 5, 1, "extra")[0]
        user_numbers.append(main_numbers + [extra_number])
    return user_numbers

def get_user_numbers_keno(num_rows, keno_tier):
    user_numbers = []
    for _ in range(num_rows):
        numbers = get_unique_numbers(1, 70, keno_tier, "nummer")
        user_numbers.append(numbers)
    return user_numbers

def get_user_numbers_jokeri(num_rows):
    user_numbers = []
    for _ in range(num_rows):
        numbers = []
        while len(numbers) < 7:
            num = input("Välj nummer (0-9) för Jokeri: ").strip()
            if num.isdigit() and 0 <= int(num) <= 9:
                numbers.append(int(num))
            else:
                print("Felaktig svar. Välj nummer mellan 0 och 9.")
        user_numbers.append(numbers)
    return user_numbers

# Genererar slumpmässiga nummer
def generate_user_numbers_lotto(num_rows):
    user_numbers = []
    for _ in range(num_rows):
        main_numbers = random.sample(range(1, 41), 7)
        extra_number = random.randint(1, 41)
        user_numbers.append(sorted(main_numbers) + [extra_number])
    return user_numbers

def generate_user_numbers_eurojackpot(num_rows):
    return [sorted(random.sample(range(1, 51), 5)) + sorted(random.sample(range(1, 13), 2)) for _ in range(num_rows)]

def generate_user_numbers_vikinglotto(num_rows):
    user_numbers = []
    for _ in range(num_rows):
        main_numbers = random.sample(range(1, 49), 6)
        extra_number = random.randint(1, 5)
        user_numbers.append(sorted(main_numbers) + [extra_number])
    return user_numbers

def generate_user_numbers_keno(num_rows, keno_tier):
    user_numbers = []
    for _ in range(num_rows):
        numbers = random.sample(range(1, 71), keno_tier)
        user_numbers.append(sorted(numbers))
    return user_numbers

def generate_user_numbers_jokeri(num_rows):
    user_numbers = []
    for _ in range(num_rows):
        numbers = random.choices(range(10), k=7)
        user_numbers.append(numbers)
    return user_numbers

# Formaterar som strings.
def format_numbers_lotto(numbers):
    main_numbers_str = ", ".join(map(str, sorted(numbers[:7])))
    extra_number_str = str(numbers[7])
    return f"{main_numbers_str} + {extra_number_str}"

def format_numbers_eurojackpot(numbers):
    main_numbers_str = ", ".join(map(str, sorted(numbers[:5])))
    extra_numbers_str = ", ".join(map(str, sorted(numbers[5:])))
    return f"{main_numbers_str} + {extra_numbers_str}"

def format_numbers_vikinglotto(numbers):
    main_numbers_str = ", ".join(map(str, sorted(numbers[:6])))
    extra_number_str = str(numbers[6])
    return f"{main_numbers_str} + {extra_number_str}"

def format_numbers_keno(numbers):
    return ", ".join(map(str, sorted(numbers)))

def format_numbers_jokeri(numbers):
    return ", ".join(map(str, numbers))

# Kollar om spelaren har vunnit
def check_win_lotto(user_numbers, winning_numbers, _):
    wins = []
    for index, numbers in enumerate(user_numbers):
        main_matches = len(set(numbers[:7]).intersection(winning_numbers[:7]))
        extra_match = numbers[7] == winning_numbers[7]
        
        if main_matches == 3 and extra_match:
            wins.append(f"Rad {index + 1}: Du har 3 + 1 rätt!")
        elif main_matches == 4 and not extra_match:
            wins.append(f"Rad {index + 1}: Du har 4 rätt!")
        elif main_matches == 5:
            wins.append(f"Rad {index + 1}: Du har 5 rätt!")
        elif main_matches == 6:
            wins.append(f"Rad {index + 1}: Du har 6 rätt!")
        elif main_matches == 6 and extra_match:
            wins.append(f"Rad {index + 1}: Du har 6 + 1 rätt!")
        elif main_matches == 7:
            wins.append(f"Rad {index + 1}: Jackpot!")

    return wins

def check_win_eurojackpot(user_numbers, winning_numbers, _):
    wins = []
    for index, numbers in enumerate(user_numbers):
        main_matches = len(set(numbers[:5]).intersection(winning_numbers[:5]))
        extra_matches = len(set(numbers[5:]).intersection(winning_numbers[5:]))
        
        if main_matches == 5 and extra_matches == 2:
            wins.append(f"Rad {index + 1}: Jackpot!")
        elif main_matches == 5 and extra_matches == 1:
            wins.append(f"Rad {index + 1}: Du har 5 + 1 rätt!")
        elif main_matches == 5 and extra_matches == 0:
            wins.append(f"Rad {index + 1}: Du har 5 + 0 rätt!")
        elif main_matches == 4 and extra_matches == 2:
            wins.append(f"Rad {index + 1}: Du har 4 + 2 rätt!")
        elif main_matches == 4 and extra_matches == 1:
            wins.append(f"Rad {index + 1}: Du har 4 + 1 rätt!")
        elif main_matches == 4 and extra_matches == 0:
            wins.append(f"Rad {index + 1}: Du har 4 + 0 rätt!")
        elif main_matches == 3 and extra_matches == 2:
            wins.append(f"Rad {index + 1}: Du har 3 + 2 rätt!")
        elif main_matches == 2 and extra_matches == 2:
            wins.append(f"Rad {index + 1}: Du har 2 + 2 rätt!")
        elif main_matches == 3 and extra_matches == 1:
            wins.append(f"Rad {index + 1}: Du har 3 + 1 rätt!")
        elif main_matches == 3 and extra_matches == 0:
            wins.append(f"Rad {index + 1}: Du har 3 + 0 rätt!")
        elif main_matches == 1 and extra_matches == 2:
            wins.append(f"Rad {index + 1}: Du har 1 + 2 rätt!")
        elif main_matches == 2 and extra_matches == 1:
            wins.append(f"Rad {index + 1}: Du har 2 + 1 rätt!")

    return wins

def check_win_vikinglotto(user_numbers, winning_numbers, _):
    wins = []
    for index, numbers in enumerate(user_numbers):
        main_matches = len(set(numbers[:6]).intersection(winning_numbers[:6]))
        extra_match = numbers[6] == winning_numbers[6]
        total_matches = main_matches + extra_match
        if total_matches in [3, 4]:
            wins.append(f"Rad {index + 1}: Du har {total_matches} + {1 if extra_match else 0} rätt!")
        elif total_matches in [5, 6]:
            wins.append(f"Rad {index + 1}: Du har {total_matches} + {1 if extra_match else 0} rätt!")
        elif total_matches == 7:
            wins.append(f"Rad {index + 1}: Jackpot!")
    return wins

def check_win_keno(user_numbers, winning_numbers, keno_tier):
    wins = []
    tier_wins = {
        2: [2, 3], 3: [2, 3, 4], 4: [2, 3, 4, 5], 5: [3, 4, 5], 
        6: [3, 4, 5, 6], 7: [4, 5, 6, 7], 8: [4, 5, 6, 7, 8], 
        9: [5, 6, 7, 8, 9], 10: [0, 5, 6, 7, 8, 9, 10]
    }

    for index, numbers in enumerate(user_numbers):
        num_matches = len(set(numbers).intersection(winning_numbers))
        if num_matches in tier_wins[keno_tier]:
            wins.append(f"Rad {index + 1}: {num_matches} rätt!")

    return wins

def check_win_jokeri(user_numbers, winning_numbers, _):
    wins = []
    for index, numbers in enumerate(user_numbers):
        num_matches = sum(1 for n, wn in zip(numbers, winning_numbers) if n == wn)
        if num_matches == 7:
            wins.append(f"Rad {index + 1}: Jackpot!")
        elif 4 <= num_matches <= 6:  # För stora vinst
            wins.append(f"Rad {index + 1}: Stort vinst med {num_matches} rätt.")
        elif 2 <= num_matches <= 3:  # För små vinst
            wins.append(f"Rad {index + 1}: Litet vinst med {num_matches} rätt.")
    return wins

if __name__ == "__main__":
    while True:
        game_choice = input("\nVälj ett spel: Lotto (1), Eurojackpot (2), Vikinglotto (3), Keno (4), Jokeri (5): ").strip()
        if game_choice not in ('1', '2', '3', '4', '5'):
            print("Felaktig svar. Välj 1 (Lotto), 2 (Eurojackpot), 3 (Vikinglotto), 4 (Keno), eller 5 (Jokeri).")
            continue

        while True:
            try:
                num_rows = int(input("Hur många rader vill du spela? (1-5): "))
                if num_rows < 1 or num_rows > 5:
                    raise ValueError("Felaktig svar. Välj mängd av rad mellan 1-5.")
                break
            except ValueError as e:
                print(e)
                continue

        if game_choice == "4":  # För keno, fråga för nivå
            while True:
                try:
                    keno_tier = int(input("Välj Keno nivå (2-10): "))
                    if keno_tier < 2 or keno_tier > 10:
                        raise ValueError("Felaktig nivå. Välj nivå mellan 2-10.")
                    break
                except ValueError as e:
                    print(e)
                    continue

        generate_type = input("Vill du välja egna nummer (1) eller generera dem slumpmässigt (2)? ").strip().upper()
        while generate_type not in ('1', '2'):
            print("Felaktig svar. Välj '1' för att välja egna nummer '2' för slumpmässiga nummer.")
            generate_type = input("Vill du välja egna nummer (1) eller generera dem slumpmässigt (2)? ").strip().upper()

        if generate_type == "1":
            if game_choice == "1":  # Lotto
                user_numbers = get_user_numbers_lotto(num_rows)
            elif game_choice == "2":  # Eurojackpot
                user_numbers = get_user_numbers_eurojackpot(num_rows)
            elif game_choice == "3":  # Vikinglotto
                user_numbers = get_user_numbers_vikinglotto(num_rows)
            elif game_choice == "4":  # Keno
                user_numbers = get_user_numbers_keno(num_rows, keno_tier)
            elif game_choice == "5":  # Jokeri
                user_numbers = get_user_numbers_jokeri(num_rows)
        elif generate_type == "2":
            if game_choice == "1":  # Lotto
                user_numbers = generate_user_numbers_lotto(num_rows)
            elif game_choice == "2":  # Eurojackpot
                user_numbers = generate_user_numbers_eurojackpot(num_rows)
            elif game_choice == "3":  # Vikinglotto
                user_numbers = generate_user_numbers_vikinglotto(num_rows)
            elif game_choice == "4":  # Keno
                user_numbers = generate_user_numbers_keno(num_rows, keno_tier)
            elif game_choice == "5":  # Jokeri
                user_numbers = generate_user_numbers_jokeri(num_rows)

        winning_numbers = None
        check_win_func = None
        format_numbers_func = None
        wins = []

        if game_choice == "1":  # Lotto
            winning_numbers = generate_user_numbers_lotto(1)[0]
            check_win_func = check_win_lotto
            format_numbers_func = format_numbers_lotto
            wins = ["3 + 1", "4", "5", "6", "6 + 1", "7"]
        elif game_choice == "2":  # Eurojackpot
            winning_numbers = generate_user_numbers_eurojackpot(1)[0]
            check_win_func = check_win_eurojackpot
            format_numbers_func = format_numbers_eurojackpot
            wins = ["2 + 1", "1 + 2", "3 + 0", "3 + 1", "2 + 2", "4 + 0", "3 + 2", "4 + 1", "4 + 2", "5 + 0", "5 + 1", "5 + 2"]
        elif game_choice == "3":  # Vikinglotto
            winning_numbers = generate_user_numbers_vikinglotto(1)[0]
            check_win_func = check_win_vikinglotto
            format_numbers_func = format_numbers_vikinglotto
            wins = ["3 + 0", "3 + 1", "4 + 0", "4 + 1", "5 + 0", "5 + 1", "6 + 0", "6 + 1"]
        elif game_choice == "4":  # Keno
            winning_numbers = generate_user_numbers_keno(1, keno_tier)[0]
            check_win_func = check_win_keno
            format_numbers_func = format_numbers_keno
            wins = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        elif game_choice == "5":  # Jokeri
            winning_numbers = generate_user_numbers_jokeri(1)[0]
            check_win_func = check_win_jokeri
            format_numbers_func = format_numbers_jokeri
            wins = []

        print("\nDina nummer:")
        for index, row in enumerate(user_numbers):
            formatted_row = format_numbers_func(row)
            print(f"Rad {index + 1}: {formatted_row}")

        print("\nVinnande nummer:")
        formatted_winning_numbers = format_numbers_func(winning_numbers)
        print(formatted_winning_numbers)

        user_wins = check_win_func(user_numbers, winning_numbers, keno_tier if game_choice == "4" else None)
        if user_wins:
            print("\nGrattis! Du har vunnit:")
            for win in user_wins:
                print(win)
        else:
            print("\nInga vinst denhär gången, bättre lycka nästa gång!")

        save_file = input("\nVill du spara dina resultat i ett fil? (ja/nej): ").strip().lower()
        if save_file == "ja":
            file_name = input("Nämn fil: ")
            with open(f"{file_name}.txt", "w") as file:
                file.write(f"Spel: {game_choice}\n")
                file.write(f"Nummer av rad: {num_rows}\n")
                file.write(f"Dina nummer:\n")
                for index, row in enumerate(user_numbers):
                    formatted_row = format_numbers_func(row)
                    file.write(f"Rad {index + 1}: {formatted_row}\n")
                file.write(f"Vinnande nummer: {formatted_winning_numbers}\n")
                file.write("Vinst:\n")
                for win in user_wins:
                    file.write(f"{win}\n")
            print(f"\nResultat sparat i {file_name}.txt")

        play_again = input("\nVill du spela igen? (ja/nej): ").strip().lower()
        if play_again != "ja":
            break