def on_button_pressed_a():
    basic.show_string("SERVO TIME ")
    basic.pause(500)
    basic.show_number(0)
    servos.P0.set_angle(0)
    basic.pause(500)
    basic.show_number(90)
    servos.P0.set_angle(90)
    basic.pause(500)
    basic.show_number(180)
    servos.P0.set_angle(180)
    basic.pause(500)
    servos.P0.stop()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.pause(500)
    basic.pause(500)
    basic.show_number(180)
    servos.P0.set_angle(180)
    basic.pause(500)
    basic.show_number(90)
    servos.P0.set_angle(90)
    basic.pause(500)
    basic.show_number(0)
    servos.P0.set_angle(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HEART)
basic.show_string("SERVO TIME", 65)