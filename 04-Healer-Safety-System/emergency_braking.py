class EmergencyBraking:
    def __init__(self, threshold=5.0):
        self.threshold = threshold

    def evaluate(self, distance):
        # Returns (should_brake: bool, brake_value: float)
        if distance < self.threshold:
            return True, 1.0
        return False, 0.0