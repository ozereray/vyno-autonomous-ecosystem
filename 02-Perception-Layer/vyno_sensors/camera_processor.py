import numpy as np
import cv2

class CameraProcessor:
    def process_frame(self, image):
        # Converts raw CARLA buffer to RGB
        i = np.array(image.raw_data)
        i2 = i.reshape((image.height, image.width, 4))
        return i2[:, :, :3] # Returns RGB