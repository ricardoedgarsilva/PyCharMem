import npyscreen
import os
import platform

class StartMenu(npyscreen.Form):
    def create(self):
        # Add the title
        self.add(npyscreen.TitleFixedText, name='Welcome to PyCharMem!', rely=1, relx=40, editable=False)

        # Add the menu with four options
        menu = self.add(npyscreen.SelectOne, max_height=4, value=[], name='Select an option', values=['Start measurement', 'Edit configuration file','Exit'],when_value_edited=self.on_select)


    def on_select(self):
        selected_option = self.my_selectone.get_selected_objects()[0]
        print(selected_option)
        match selected_option:
            case 0: 
                pass
            case 1:
                if platform.system() == 'Windows': editor = 'notepad.exe'
                else: editor = 'nano'
                os.system(f'{editor} config.ini')



class PyCharMem(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', StartMenu, name='Main menu')

if __name__ == '__main__':
    app = PyCharMem().run()
