# This should not be run, it just contains the main codebase
import re
from calculator import *
from decimal import Decimal
from colorama import Fore, Style
import PySimpleGUI as Sg



def help_print():
    print(
        f"Invalid Options...",
        f"Usage: python3 pystatcalc.py [-h] [-t] [-g] [--help] [--terminal] [--graphical]\r\n",
        f"optional arguments:",
        f"  -h              shows this help message and exits",
        f"  -t              forces terminal output (GUI by default)",
        f"  -g              forces graphpical interface",
        f"  --help          same as -h",
        f"  --terminal      same as -t",
        f"  --graphical     same as -g",
        sep="\r\n"
    )


def input_validation(input_string: str):
    regex_p = r"([-+][0-9.]*|[0-9]+[.][0-9]+|[0-9]+)"
    f_list = sorted(Decimal(v) for v in re.findall(regex_p, input_string))
    if len(f_list) > 1:
        return f_list
    else:
        raise ValueError


class Interface:
    def __init__(self):
        self.table = Table()

    @staticmethod
    def l_format(input_list, size=0):
        if size == 0:
            return input_list
        output_list = []
        format_str = "{:." + str(size) + "f}"
        for dist in range(len(input_list)):
            output_str = format_str.format(input_list[dist])
            output_list.append(output_str)
        return output_list

    @staticmethod
    def d_format(input_decimal, size=0):
        if size == 0:
            return input_decimal
        format_str = "{:." + str(size) + "f}"
        return format_str.format(input_decimal)

    @staticmethod
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


class Terminal(Interface):
    def run(self):
        self.input_window()
        self.table.run()
        self.central_tendency_window()
        if self.table.class_value != "irregular":
            self.gen_information_window()
            self.reg_table_window()
        else:
            print("Class Value is Irregular, cannot proceed farther.")

    def input_window(self):
        # Input
        while True:
            try:
                name = input(f"What are the values?\r\n")
                self.table.rol = input_validation(name)
                break
            except ValueError:
                print(f"List is Invalid.\r\nPlease input a valid list.")
                continue
        print(
            f"\r\nYour formatted input is:\r\n"
            f"{', '.join(str(v) for v in self.table.rol)}"
        )

    def central_tendency_window(self):
        ctw_header = str('┌' + '─' * 126 + '┐')
        ctw_header_c = str('│' + " {:<124} ".format("Central Tendency Table")  + '│')
        ctw_separator = str('├' + '─' * 126 + '┤')
        ctw_content_a = str('│' + " {:<124} ".format("Mean:   %s" % (str(self.table.mean))) + '│')
        ctw_content_b = str('│' + " {:<124} ".format("Median: %s" % (str(self.table.median))) + '│')
        ctw_content_c = str('│' + " {:<124} ".format("Mode:   %s" % (str(
            self.table.mode if self.table.multimode is None else self.table.multimode
        ))) + '│')
        ctw_closer = str('└' + '─' * 126 + '┘')
        print(
            ctw_header, ctw_header_c, ctw_separator, ctw_content_a, ctw_content_b, ctw_content_c, ctw_closer,
            sep='\r\n', end="\r\n"
        )

    def gen_information_window(self):
        rol = self.rol_string(self.table.rol, self.table.class_value)
        giw_content_l = [
            "Precision:    {} Decimals".format(str(self.table.precision)),
            "Chosen Class: {}".format(str(self.table.class_value)),
            "Amplitude:    {}".format(str(self.table.total_amplitude)),
            "Absolute Mean Deviation: {:.15}".format(str(self.table.am_deviation)),
            "Variance:     {:.15}".format(str(self.table.variance)),
            "Default Deviation: {:.15}".format(str(self.table.d_deviation)),
        ]
        dist = (len(rol) - len(giw_content_l))
        if dist > 0:
            for i in range(dist):
                giw_content_l.append("")
        else:
            for i in range(abs(dist)):
                rol.append("")
        giw_header = str('┌' + '─' * 62 + '┬' + '─' * 63 + '┐')
        giw_header_c = str('│' + " {:<60} ".format(f"ROL [{self.table.class_value}l] - Interval: [{self.table.interval}]") + '│'
                           + " {:<61} ".format("General Information") + '│')
        giw_separator = str('├' + '─' * 62 + '┼' + '─' * 63 + '┤')
        giw_closer = str('└' + '─' * 62 + '┴' + '─' * 63 + '┘')
        print(
            giw_header, giw_header_c, giw_separator,
            sep='\r\n', end="\r\n"
        )
        for o in range(len(rol)):
            print(str('│' + "  {0:<59} ".format(rol[o]) + "│" + " {0:<61} ".format(giw_content_l[o]) + '│'))
        print(giw_closer)

    def reg_table_window(self):
        rt_header = str('┌'
                        + '─' * 17 + '┬'
                        + '─' * 6 + '┬'
                        + '─' * 5 + '┬'
                        + '─' * 8 + '┬'
                        + '─' * 9 + '┬'
                        + '─' * 6 + '┬'
                        + '─' * 7 + '┬'
                        + '─' * 8 + '┬'
                        + '─' * 11 + '┬'
                        + '─' * 12 + '┬'
                        + '─' * 13 + '┬'
                        + '─' * 13
                        + '┐')
        rt_header_c = str('│'
                          + "{:^17}".format("   CLASSES   ")  + '│'
                          + "{:<6}".format(" Xi ")  + '│'
                          + "{:<5}".format(" Fi ")  + '│'
                          + "{:<8}".format(" Fr ")  + '│'
                          + "{:<9}".format(" Fr% ")  + '│'
                          + "{:<6}".format(" Fac ")  + '│'
                          + "{:<7}".format(" Fac% ")  + '│'
                          + "{:<8}".format(" FiXi ")  + '│'
                          + "{:<11}".format(" |Xi - X| ")  + '│'
                          + "{:<12}".format(" (Xi - X)^2")  + '│'
                          + "{:<13}".format(" Fi|Xi - X|")  + '│'
                          + "{:<13}".format(" Fi(Xi - X)^2")  + '│')
        rt_separator = str('├'
                           + '─' * 17 + '┼'
                           + '─' * 6 + '┼'
                           + '─' * 5 + '┼'
                           + '─' * 8 + '┼'
                           + '─' * 9 + '┼'
                           + '─' * 6 + '┼'
                           + '─' * 7 + '┼'
                           + '─' * 8 + '┼'
                           + '─' * 11 + '┼'
                           + '─' * 12 + '┼'
                           + '─' * 13 + '┼'
                           + '─' * 13
                           + '┤')
        rt_closer = str('└'
                        + '─' * 17 + '┴'
                        + '─' * 6 + '┴'
                        + '─' * 5 + '┴'
                        + '─' * 8 + '┴'
                        + '─' * 9 + '┴'
                        + '─' * 6 + '┴'
                        + '─' * 7 + '┴'
                        + '─' * 8 + '┴'
                        + '─' * 11 + '┴'
                        + '─' * 12 + '┴'
                        + '─' * 13 + '┴'
                        + '─' * 13
                        + '┘')
        print(rt_header, rt_header_c, rt_separator, sep="\r\n")
        for i in range(len(self.table.freq)):
            print('│',
                  "{:^17}".format(self.table.class_list[i]) + '│',
                  "{:^6}".format(self.table.class_midpoint[i]) + '│',
                  "{:^5}".format(self.table.freq[i]) + '│',
                  "{:^8}".format(self.d_format(self.table.r_freq[i], 6)) + '│',
                  "{:^9}".format("{:.5}".format(self.table.rp_freq[i]) + "%") + '│',
                  "{:^6}".format(self.table.a_freq[i]) + '│',
                  "{:^7}".format("{:.5}".format(self.table.pa_freq[i] + "%")) + '│',
                  "{:^8}".format("{:.6}".format(self.table.fixi[i])) + '│',
                  "{:^11}".format("{:.6}".format(self.table.mx_mean[i])) + '│',
                  "{:^12}".format("{:.6}".format(self.table.mx_mean_s[i])) + '│',
                  "{:^13}".format("{:.6}".format(self.table.fmx_mean[i])) + '│',
                  "{:^13}".format("{:.6}".format(self.table.fmx_mean_s[i])) + '│',
                  sep="")
        # total
        print(rt_separator, "\r\n", '│',
              "{:^17}".format(f" Total :")  + '│',
              "{:^6}".format("-") + '│',
              "{:^5}".format(sum(self.table.freq)) + '│',
              "{:^8}".format(self.d_format(sum(self.table.r_freq), 6)) + '│',
              "{:^9}".format(str(round(sum(Decimal(i) for i in self.table.rp_freq), 2)) + "%") + '│',
              "{:^6}".format("-") + '│',
              "{:^7}".format("-") + '│',
              "{:^8}".format(sum(self.table.fixi)) + '│',
              "{:^11}".format("-") + '│',
              "{:^12}".format("-") + '│',
              "{:^13}".format("{:.8}".format(sum(self.table.fmx_mean))) + '│',
              "{:^13}".format("{:.8}".format(sum(self.table.fmx_mean_s))) + '│',
              "\r\n", rt_closer, "\r\n", sep="")


class Graphical(Interface):
    def __init__(self):
        super().__init__()
        Sg.theme("dark grey 9")
        self.app_name = "StatCalc"
        self.size_l, self.size_r, self.size_t, self.size_b = 800, 0, 0, 0
        self.menubar = [
            ["File", ("Run", "Export", "Import", "Close")],
            ["About", ("License", "About StatCalc")]
        ]
        self.stop = False
        self.rc_main, self.rc_alt = "grey30", "grey10"
        self.input = []
        self.ct_header, self.ct_content = [], []
        self.rol_header, self.rol_content = [], []
        self.gi_header, self.gi_content = [], []
        self.rt_header, self.rt_content = [], []

    def run(self):
        while True:
            if self.stop is not True:
                self.input_window()
            else:
                break

    def main_loop(self, window):
        while True:
            event, values = window.read()
            if event == Sg.WINDOW_CLOSED or event == "Close":
                self.stop = True
                break
            elif event == "Run":
                if values["-INPUT-"] != "":
                    try:
                        self.input = input_validation(values["-INPUT-"])
                        window["-FEED-"].update("Your input has {} entries. Proceeding".format(len(self.input)))
                    except ValueError:
                        window["-FEED-"].update("Invalid values, try again.")
                else:
                    window["-FEED-"].update("Input cannot be empty, try again.")
                if len(self.input) != 0:
                    self.table.rol = self.input
                    self.table.run()
                    if self.stop is not True and self.table.class_value == "irregular":
                        window.close()
                        self.central_tendency_window()
                    elif self.stop is not True:
                        window.close()
                        self.regular_table_window()
                elif len(self.input) == 0:
                    continue

    def central_tendency_content(self):
        self.ct_header, self.ct_content = [], []
        self.ct_header = [str(" " * 30 + "Central Tendency Table" + " " * 30)]
        self.ct_content = [
            [str("Mean:" + " " * 10 + "{:.8}").format(self.table.mean)],
            [str("Median:" + " " * 8 + "{:.8}").format(self.table.median)],
            [str("Mode:" + " " * 10 + "{:.8}").format(
                self.table.multimode if self.table.mode == 0 else self.table.mode
            )],
        ]
        return Sg.Table(
            headings=self.ct_header,
            values=self.ct_content,
            def_col_width=20,
            max_col_width=50,
            visible=True,
            num_rows=len(self.ct_content),
            background_color=self.rc_main,
            alternating_row_color=self.rc_alt,
            auto_size_columns=True,
            hide_vertical_scroll=True,
            justification="left",
            key="-CT_TABLE-"
        )

    def rol_gen(self):
        self.rol_header, self.rol_content = [], []
        self.rol_header = ["Rol [{}l] - Interval: [{}]".format(self.table.class_value, self.table.interval)]
        for i in range(len(self.rol_string(self.table.rol, self.table.class_value))):
            self.rol_content.append([self.rol_string(self.table.rol, self.table.class_value)[i]])

    def general_info_gen(self):
        self.gi_header, self.gi_content = [], []
        self.rol_gen()
        self.gi_header = ["   General Information   "]
        self.gi_content = [
            ["Precision:    {} Decimals".format(self.table.precision)],
            ["Chosen Class: {}".format(self.table.class_value)],
            ["Amplitude:    {}".format(self.table.total_amplitude)],
            [str("Mean:" + " " * 10 + "{:.8}").format(self.table.mean)],
            [str("Median:" + " " * 8 + "{:.8}").format(self.table.median)],
            [str("Mode:" + " " * 10 + "{:.8}").format(
                self.table.multimode if self.table.mode == 0 else self.table.mode
            )],
            ["Absolute Mean Deviation: {:.15}".format(self.table.am_deviation)],
            ["Variance:     {:.15}".format(self.table.variance)],
            ["Default Deviation: {:.15}".format(self.table.d_deviation)]
        ]
        dist = (len(self.rol_content) - len(self.gi_content))
        if dist > 0:
            for i in range((len(self.rol_content) - len(self.rol_content))):
                self.gi_content.append(" ")
        else:
            for i in range((len(self.gi_content) - len(self.rol_content))):
                self.rol_content.append(" ")
        return [Sg.Table(
            headings=self.rol_header,
            values=self.rol_content,
            def_col_width=20,
            max_col_width=50,
            visible=True,
            num_rows=len(self.rol_content),
            background_color=self.rc_main,
            alternating_row_color=self.rc_alt,
            auto_size_columns=True,
            hide_vertical_scroll=True,
            justification="left",
            key="-ROL_TABLE-"
        ), Sg.Table(
            headings=self.gi_header,
            values=self.gi_content,
            def_col_width=20,
            max_col_width=50,
            visible=True,
            num_rows=len(self.gi_content),
            background_color=self.rc_main,
            alternating_row_color=self.rc_alt,
            auto_size_columns=True,
            hide_vertical_scroll=True,
            justification="left",
            key="-GI_TABLE-"
        )]

    def regular_table_gen(self):
        self.rt_header, self.rt_content = [], []
        self.rt_header = [
            "{:^17}".format("   CLASSES   "),
            "{:^6}".format(" Xi "),
            "{:^5}".format(" Fi "),
            "{:^8}".format(" Fᵣ "),
            "{:^9}".format(" Fᵣ% "),
            "{:^6}".format(" Fac "),
            "{:^7}".format(" Fac% "),
            "{:^8}".format(" FiXi "),
            "{:^12}".format(" |Xi- X| "),
            "{:^13}".format(" (Xi- X)² "),
            "{:^14}".format(" Fi|Xi- X| "),
            "{:^14}".format(" Fi(Xi- X)² "),
        ]
        if len(self.rt_content) == 0:
            for i in range(len(self.table.freq)):
                tmp_l = ["{:^17}".format(self.table.class_list[i]), "{:^6}".format(self.table.class_midpoint[i]),
                         "{:^5}".format(self.table.freq[i]), "{:^8}".format(self.d_format(self.table.r_freq[i], 6)),
                         str("{:.5}".format(self.table.rp_freq[i]) + "%"), "{:^6}".format(self.table.a_freq[i]),
                         "{:^7}".format("{:.5}".format(self.table.pa_freq[i] + "%")),
                         "{:^8}".format("{:.6}".format(self.table.fixi[i])),
                         "{:^11}".format("{:.6}".format(self.table.mx_mean[i])),
                         "{:^12}".format("{:.6}".format(self.table.mx_mean_s[i])),
                         "{:^13}".format("{:.6}".format(self.table.fmx_mean[i])),
                         "{:^13}".format("{:.6}".format(self.table.fmx_mean_s[i]))]
                self.rt_content.append(tmp_l)
            self.rt_content.append([
                "{:^17}".format(f" Total: "),
                "{:^6}".format("-"),
                "{:^5}".format(sum(self.table.freq)),
                "{:^8}".format(self.d_format(sum(self.table.r_freq), 6)),
                "{:^9}".format(str(round(sum(Decimal(i) for i in self.table.rp_freq), 2)) + "%"),
                "{:^6}".format("-"),
                "{:^7}".format("-"),
                "{:^8}".format(sum(self.table.fixi)),
                "{:^11}".format("-"),
                "{:^12}".format("-"),
                "{:^13}".format("{:.8}".format(sum(self.table.fmx_mean))),
                "{:^13}".format("{:.8}".format(sum(self.table.fmx_mean_s))),
            ])
        return Sg.Table(
            headings=self.rt_header,
            values=self.rt_content,
            def_col_width=20,
            max_col_width=50,
            visible=True,
            num_rows=len(self.rt_content),
            background_color=self.rc_main,
            alternating_row_color=self.rc_alt,
            auto_size_columns=True,
            hide_vertical_scroll=True,
            justification="left",
            key="-REGULAR_TABLE-"
        )

    def layout_factory(self, input_w=False, table_s=False, table_f=False, about=False, app_license=False):
        if input_w:
            return [
                [Sg.Menu(self.menubar)],
                [Sg.Text("Insert the Values:")],
                [Sg.Input(key="-INPUT-", size=(100, 3)),
                 Sg.Button("Run"), Sg.Button("Import"), Sg.Button("Export"), Sg.Button("Close")],
                [Sg.Text(size=(130, 1), key="-FEED-", justification="c")],
                [Sg.Text(size=(130, 1), key="-BLANK-")],
            ]
        elif table_s:
            return [
                [Sg.Menu(self.menubar)],
                [Sg.Text("Insert the Values:")],
                [Sg.Input(key="-INPUT-", size=(100, 3)),
                 Sg.Button("Run"), Sg.Button("Import"), Sg.Button("Export"), Sg.Button("Close")],
                [Sg.Text(size=(130, 1), key="-FEED-", justification="c")],
                [Sg.Text(size=(130, 1), key="-BLANK-")],
                [self.central_tendency_content()],
                [Sg.Text(size=(130, 1), key="-CT_FEED-", justification="c")],
            ]
        elif table_f:
            left_col_l = [
                [self.general_info_gen()[0]],
                [Sg.Text(size=(30, 1), key="-BLANK2-")]
            ]
            right_col_l = [
                [self.general_info_gen()[1]],
                [Sg.Text(size=(30, 1), key="-GI_FEED-", justification="c")],

            ]
            return [
                [Sg.Menu(self.menubar)],
                [Sg.Text("Insert the Values:")],
                [Sg.Input(key="-INPUT-", size=(100, 3)),
                 Sg.Button("Run"), Sg.Button("Import"), Sg.Button("Export"), Sg.Button("Close")],
                [Sg.Text(size=(130, 1), key="-FEED-", justification="c")],
                [Sg.Column(left_col_l, element_justification="c"), Sg.Column(right_col_l, element_justification="l")],
                [self.regular_table_gen()],
                [Sg.Text(size=(130, 1), key="-RT_FEED-", justification="c")],
            ]

    def input_window(self):
        input_layout = self.layout_factory(input_w=True)
        input_window = Sg.Window(self.app_name, input_layout, element_justification="c")
        self.main_loop(input_window)
        input_window.Close()

    def central_tendency_window(self):
        ct_layout = self.layout_factory(table_s=True)
        ct_window = Sg.Window(self.app_name, ct_layout, element_justification="c")
        self.main_loop(ct_window)
        ct_window.Close()

    def regular_table_window(self):
        rt_layout = self.layout_factory(table_f=True)
        rt_window = Sg.Window(self.app_name, rt_layout, element_justification="c")
        self.main_loop(rt_window)
        rt_window.Close()
