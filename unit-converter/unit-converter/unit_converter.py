import streamlit as st  # type: ignore

# Global Conversion Dictionary
conversions = {
    # Length
    "meter_kilometer": 0.001,
    "kilometer_meter": 1000,
    # Weight
    "gram_kilogram": 0.001,
    "kilogram_gram": 1000,
    # Temperature (Formula-based conversions)
    "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
    "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
    "celsius_kelvin": lambda c: c + 273.15,
    "kelvin_celsius": lambda k: k - 273.15,
    "fahrenheit_kelvin": lambda f: (f - 32) * 5/9 + 273.15,
    "kelvin_fahrenheit": lambda k: (k - 273.15) * 9/5 + 32,
    # Time
    "second_minute": 1/60,
    "minute_second": 60,
    "second_hour": 1/3600,
    "hour_second": 3600,
    "second_day": 1/86400,
    "day_second": 86400,
    # Volume
    "liter_gallon": 0.264172,
    "gallon_liter": 3.78541,
    # Area
    "square_meter_square_kilometer": 0.000001,
    "square_kilometer_square_meter": 1000000,
    # Speed
    "meter_second_kilometer_hour": 3.6,
    "kilometer_hour_meter_second": 1/3.6,
    # Energy
    "joule_calorie": 0.239006,
    "calorie_joule": 4.184,
    # Power
    "watt_horsepower": 0.00134102,
    "horsepower_watt": 745.7,
    # Pressure
    "pascal_bar": 0.00001,
    "bar_pascal": 100000,
    # Electricity (Updated for accuracy)
    "watt_kilowatt": 0.001,  # 1 watt = 0.001 kilowatts
    "kilowatt_watt": 1000,  # 1 kilowatt = 1000 watts
    "volt_ampere": lambda v, a: v * a,  # Power (W) = Voltage (V) × Current (A)
    "ampere_volt": lambda w, v: w / v if v != 0 else "Error: Voltage cannot be zero",
    "watt_volt": lambda w, a: w / a if a != 0 else "Error: Current cannot be zero",
    "volt_watt": lambda v, a: v * a,  # Same as volt_ampere
}

# Extract unique units
unique_units = sorted(set(unit for pair in conversions.keys() for unit in pair.split("_")))

# Streamlit UI
st.title("Unit Converter")

unit_from = st.selectbox("Select unit to convert from:", unique_units)
unit_to = st.selectbox("Select unit to convert to:", unique_units)

value = st.number_input("Enter value:", min_value=0.0, format="%.4f")

# Conversion Logic
def convert_unit(value, from_unit, to_unit):
    key = f"{from_unit}_{to_unit}"
    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return "Conversion not available"

# Perform Conversion
if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.success(f"Converted value: {result}")

