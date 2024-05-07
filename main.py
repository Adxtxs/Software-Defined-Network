from controller import SDNController
from server import Server
from network import Network, Switch, Link, TrafficManager
from external_apps import ExternalApps
from event_manager import EventManager

def get_user_input():
    devices_input = input("Enter network devices (comma-separated): ").strip()
    devices = [device.strip() for device in devices_input.split(',') if device.strip()]
    return devices

def main():
    # Instantiate controller, server, network components, and external apps
    controller = SDNController()
    server = Server()
    switch = Switch()
    link = Link()
    traffic_manager = TrafficManager()
    external_apps = ExternalApps()
    event_manager = EventManager()

    # Get user input for network devices
    devices = get_user_input()

    if not devices:
        print("No network devices provided. Exiting.")
        return

    # Instantiate network with user input
    network_obj = Network(devices=devices)

    # Get user input for server performance metrics
    cpu_usage = int(input("Enter CPU usage (%): "))
    memory_usage = int(input("Enter memory usage (%): "))
    disk_usage = int(input("Enter disk usage (%): "))

    # Monitor server performance with user input metrics
    server.monitor_performance(cpu_usage, memory_usage, disk_usage)

    # Simulate network events
    event_manager.add_event("Event1")
    event_manager.add_event("Event2")
    event_manager.process_events()

    # Perform simulated actions
    controller.manage_events()
    controller.optimize_network(network_obj)
    controller.configure_routing(network_obj)
    server.optimize_performance()
    switch.configure_switch()
    link.monitor_link_status()
    traffic_manager.manage_traffic()
    external_apps.add_app("FileExplorer")
    external_apps.execute_app("VideoEditor")

if __name__ == "__main__":
    main()
