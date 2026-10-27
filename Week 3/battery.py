print("How many bars should be charged?")

battery_bars_to_charge = int(input())

charged_battery_bars = 0

while charged_battery_bars < battery_bars_to_charge:
    charged_battery_bars += 1
    print(f"Charging: {'🔋 ' * charged_battery_bars}")

print(f"The battery is fully charged! {charged_battery_bars} 🔋")
