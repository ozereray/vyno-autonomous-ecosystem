from carla_bridge import CARLABridge

class VYNO_Swarm_Orchestrator:
    def __init__(self):
        self.carla = CARLABridge()
        self.is_running = True

    def run(self):
        print("VYNO Swarm AI Devreye Girdi...")
        try:
            while self.is_running:
                # 1. Verileri al
                data = self.carla.get_sensor_data()
                
                # 2. DÜZELTME: carla_bridge.py ile uyumlu çağrı
                self.carla.apply_controls(throttle=0.4, steer=0.0)
                
                # Hızı ekrana bas
                print(f"[SWARM] Hiz: {data.get('speed', 0):.1f} | Durum: Aktif")
        except KeyboardInterrupt:
            self.is_running = False
            print("Sistem kapatiliyor...")

if __name__ == "__main__":
    orchestrator = VYNO_Swarm_Orchestrator()
    orchestrator.run()