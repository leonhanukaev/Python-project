import pyautogui

def copy_tab_titles():
    # Get the position of the tab switch button
    tab_switch_button_pos = pyautogui.locateOnScreen('tab_switch_button.png')
    if tab_switch_button_pos is None:
        print("Failed to find tab switch button.")
        return

    # Click on the switch tabs button
    tab_switch_button_center = pyautogui.center(tab_switch_button_pos)
    pyautogui.click(tab_switch_button_center)

    # Waiting for the tabs to fully display
    pyautogui.sleep(1)
    
    tab_title_positions = pyautogui.locateAllOnScreen('tab_title.png')
    if tab_title_positions is None:
        print("Failed to find tab titles.")
        return

    # Create or open a file for writing
    with open('tab_titles.txt', 'w') as file:
        for pos in tab_title_positions:
            tab_title_center = pyautogui.center(pos)
            pyautogui.click(tab_title_center)  
            pyautogui.hotkey('ctrl', 'c')  
            tab_title = pyautogui.paste()  
            file.write(tab_title + '\n')  

    print("Tab names successfully copied and saved to file tab_titles.txt.")

copy_tab_titles()
