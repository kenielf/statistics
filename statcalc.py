#!/bin/env python
# Kenielf's Statistics Calculator
import statistics
import math
from decimal import *
from constants import cheat_str, sanitized_list


# Returns a workable ROL list from a string
def sanitize(input_str):
    while True:
        try:
            sanitized_list = sorted([Decimal(v) for v in input_str.split()])
            return sanitized_list
        except ValueError:
            print("The list of values contains an error, try again.")
            continue


# Returns a workable ROL list from input
def get_input():
    while True:
        try:
            input_str = input("What are the values?\n" "Separate them with spaces.\n")
            input_list = sorted([Decimal(v) for v in input_str.split()])
            return input_list
        except ValueError:
            print("The list of values contains an error, try again.")
            continue


# Returns the mean, median, mode and amplitude in this order respectively
def central_tendencies(input_list):
    local_mean = Decimal(statistics.mean(input_list))
    local_median = Decimal(statistics.median(input_list))
    local_mode = list(Decimal(v) for v in statistics.multimode(input_list))
    local_amplitude = input_list[-1] - input_list[0]
    return local_mean, local_median, local_mode, local_amplitude


def class_group(input_list):
    class_min = class_max = 0
    local_class_list = []
    input_list_length = len(input_list)
    while class_min == 0 and class_max == 0:
        if input_list_length <= 50:
            class_min, class_max = 5, 10
        elif input_list_length <= 100:
            class_min, class_max = 8, 16
        elif input_list_length <= 200:
            class_min, class_max = 10, 20
        elif input_list_length <= 300:
            class_min, class_max = 12, 24
        elif input_list_length <= 500:
            class_min, class_max = 15, 30
        else:
            class_min, class_max = 20, 40
        for entry in range(class_min, class_max + 1):
            if input_list_length % entry == 0:
                local_class_list.append(entry)
            else:
                continue
        if local_class_list is not None:
            pass
        else:
            print(f"This list is irregular.")
            local_class_list = "Irregular"
        return local_class_list


def min_max_table(input_list, class_value, local_interval):
    local_min_list, local_max_list = [], []
    min_first, max_last = input_list[0], input_list[-1]
    min_current = max_current = 0
    while min_current == 0:
        min_current, max_current = min_first, Decimal(min_first + local_interval)
        for entry in range(1, class_value + 1):
            local_min_list.append(min_current), local_max_list.append(max_current)
            min_current = max_current
            max_current += local_interval
            if max_current >= (max_last + (interval * 2)):
                break
            else:
                continue
        if local_max_list[-1] == input_list[-1]:
            min_current, max_current = local_max_list[-1], (
                local_max_list[-1] + interval
            )
            local_min_list.append(min_current), local_max_list.append(max_current)
    return local_min_list, local_max_list


def class_midpoint(class_value, min_list, max_list):
    midpoint_list = []
    for entry in range(class_value):
        midpoint_list.append((max_list[entry] + min_list[entry]) / 2)
    return midpoint_list


def absolute_frequency(input_list, class_value, min_list, max_list):
    local_frequency_list = []
    for entry in range(class_value):
        local_frequency = 0
        for item in input_list:
            if min_list[entry] <= item < max_list[entry]:
                local_frequency += 1
        local_frequency_list.append(local_frequency)
    return local_frequency_list


def relative_frequency(input_list, class_value, absolute_frequency_list):
    relative_frequency_list = []
    for entry in range(class_value):
        local_rel_frequency = Decimal(absolute_frequency_list[entry] / len(input_list))
        relative_frequency_list.append(local_rel_frequency)
    return relative_frequency_list


def perc_relative_frequency(frequency_list):
    new_freq_list = []
    frequency_value = 0
    for entry in range(len(frequency_list)):
        frequency_value = Decimal(frequency_list[entry]) * 100
        new_freq_list.append(frequency_value)
    return new_freq_list


def accumulated_frequency(frequency_list):
    new_freq_list = []
    frequency_value, first = 0, 0
    for i, entry in enumerate(frequency_list):
        if i == 0:
            frequency_value = entry
            new_freq_list.append(entry)
        else:
            frequency_value += entry
            new_freq_list.append(frequency_value)
    return new_freq_list


def perc_accumulated_frequency(perc_relative_frequency_list):
    new_freq_list = []
    frequency_value = 0
    for i, entry in enumerate(perc_relative_frequency_list):
        if i == 0:
            frequency_value = round(entry, 2)
            new_freq_list.append(frequency_value)
        else:
            frequency_value += round(entry, 2)
            new_freq_list.append(frequency_value)
    new_freq_list[-1] = round(new_freq_list[-1], 1)
    return new_freq_list


def fixi(midpoints, frequencies):
    fixi_list = []
    fixi_current = 0
    for i in range(len(midpoints)):
        fixi_current = Decimal(midpoints[i] * frequencies[i])
        fixi_list.append(fixi_current)
    return fixi_list


def mod_xixbar(midpoints, mean):
    xixbar_list = []
    xixbar_current = 0
    for i in range(len(midpoints)):
        xixbar_current = Decimal(abs(midpoints[i] - mean))
        xixbar_list.append(xixbar_current)
    return xixbar_list


def xixbar_squared(mod_xixbar_list):
    xixbar_squared_list = []
    xixbar_squared_current = 0
    for i in range(len(mod_xixbar_list)):
        xixbar_current = Decimal(mod_xixbar_list[i] ** 2)
        xixbar_squared_list.append(xixbar_current)
    return xixbar_squared_list


def frequency_mod_xixbar(mod_xixbar, frequency_list):
    frequency_mod_xixbar_list = []
    frequency_mod_xixbar_current = 0
    for i in range(len(mod_xixbar)):
        frequency_mod_xixbar_current = Decimal(mod_xixbar[i] * frequency_list[i])
        frequency_mod_xixbar_list.append(frequency_mod_xixbar_current)
    return frequency_mod_xixbar_list


def frequency_mod_xixbar_squared(xixbar_squared_list, frequency_list):
    frequency_mod_xixbar_squared_list = []
    frequency_mod_xixbar_squared_current = 0
    for i in range(len(xixbar_squared_list)):
        frequency_mod_xixbar_squared_current = Decimal(
            xixbar_squared_list[i] * frequency_list[i]
        )
        frequency_mod_xixbar_squared_list.append(frequency_mod_xixbar_squared_current)
    return frequency_mod_xixbar_squared_list


def deviations(
    frequency_list, frequency_xixbar_list, frequency_mod_xixbar_squared_list
):
    absolute_medium_deviation = Decimal(
        sum(frequency_xixbar_list) / sum(frequency_list)
    )
    variance = Decimal(sum(frequency_mod_xixbar_squared_list) / sum(frequency_list))
    default_deviation = Decimal(math.sqrt(variance))
    return absolute_medium_deviation, variance, default_deviation


# Sanitizes values to work in fancy_print()
def list_format(entry_list, size=0):
    if size == 0:
        return entry_list
    output_list = []
    format_str = "{:." + str(size) + "f}"
    for entry in range(len(entry_list)):
        string = format_str.format(entry_list[entry])
        output_list.append(string)
    return output_list


def decimal_format(entry_decimal, size=0):
    if size == 0:
        return entry_decimal
    output_str = ""
    format_str = "{:." + str(size) + "f}"
    for entry in range(1):
        string = format_str.format(entry_decimal)
        output_str += string
    return output_str


def sum_calculator(entry, size=0):
    if size == 0:
        return sum([Decimal(v) for v in entry])
    return round(sum([Decimal(v) for v in entry]), size)


def rol_string(input_list, class_value):
    rol_list = []
    cur_min, cur_max = 0, 0
    for i in range(class_value):
        current = ""
        cur_max += (len(input_list) / class_value) 
        for o in range(int(cur_min), int(cur_max)):
            current += str(input_list[o]) + ", "
        rol_list.append(current)
        cur_min = cur_max
    return rol_list

# Prints formatted table
def fancy_print(
    class_value,
    min_list,
    max_list,
    midpoint_list,
    frequency_list,
    relative_frequency_list,
    perc_relative_frequency_list,
    acc_frequency_list,
    perc_acc_frequency_list,
    fixi_values,
    xixbars,
    xixbars_squared,
    frequencies_xixbar,
    frequencies_mod_xixbar_squared_list,
):
    # String Formatting
    min_list = list_format(min_list, 2)
    max_list = list_format(max_list, 2)
    midpoint_list = list_format(midpoint_list, 2)
    frequency_list = list_format(frequency_list)
    relative_frequency_list = list_format(relative_frequency_list, 6)
    percentage_relative_frequency_list = list_format(perc_relative_frequency_list, 2)
    accumulated_frequency_list = list_format(acc_frequency_list)
    perc_accumulated_frequency_list = list_format(perc_acc_frequency_list, 2)
    fixis = list_format(fixi_values)
    xixbar_list = list_format(xixbars, 4)
    xixbar_squared_list = list_format(xixbars_squared, 4)
    frequencies_xixbar_list = list_format(frequencies_xixbar, 4)
    frequencies_mod_xixbar_squared = list_format(frequencies_mod_xixbar_squared_list, 4)
    # Print table
    print(
        "┌──────────────────┬────────┬────┬─────────┬──────────┬─────┬──────────┬────────┬──────────┬───────────┬───────────┬────────────┐"
    )
    print(
        "│      CLASSE      │   Xi   │ Fi │    Fr   │    Fr%   │ Fac │   Fac%   │  FiXi  │ |Xi - x̅| │ (Xi - x̅)² │ F|Xi - x̅| │ F(Xi - x̅)² │"
    )
    print(
        "├──────────────────┼────────┼────┼─────────┼──────────┼─────┼──────────┼────────┼──────────┼───────────┼───────────┼────────────┤"
    )
    for entry in range(class_value):
        print(
            "│ [%6s,%6s[  │ %6s │%3s │%7s │%8s%% │%4s │%8s%% │%7s │%9s │%10s │%10s │%11s │"
            % (
                min_list[entry],
                max_list[entry],
                midpoint_list[entry],
                frequency_list[entry],
                relative_frequency_list[entry],
                percentage_relative_frequency_list[entry],
                accumulated_frequency_list[entry],
                perc_accumulated_frequency_list[entry],
                fixis[entry],
                xixbar_list[entry],
                xixbar_squared_list[entry],
                frequencies_xixbar_list[entry],
                frequencies_mod_xixbar_squared[entry],
            )
        )
    print(
        "├──────────────────┴────────┼────┼─────────┼──────────┼─────┼──────────┼────────┼──────────┼───────────┼───────────┼────────────┤"
    )
    print(
        "│    TOTAL(Σ):              │%3s │%8s │%8s%% │     │          │%7s │          │           │%10s │%11s │"
        % (
            sum_calculator(frequency_list),
            sum_calculator(relative_frequency_list, 2),
            sum_calculator(perc_relative_frequency_list, 1),
            sum_calculator(fixis),
            sum_calculator(frequencies_xixbar_list),
            sum_calculator(frequencies_mod_xixbar_squared, 3)
        )
    )
    print(
        "└───────────────────────────┴────┴─────────┴──────────┴─────┴──────────┴────────┴──────────┴───────────┴───────────┴────────────┘"
    )


def isolated_values_table(
    precision,
    rol,
    mean,
    median,
    mode,
    ampltiude,
    class_value,
    interval,
    absolute_mean_deviation,
    variance,
    default_deviation
):
    print(
        "┌────────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────────┐"
    )
    print(
        "│    [ROL] [COLUMNS: %4s] [INTERVAL: %4s]                  │                                                                  │"
        % (
            class_value,
            interval
        )
    )
    print(
        "├────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────┤"

    )
    for entry in range(class_value):
        if entry == 0:
            current_line = f"Precision: [{precision}] Decimals"
        elif entry == 1:
            current_line = f"Mean: [{mean}]"
        elif entry == 2:
            current_line = f"Median: [{median}]"
        elif entry == 3:
            current_line = f"Mode: {[float(v) for v in mode]}"
        elif entry == 4:
            current_line = f"Amplitude: [{amplitude}]"
        else:
            current_line = ""
        #
        print(
            "│  %-56s  │ %-64s │"
            % (
                (rol[entry]),
                current_line
            )
        )
    print(
        "├────────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────────┤"
    )
    print(
        "│ Abs. Mean Deviation: %-104s │\n│ Variance: %-115s │\n│ Default Variation: %-106s │"
        % (
            decimal_format(absolute_mean_deviation, 30),
            decimal_format(variance, 30),
            decimal_format(default_deviation, 30)
     
        )
    )
    print(
        "└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘"
    )


# MAIN #
if __name__ == "__main__":
    getcontext().prec = 30
    precision = getcontext().prec
    # USE INPUT OR SET TEST STR/LIST #
    #values = get_input()
    values = sanitize(cheat_str)
    #
    mean, median, mode, amplitude = central_tendencies(values)
    class_values = class_group(values)
    chosen_class = class_values[0]
    base_class = chosen_class
    interval = Decimal(amplitude / chosen_class)
    min_list, max_list = min_max_table(values, chosen_class, interval)
    if len(min_list) != chosen_class:
        chosen_class = len(min_list)
    midpoint_list = class_midpoint(chosen_class, min_list, max_list)
    frequencies = absolute_frequency(values, chosen_class, min_list, max_list)
    relative_frequencies = relative_frequency(values, chosen_class, frequencies)
    perc_relative_frequencies = perc_relative_frequency(relative_frequencies)
    accumulated_frequencies = accumulated_frequency(frequencies)
    perc_accumulated_frequencies = perc_accumulated_frequency(perc_relative_frequencies)
    fixi_list = fixi(midpoint_list, frequencies)
    xixbar_list = mod_xixbar(midpoint_list, mean)
    xixbar_squared_list = xixbar_squared(xixbar_list)
    frequencies_mod_xixbar = frequency_mod_xixbar(xixbar_list, frequencies)
    frequencies_mod_xixbar_squared = frequency_mod_xixbar_squared(
        xixbar_squared_list, frequencies
    )
    absolute_mean_deviation, variance, default_deviation = deviations(
        frequencies, xixbar_list, frequencies_mod_xixbar_squared
    )
    #
    rol = rol_string(values, base_class)
    #
    fancy_print(
        chosen_class,
        min_list,
        max_list,
        midpoint_list,
        frequencies,
        relative_frequencies,
        perc_relative_frequencies,
        accumulated_frequencies,
        perc_accumulated_frequencies,
        fixi_list,
        xixbar_list,
        xixbar_squared_list,
        frequencies_mod_xixbar,
        frequencies_mod_xixbar_squared,
    )
    print("\n")
    isolated_values_table(
        precision,
        rol,
        mean,
        median,
        mode,
        amplitude,
        base_class,
        interval,
        absolute_mean_deviation,
        variance,
        default_deviation
    )

