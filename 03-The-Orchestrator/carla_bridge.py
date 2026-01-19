import carla

class CARLABridge:
    def __init__(self):
        self.client = carla.Client('127.0.0.1', 2000)
        self.client.set_timeout(10.0)
        self.vehicle = None # Assigned when Tesla Model 3 is spawned

    def apply_controls(self, throttle=0.0, steer=0.0, brake=0.0):
        if self.vehicle:
            self.vehicle.apply_control(carla.VehicleControl(throttle=throttle, steer=steer, brake=brake))