import keyboard
# press a to print rk
keyboard.add_hotkey('1',   lambda: keyboard.write('1111'))
keyboard.add_hotkey('2',   lambda: keyboard.write('2222'))
keyboard.add_hotkey('3',   lambda: keyboard.write('3'))
keyboard.add_hotkey('4',   lambda: keyboard.write('4444'))
  
keyboard.wait('esc')
