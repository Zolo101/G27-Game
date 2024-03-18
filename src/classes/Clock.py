class Clock:
    """ Simple class for handling timings """

    def __init__(self):
        self.time = 0

    def tick(self):
        """ Increments the `time` property by 1."""
        self.time += 1

    def transition(self, frame_duration):
        """
        Checks if `x % frame_duration` is equal to zero,
        where x is `time`.
        """
        return self.time % frame_duration == 0
