def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")
    return bmr

def calorie_surplus_calculator():
    try:
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (male/female): ").strip().lower()
        current_weight = float(input("Enter your current weight in kg: "))
        height = float(input("Enter your height in cm: "))
        goal_weight = float(input("Enter your goal weight in kg: "))
        time_f = float(input("Enter the time frame to reach your goal in weeks: "))
        activity = input("Enter your activity level (sedentary, light, moderate, active, very active): ").strip().lower()

        if goal_weight <= current_weight:
            print("Goal weight must be higher than current weight for a surplus calculation.")
            return

        # Constants
        calorie_per_kg = 7700  # Approximate calories per kg of weight gain
        daysper_week = 7
        activity_multipliers = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "very active": 1.9
        }

        # Calculate BMR
        bmr = calculate_bmr(current_weight, height, age, gender)

        # Adjust BMR based on activity level
        if activity in activity_multipliers:
            maintain_calories = bmr * activity_multipliers[activity]
        else:
            print("Invalid activity level. Please choose from sedentary, light, moderate, active, very active.")
            return

        # Calculate total calorie surplus needed
        weight_gain = goal_weight - current_weight
        total_calories_needed = weight_gain * calorie_per_kg

        # Calculate daily caloric surplus needed
        total_days = time_f * daysper_week
        dailycalorie_surplus = total_calories_needed / total_days
        dailycalorie_intake = maintain_calories + dailycalorie_surplus

        print(f"\nTo reach your goal weight of {goal_weight} kg in {time_f} weeks, you need to consume approximately {dailycalorie_intake:.2f} calories daily.")
        
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    calorie_surplus_calculator()