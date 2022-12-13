class MenuInit():
    def __init__(self):
        self.cursor = 0
        self.state = None

        self.input_delay = 200
        self.input_timer = 0

    def increase_cursor_value(self, update_state):
        if self.cursor < 2:
            self.cursor += 1
            self.state = update_state()

    def decrease_cursor_value(self, update_state):
        if self.cursor > 0:
            self.cursor -= 1
            self.state = update_state()

    def process_cursor_movement(self, state_1, state_2, state_3):
        if self.cursor == 0:
            self.state = state_1
        elif self.cursor == 1:
            self.state = state_2
        elif self.cursor == 2:
            self.state = state_3

        return self.state
