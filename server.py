class Server:
    def __init__(self):
        self.cpu_usage = 0
        self.memory_usage = 0
        self.disk_usage = 0
        self.sdn_controller = None  # Placeholder for SDN controller integration

    def set_sdn_controller(self, controller):
        self.sdn_controller = controller
        print("SDN Controller connected to the server.")

    def monitor_performance(self, cpu_usage, memory_usage, disk_usage):
        print("Monitoring server performance...")
        # Set server performance metrics based on user input
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.disk_usage = disk_usage
        print(f"CPU Usage: {self.cpu_usage}%")
        print(f"Memory Usage: {self.memory_usage}%")
        print(f"Disk Usage: {self.disk_usage}%")

    def optimize_performance(self):
        print("Optimizing server performance...")
        if self.cpu_usage > 80 or self.memory_usage > 80 or self.disk_usage > 80:
            print("Server performance optimized.")
            if self.sdn_controller:
                self.sdn_controller.handle_server_optimization()
        else:
            print("Server performance within acceptable limits.")

    def handle_server_fault(self, fault_event):
        print(f"Handling server fault: {fault_event}")
        if self.sdn_controller:
            self.sdn_controller.handle_server_fault_event(fault_event)
        # Placeholder server fault handling logic
