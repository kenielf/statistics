import statistics
import math
from decimal import *
from colorama import Fore, Style


class Table:
    # Initialize all class variables
    rol = None
    total_amplitude = None
    mean, median, mode, multimode = None, None, None, None
    _class, class_value = None, None
    interval = None
    min_list, max_list = None, None
    class_list = None
    class_midpoint = None
    freq, r_freq, rp_freq, a_freq, pa_freq = None, None, None, None, None
    fixi, mx_mean, mx_mean_s, fmx_mean, fmx_mean_s = None, None, None, None, None
    am_deviation, variance, d_deviation = None, None, None
    precision = getcontext().prec

    def run(self):
        # Total Amplitude
        self.total_amplitude = self.rol[-1] - self.rol[0]
        # Central Tendencies
        self.mean = statistics.mean(self.rol)
        self.median = statistics.median(self.rol)
        if len(statistics.multimode(self.rol)) > 1:
            self.mode = statistics.multimode(self.rol)
        else:
            self.mode = statistics.mode(self.rol)
        # Building Classes
        class_min, class_max = 0, 0
        o_class_list = []
        input_len = len(self.rol)
        while class_min == 0 and class_max == 0:
            if input_len <= 50:
                class_min, class_max = 5, 10
            elif input_len <= 100:
                class_min, class_max = 8, 16
            elif input_len <= 200:
                class_min, class_max = 10, 20
            elif input_len <= 300:
                class_min, class_max = 12, 24
            elif input_len <= 500:
                class_min, class_max = 15, 30
            else:
                class_min, class_max = 20, 40
            for integer in range(class_min, class_max + 1):
                if input_len % integer == 0:
                    o_class_list.append(integer)
            if len(o_class_list) != 0:
                self._class = o_class_list
            else:
                self._class = "irregular"
                break
        if self._class != "irregular":

            self.class_value = self._class[0]
        # Interval
        self.interval = Decimal(self.total_amplitude / self.class_value)
        # Min and Max Lists
        o_min_list, o_max_list = [], []
        min_first, max_last = self.rol[0], self.rol[-1]
        min_current = 0
        while min_current == 0:
            min_current, max_current = min_first, Decimal(min_first + self.interval)
            for dist in range(1, self.class_value + 1):
                o_min_list.append(min_current), o_max_list.append(max_current)
                min_current = max_current
                max_current += self.interval
                if max_current >= (max_last + (self.interval * 2)):
                    break
                else:
                    continue
            if o_max_list[-1] == self.rol[-1]:
                min_current, max_current = o_max_list[-1], (
                        o_max_list[-1] + self.interval
                )
                o_min_list.append(min_current), o_max_list.append(max_current)
        self.min_list, self.max_list = o_min_list, o_max_list
        # Formatted Class List
        of_class_list = []
        for dist in range(self.class_value + 1):
            cf_class = str(f"{self.min_list[dist]} ⊢ {self.max_list[dist]}")
            of_class_list.append(cf_class)
        self.class_list = of_class_list
        # Calculating class midpoint
        o_midpoint_list = []
        for dist in range(self.class_value + 1):
            o_midpoint_list.append((self.max_list[dist] + self.min_list[dist]) / 2)
        self.class_midpoint = o_midpoint_list
        # Abs Frequency
        o_freq_list = []
        for dist in range(self.class_value + 1):
            c_freq = 0
            for item in self.rol:
                if self.min_list[dist] <= item < self.max_list[dist]:
                    c_freq += 1
            o_freq_list.append(c_freq)
        self.freq = o_freq_list
        # Rel Frequency
        or_freq = []
        for dist in range(len(self.freq)):
            cr_freq = Decimal(self.freq[dist] / len(self.rol))
            or_freq.append(cr_freq)
        self.r_freq = or_freq
        # Rel Percentage Frequency
        opr_freq = []
        for dist in range(len(self.freq)):
            cpr_freq = Decimal(self.r_freq[dist] * 100)
            opr_freq.append(cpr_freq)
        self.rp_freq = opr_freq
        # Accumulated Frequency
        oa_freq = []
        ca_freq = 0
        for dist, entry in enumerate(self.freq):
            if dist == 0:
                ca_freq = entry
                oa_freq.append(ca_freq)
            else:
                ca_freq += entry
                oa_freq.append(ca_freq)
        self.a_freq = oa_freq
        # Percentage Accumulated Frequency
        opa_freq = []
        cpa_freq = 0
        for dist, entry in enumerate(self.r_freq):
            if dist == 0:
                cpa_freq = entry * 100
                opa_freq.append(cpa_freq)
            else:
                cpa_freq += entry * 100
                opa_freq.append(cpa_freq)
        opa_freq = list(round(entry, 9) for entry in opa_freq)
        opa_freq = list(str(str(v) + "%") for v in opa_freq)
        self.pa_freq = opa_freq
        # FiXi
        o_fixi = []
        for dist in range(len(self.class_midpoint)):
            c_fixi = Decimal(self.class_midpoint[dist] * self.freq[dist])
            o_fixi.append(c_fixi)
        self.fixi = o_fixi
        # Modular X Mean
        omx_mean = []
        for dist in range(len(self.class_midpoint)):
            cmx_mean = Decimal(abs(self.class_midpoint[dist] - self.mean))
            omx_mean.append(cmx_mean)
        self.mx_mean = omx_mean
        # X Mean Squared
        omx_mean_s = []
        for dist in range(len(self.mx_mean)):
            cmx_mean_s = Decimal(self.mx_mean[dist] ** 2)
            omx_mean_s.append(cmx_mean_s)
        self.mx_mean_s = omx_mean_s
        # Frequency by X mean
        ofmx_mean = []
        for dist in range(len(self.mx_mean)):
            cfmx_mean = Decimal(self.mx_mean[dist] * self.freq[dist])
            ofmx_mean.append(cfmx_mean)
        self.fmx_mean = ofmx_mean
        # Frequency by X mean squared
        ofmx_mean_s = []
        for dist in range(len(self.mx_mean_s)):
            cfmx_mean_s = Decimal(self.mx_mean_s[dist] * self.freq[dist])
            ofmx_mean_s.append(cfmx_mean_s)
        self.fmx_mean_s = ofmx_mean_s
        # Deviation
        self.am_deviation = Decimal(sum(self.fmx_mean) / sum(self.freq))
        self.variance = Decimal(sum(self.fmx_mean_s) / sum(self.freq))
        self.d_deviation = Decimal(math.sqrt(self.variance))

    # Should only be used by developers, to verify values
    def print_debug(self):
        spr = Fore.LIGHTRED_EX
        spc = Fore.LIGHTCYAN_EX
        sra = Style.RESET_ALL
        print(f"{spc}Debugger...{sra}")
        print(f"{spr}ROL: {sra}{', '.join(str(v) for v in self.rol)}")
        print(f"{spr}Total Amplitude: {sra}{self.total_amplitude}")
        print(f"{spr}Mean: {sra}{self.mean}")
        print(f"{spr}Median: {sra}{self.median}")
        print(f"{spr}Mode: {sra}{self.multimode if self.mode == 0 else self.mode}")
        print(f"{spc}Mode Type: {sra}{'Multimode' if self.mode == 0 else 'Regular Mode'}")
        print(f"{spr}Possible Classes: {sra}{self._class}")
        print(f"{spr}Chosen Class: {sra}{self.class_value}")
        print(f"{spr}Interval: {sra}{self.interval}")
        print(f"{spr}Min List: {sra}{', '.join(str(v) for v in self.min_list)}")
        print(f"{spr}Max List: {sra}{', '.join(str(v) for v in self.max_list)}")
        print(f"{spr}Class List: {sra}{', '.join(str(v) for v in self.class_list)}")
        print(f"{spr}Class Midpoint: {sra}{', '.join(str(v) for v in self.class_midpoint)}")
        print(f"{spr}Frequencies: {sra}{', '.join(str(v) for v in self.freq)}")
        print(f"{spr}Relative Frequencies: {sra}{', '.join(str(round(v, 10)) for v in self.r_freq)}")
        print(f"{spc}Sum of Relative Frequencies: {sra}{str(round(sum(self.r_freq), 10))}")
        print(f"{spr}Accumulated Frequencies: {sra}{', '.join(str(round(v, 10)) for v in self.a_freq)}")
        print(f"{spr}Percentage Acc Frequencies: {sra}{', '.join(self.pa_freq)}")
        print(f"{spr}FiXi: {sra}{', '.join(str(v) for v in self.fixi)}")
        print(f"{spr}|Xi - X̄|: {sra}{', '.join(str(y) for y in list(round(v, 10) for v in self.mx_mean))}")
        print(f"{spc}𝚺|Xi - X̄|: {sum(list(round(v, 10) for v in self.mx_mean))}")
        print(f"{spr}(Xi - X̄)²: {sra}{', '.join(str(y) for y in list(round(v, 10) for v in self.mx_mean_s))}")
        print(f"{spc}𝚺(Xi - X̄)²: {sum(list(round(v, 10) for v in self.mx_mean_s))}")
        print(f"{spr}Fi * |Xi - X̄|: {sra}{', '.join(str(y) for y in list(round(v, 10) for v in self.fmx_mean))}")
        print(f"{spc}𝚺(Fi * |Xi - X̄|): {sum(list(round(v, 10) for v in self.fmx_mean))}")
        print(f"{spr}Fi * (Xi - X̄)²: {sra}{', '.join(str(y) for y in list(round(v, 10) for v in self.fmx_mean_s))}")
        print(f"{spc}𝚺(Fi * (Xi - X̄)²): {sum(list(round(v, 10) for v in self.fmx_mean_s))}")
