import npyscreen

class MainMenu(npyscreen.NPSApp):
    def main(self):
        options = ["Option 1", "Option 2", "Option 3"]
        self.selection = []
        
        # Create the form
        self.form = npyscreen.Form(name = "Main Menu")
        self.menu = self.form.add(npyscreen.MultiSelect, max_height=-2, values=options)
        
        # Define the functions for each option
        def option1():
            npyscreen.notify_confirm("Option 1 selected", title="Option 1")
            
        def option2():
            npyscreen.notify_confirm("Option 2 selected", title="Option 2")
            
        def option3():
            npyscreen.notify_confirm("Option 3 selected", title="Option 3")
        
        # Define the function to be called on exit
        def on_exit():
            for selection in self.selection:
                if selection == "Option 1":
                    option1()
                elif selection == "Option 2":
                    option2()
                    
                elif selection == "Option 3":
                    option3()
                    
        # Set the function to be called on exit
        self.form.on_exit = on_exit
        
        # Override the h_select() method to handle Enter key press
        def h_select(self, ch):
            super(npyscreen.MultiSelect, self).h_select(ch)
            self.parent.parentApp.switchForm(None)
        
        self.menu.h_select = h_select
        
        # Run the form
        self.form.edit()
        self.selection = self.menu.get_selected_objects()
        
if __name__ == "__main__":
    app = MainMenu()
    app.run()
