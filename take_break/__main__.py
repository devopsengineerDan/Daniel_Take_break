import webbrowser
import time
import os
import re
import click
import six
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt,
                        style_from_dict)
from pyfiglet import figlet_format


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


def confirm():
    questions = [
        {
            'type': 'confirm',
            'name': 'send',
            'message': 'Accept the break?'
        }
    ]
    answers = prompt(questions, style=style)
    return answers

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
            'message': 'Confirm you want to make a break?'
        }
    ]

    answers = prompt(questions, style=style)
    return answers


@click.command()
def main():
    """
    Simple CLI taking break app
    """
    log('This program was started on ' + time.ctime(), "blue")
    log("B r e a k A p p", color="blue", figlet=True)
    log("Welcome break app developed by bonbon", "green")

    res = inPuts()
    if res.get("send", False):
        try:
            num_breaks = int(res.get("breaks"))
            break_duaration = int(res.get("time"))
            breaks = 0
            while (num_breaks > breaks):
                uin = break_duaration
                when_to_stop = abs(int(uin))

                while when_to_stop > 0:
                    m, s = divmod(when_to_stop, 60)
                    h, m = divmod(m, 60)
                    time_left = str(h).zfill(2) + ":" + \
                        str(m).zfill(2) + ":" + str(s).zfill(2)
                    print(time_left + "\r", end="")
                    time.sleep(1)
                    when_to_stop -= 1
                    while when_to_stop == 0:
                        accept = confirm()
                        if accept.get("send", False):
                            log("when done with break hit enter\n", "green")
                            webbrowser.open(
                                "https://www.youtube.com/watch?v=m7Bc3pLyij0",
                                new=0, autoraise=True)
                            break
                        else:
                            break
                num_breaks -= 1
        except Exception as e:
            raise Exception("An error occured: %s" % (e))


if __name__ == '__main__':
    main()
