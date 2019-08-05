import webbrowser
import time
import os
import re
import click
import six
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt,
                        style_from_dict)

from pyfiglet import figlet_format

print('This program started on' + time.ctime())


def take_break():
    print('one break comes after two hours\n')
    num_breaks = int(input('how many breaks do you want?: '))
    break_duaration = int(
        input('After how many hours do you need the break?: '))
    breaks = 0
    while (breaks < num_breaks):
        uin = break_duaration
        when_to_stop = abs(int(uin))

        while when_to_stop >= 0:
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + \
                str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left + "\r", end="")
            time.sleep(1)
            when_to_stop -= 1
            while when_to_stop == 0:
                accept = input("accept the break(Y/N): ")
                if accept.upper() == 'Y':
                    print("when done with break hit enter\n")
                    webbrowser.open(
                        "https://www.youtube.com/watch?v=m7Bc3pLyij0",
                        new=0, autoraise=True)
                else:
                    break
    breaks += 1


try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})


def log(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)


class Validator(Validator):
    pattern = r"^([1-9]|1[012])$"

    def validate(self, email):
        if len(email.text):
            if re.match(self.pattern, email.text):
                return True
            else:
                raise ValidationError(
                    message="Invalid email",
                    cursor_position=len(email.text))
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(email.text))


def inPuts():
    questions = [
        {
            'type': 'input',
            'name': 'breaks',
            'message': 'how many breaks do you want?(leave blank to use previous breaks): ',
            'validate': Validator
        },
        {
            'type': 'input',
            'name': 'time',
            'message': 'After how many hours do you need a break?(leave blank to use previous time): ',
            'validate': Validator
        },
        {
            'type': 'confirm',
            'name': 'send',
            'message': 'Do you want to take the break?'
        }
    ]

    answers = prompt(questions, style=style)
    return answers


@click.command()
def main():
    """
    Simple CLI taking break app
    """
    log("BonBreak", color="green", figlet=True)
    log("Welcome break app", "purple")

    res = inPuts()
    if res.get("send", False):
        print('one break comes after two hours\n')
        num_breaks = int(input('how many breaks do you want?: '))
        break_duaration = int(
            input('After how many hours do you need the break?: '))
        breaks = 0
        while (breaks < num_breaks):
            uin = break_duaration
            when_to_stop = abs(int(uin))

            while when_to_stop >= 0:
                m, s = divmod(when_to_stop, 60)
                h, m = divmod(m, 60)
                time_left = str(h).zfill(2) + ":" + \
                    str(m).zfill(2) + ":" + str(s).zfill(2)
                print(time_left + "\r", end="")
                time.sleep(1)
                when_to_stop -= 1
                while when_to_stop == 0:
                    accept = input("accept the break(Y/N): ")
                    if accept.upper() == 'Y':
                        log("when done with break hit enter\n", "green")
                        webbrowser.open(
                            "https://www.youtube.com/watch?v=m7Bc3pLyij0",
                            new=0, autoraise=True)
                    else:
                        break
        breaks += 1
        try:
            response = take_break(res)
        except Exception as e:
            raise Exception("An error occured: %s" % (e))

        if response.status_code == 202:
            log("Mail sent successfully", "blue")
        else:
            log("An error while trying to send", "red")


if __name__ == '__main__':
    main()
