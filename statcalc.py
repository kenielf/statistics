#!/bin/env python
# Kenielf's General Statistics Calculator
import math, statistics, sys
from colorama import Fore, Style
from decimal import *
# Testing
from constants import cheat_str, sanitized_list


# ----- Input and String Sanitization -----#
def str_sanitize(input_str):
    while True:
        try:
            sanitized_list = sorted([Decimal(v) for v in input_str.split()])
            return sanitized_list
        except ValueError:
            raise ValueError(
                f"{Fore.RED}The list of values contains an error, try again.{Style.RESET_ALL}"
            )
            continue


def cli_input():
    while True:
        try:
            input_str = input(
                f"{Fore.CYAN}What are the values?{Style.RESET_ALL}\n",
                f"{Fore.BLUE}Separate them with spaces.{Style.RESET_ALL}\n",
            )
            input_list = str_sanitize(input_str)
            return input_list
        except ValueError:
            continue


def list_format(input_list, size=0):
    if size == 0:
        return input_list
    output_list = []
    format_str = "{:." + str(size) + "f}"
    for dist in range(len(input_list)):
        output_str = format_str.format(input_list[dist])
        output_list.append(output_str)
    return output_list


def dec_format(input_decimal, size=0):
    if size == 0:
        return input_decimal
    output_list = []
    format_str = "{:." + str(size) + "f}"
    return format_str.format(input_decimal)


def rol_string(input_list, input_class):
    rol_list = []
    cur_min, cur_max = 0, 0
    for entry in range(input_class):
        cur_str = ""
        cur_max += int(len(input_list) / input_class)
        for pos in range(cur_min, cur_max):
            cur_str += str(input_list[pos]) + ", "
        rol_list.append(cur_str)
        cur_min = cur_max
    return rol_list


def calc_sum(input_list, size=0):
    if size == 0:
        return sum([Decimal(entry) for entry in input_list])
    return round(sum([Decimal(entry) for entry in input_list]), size)


# ----- Calculator Functions -----#
def calc_central_tendencies(input_list):
    output_mean = Decimal(statistics.mean(input_list))
    output_median = Decimal(statistics.median(input_list))
    output_mode = list(Decimal(v) for v in statistics.multimode(input_list))
    output_amplitude = input_list[-1] - input_list[0]
    return output_mean, output_median, output_mode, output_amplitude


def calc_class_group(input_list):
    class_min = class_max = 0
    output_class_list = []
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
                output_class_list.append(entry)
            else:
                continue
        if output_class_list is not None:
            pass
        else:
            print(f"{Fore.RED}This list is irregular.{Style.RESET_ALL}")
            output_classes = "irregular"
        return output_class_list


def calc_minmax_table(input_list, input_class, input_interval):
    output_min_list, output_max_list = [], []
    min_first, max_last = input_list[0], input_list[-1]
    min_current = max_current = 0
    while min_current == 0:
        min_current, max_current = min_first, Decimal(min_first + input_interval)
        for dist in range(1, input_class + 1):
            output_min_list.append(min_current), output_max_list.append(max_current)
            min_current = max_current
            max_current += input_interval
            if max_current >= (max_last + (input_interval * 2)):
                break
            else:
                continue
        if output_max_list[-1] == input_list[-1]:
            min_current, max_current = output_max_list[-1], (
                output_max_list[-1] + input_interval
            )
            output_min_list.append(min_current), output_max_list.append(max_current)
    return output_min_list, output_max_list


def calc_class_midpoint(input_class, input_min, input_max):
    output_midpoint_list = []
    for dist in range(input_class):
        output_midpoint_list.append((input_max[dist] + input_min[dist]) / 2)
    return output_midpoint_list


def calc_abs_frequency(input_list, input_class, input_min, input_max):
    output_freq_list = []
    for dist in range(input_class):
        current_frequency = 0
        for item in input_list:
            if input_min[dist] <= item < input_max[dist]:
                current_frequency += 1
        output_freq_list.append(current_frequency)
    return output_freq_list


def calc_relative_frequency(input_list, input_class, input_abs_freq_list):
    output_rel_freq_list = []
    for dist in range(input_class):
        rel_frequency = Decimal(input_abs_freq_list[dist] / len(input_list))
        output_rel_freq_list.append(rel_frequency)
    return output_rel_freq_list


def calc_perc_relative_frequency(input_rel_freq_list):
    output_perc_rel_freq_list = []
    perc_rel_freq = 0
    for dist in range(len(input_rel_freq_list)):
        perc_rel_freq = Decimal(input_rel_freq_list[dist]) * 100
        output_perc_rel_freq_list.append(perc_rel_freq)
    return output_perc_rel_freq_list


def calc_accumulated_frequency(input_abs_freq_list, crescent_order=True):
    acc_freq_list = []
    acc_freq = 0
    for dist, entry in enumerate(input_abs_freq_list):
        if dist == 0:
            acc_freq = entry
            acc_freq_list.append(acc_freq)
        else:
            acc_freq += entry
            acc_freq_list.append(acc_freq)
    if crescent_order == True:
        return acc_freq_list
    else:
        return acc_freq_list.reverse()


def calc_perc_accumulated_frequency(input_relative_freq_list):
    perc_acc_freq_list = []
    perc_acc_freq = 0
    for dist, entry in enumerate(input_relative_freq_list):
        if dist == 0:
            perc_acc_freq = Decimal(entry * 100)
            perc_acc_freq_list.append(perc_acc_freq)
        else:
            perc_acc_freq += entry
            perc_acc_freq_list.append(perc_acc_freq)
    perc_acc_freq_list = list(round(entry, 2) for entry in perc_acc_freq_list)
    return perc_acc_freq_list


def calc_fixi(input_midpoint_list, input_abs_freq_list):
    output_fixi_list = []
    fixi_current = 0
    for dist in range(len(input_midpoint_list)):
        fixi_current = Decimal(input_midpoint_list[dist] * input_abs_freq_list[dist])
        output_fixi_list.append(fixi_current)
    return output_fixi_list


def calc_mod_xixbar(input_midpoint_list, input_mean):
    output_xixbar_list = []
    xixbar_current = 0
    for dist in range(len(input_midpoint_list)):
        xixbar_current = Decimal(abs(input_midpoint_list[dist] - input_mean))
        output_xixbar_list.append(xixbar_current)
    return output_xixbar_list


def calc_xixbar_squared(input_mod_xixbar_list):
    output_xixbar_squared_list = []
    xixbar_squared_current = 0
    for dist in range(len(input_mod_xixbar_list)):
        xixbar_squared_current = Decimal(input_mod_xixbar_list[dist] ** 2)
        output_xixbar_squared_list.append(xixbar_squared_current)
    return output_xixbar_squared_list


def calc_freq_mod_xixbar(input_mod_xixbar, input_abs_freq_list):
    output_freq_mod_xixbar_list = []
    freq_mod_xixbar_current = 0
    for dist in range(len(input_mod_xixbar)):
        freq_mod_xixbar_current = Decimal(
            input_mod_xixbar[dist] * input_abs_freq_list[dist]
        )
        output_freq_mod_xixbar_list.append(freq_mod_xixbar_current)
    return output_freq_mod_xixbar_list


def calc_freq_mod_xixbar_squared(input_xixbar_squared_list, input_abs_freq_list):
    output_freq_mod_xixbar_squared_list = []
    freq_mod_xixbar_squared_current = 0
    for dist in range(len(input_xixbar_squared_list)):
        freq_mod_xixbar_squared_current = Decimal(
            input_xixbar_squared_list[dist] * input_abs_freq_list[dist]
        )
        output_freq_mod_xixbar_squared_list.append(freq_mod_xixbar_squared_current)
    return output_freq_mod_xixbar_squared_list


def calc_deviations(
    input_abs_freq_list, input_freq_xixbar_list, input_freq_mod_xixbar_squared_list
):
    output_abs_medium_deviation = Decimal(
        sum(input_freq_xixbar_list) / sum(input_abs_freq_list)
    )
    output_variance = Decimal(
        sum(input_freq_mod_xixbar_squared_list) / sum(input_abs_freq_list)
    )
    output_default_deviation = Decimal(math.sqrt(output_variance))
    return output_abs_medium_deviation, output_variance, output_default_deviation


# ----- Runtime Dependent Functions -----#
def main_table_print(
    input_class,
    input_min,
    input_max,
    input_midpoint_list,
    input_abs_freq_list,
    input_rel_freq_list,
    input_perc_rel_freq_list,
    input_acc_freq_list,
    input_perc_acc_freq_list,
    input_fixi_list,
    input_xixbar_list,
    input_xixbar_squared_list,
    input_freq_xixbar_list,
    input_freq_xixbar_squared_list,
):
    # String Formatting
    input_min = list_format(input_min, 2)
    input_max = list_format(input_max, 2)
    input_midpoint_list = list_format(input_midpoint_list, 2)
    input_abs_freq_list = list_format(input_abs_freq_list)
    input_rel_freq_list = list_format(input_rel_freq_list, 6)
    input_perc_rel_freq_list = list_format(input_perc_rel_freq_list, 2)
    input_acc_freq_list = list_format(input_acc_freq_list)
    input_perc_acc_freq_list = list_format(input_perc_acc_freq_list, 2)
    input_fixi_list = list_format(input_fixi_list)
    input_xixbar_list = list_format(input_xixbar_list, 4)
    input_xixbar_squared_list = list_format(input_xixbar_squared_list, 4)
    input_freq_xixbar_list = list_format(input_freq_xixbar_list, 4)
    input_freq_xixbar_squared_list = list_format(input_freq_xixbar_squared_list, 4)
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
    for entry in range(input_class):
        print(
            "│  %6s ⊢ %6s │ %6s │%3s │%7s │%8s%% │%4s │%8s%% │%7s │%9s │%10s │%10s │%11s │"
            % (
                input_min[entry],
                input_max[entry],
                input_midpoint_list[entry],
                input_abs_freq_list[entry],
                input_rel_freq_list[entry],
                input_perc_rel_freq_list[entry],
                input_acc_freq_list[entry],
                input_perc_acc_freq_list[entry],
                input_fixi_list[entry],
                input_xixbar_list[entry],
                input_xixbar_squared_list[entry],
                input_freq_xixbar_list[entry],
                input_freq_xixbar_squared_list[entry],
            )
        )
    print(
        "├──────────────────┴────────┼────┼─────────┼──────────┼─────┼──────────┼────────┼──────────┼───────────┼───────────┼────────────┤"
    )
    print(
        "│    TOTAL(Σ):              │%3s │%8s │%8s%% │     │          │%7s │          │           │%10s │%11s │"
        % (
            calc_sum(input_abs_freq_list),
            calc_sum(input_rel_freq_list, 2),
            (calc_sum(input_rel_freq_list, 2) * 100),
            calc_sum(input_fixi_list),
            calc_sum(input_freq_xixbar_list),
            calc_sum(input_freq_xixbar_squared_list, 3),
        )
    )
    print(
        "└───────────────────────────┴────┴─────────┴──────────┴─────┴──────────┴────────┴──────────┴───────────┴───────────┴────────────┘"
    )


def auxiliary_table_print(
    input_precision,
    input_rol,
    input_mean,
    input_median,
    input_mode,
    input_amplitude,
    input_class,
    input_interval,
    input_absolute_mean_deviation,
    input_variance,
    input_default_deviation,
):
    print(
        "┌────────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────────┐"
    )
    print(
        "│    [ROL] [COLUMNS: %4s] [INTERVAL: %4s]                  │                                                                  │"
        % (input_class, input_interval)
    )
    print(
        "├────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────┤"
    )
    for entry in range(input_class):
        if entry == 0:
            current_line = f"Precision: [{input_precision}] Decimals"
        elif entry == 1:
            current_line = f"Mean: [{input_mean}]"
        elif entry == 2:
            current_line = f"Median: [{input_median}]"
        elif entry == 3:
            current_line = f"Mode: {[float(v) for v in input_mode]}"
        elif entry == 4:
            current_line = f"Amplitude: [{input_amplitude}]"
        else:
            current_line = ""
        #
        print("│  %-56s  │ %-64s │" % (input_rol[entry], current_line))
    print(
        "├────────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────────┤"
    )
    print(
        "│ Abs. Mean Deviation: %-104s │\n│ Variance: %-115s │\n│ Default Variation: %-106s │"
        % (
            dec_format(input_absolute_mean_deviation, 30),
            dec_format(input_variance, 30),
            dec_format(input_default_deviation, 30),
        )
    )
    print(
        "└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘"
    )


def help_print():
    print(
        f"usage: python3 pystatcalc.py [-h] [-t] [-i <list_string | path to file.html>]\n\n"
        f"optional arguments:\n"
        f"  -h              shows this help message and exits\n"
        f"  -t              forces terminal output (GUI by default)\n"
        f"  -i              direct input, should be a list of values separated by spaces or a .html file\n"
    )


# ----- Runtime Functions -----#
def cli_calculator():
    while True:
        getcontext().prec = 50
        precision = getcontext().prec
        # ---INPUT---#
        # values = cli_input()
        values = str_sanitize(cheat_str)
        # ---CENTRAL TENDENCIES & AMPLITUDE---#
        mean, median, mode, amplitude = calc_central_tendencies(values)
        # ---CLASSES---#
        classes = calc_class_group(values)
        if classes == "irregular":
            break
        else:
            base_class = classes[0]
        chosen_class = classes[0]
        interval = Decimal(amplitude / chosen_class)
        min_list, max_list = calc_minmax_table(values, chosen_class, interval)
        if len(min_list) != chosen_class:
            chosen_class = len(min_list)
        # ---FREQUENCY---#
        midpoints = calc_class_midpoint(chosen_class, min_list, max_list)
        frequencies = calc_abs_frequency(values, chosen_class, min_list, max_list)
        rel_frequencies = calc_relative_frequency(values, chosen_class, frequencies)
        perc_rel_frequencies = calc_perc_relative_frequency(rel_frequencies)
        acc_frequencies = calc_accumulated_frequency(frequencies)
        perc_acc_frequencies = calc_perc_accumulated_frequency(rel_frequencies)
        fixi_list = calc_fixi(midpoints, frequencies)
        xixbar_list = calc_mod_xixbar(midpoints, mean)
        xixbar_squared_list = calc_xixbar_squared(xixbar_list)
        freq_mod_xixbar = calc_freq_mod_xixbar(xixbar_list, frequencies)
        freq_mod_xixbar_squared = calc_freq_mod_xixbar_squared(
            xixbar_squared_list, frequencies
        )
        # ---DISPERSION---#
        abs_mean_deviation, variance, default_deviation = calc_deviations(
            frequencies, xixbar_list, freq_mod_xixbar_squared
        )
        # ---PRINTING---#
        rol = rol_string(values, chosen_class)
        #
        auxiliary_table_print(
            precision,
            rol,
            mean,
            median,
            mode,
            amplitude,
            base_class,
            interval,
            abs_mean_deviation,
            variance,
            default_deviation,
        )
        print("\n")
        main_table_print(
            chosen_class,
            min_list,
            max_list,
            midpoints,
            frequencies,
            rel_frequencies,
            perc_rel_frequencies,
            acc_frequencies,
            perc_acc_frequencies,
            fixi_list,
            xixbar_list,
            xixbar_squared_list,
            freq_mod_xixbar,
            freq_mod_xixbar_squared,
        )
        break


# ----- MAIN -----#
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        if ("-t" in args) == True:
            print("Terminal Output")
            cli_calculator()
        elif ("-h" in args) == True:
            print("No arguments")
            help_print()
        else:
            print("Invalid arguments, please try again.")
            help_print()
    else:
        print("No arguments")
        help_print()


