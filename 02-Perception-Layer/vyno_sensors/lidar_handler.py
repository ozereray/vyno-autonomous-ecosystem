import numpy as np

class LidarHandler:
    def get_distance(self, data):
        # Parses Lidar point cloud to find the closest object in front
        points = np.frombuffer(data.raw_data, dtype=np.dtype('f4'))
        points = np.reshape(points, (int(points.shape[0] / 4), 4))
        forward_pts = points[points[:, 0] > 0]
        return np.min(forward_pts[:, 0]) if len(forward_pts) > 0 else 100.0