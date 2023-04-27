class Monitor:
    monitor_counter = 0
    def __init__(self, brand, size):
        Monitor.monitor_counter += 1
        self.__id_monitor: int = Monitor.monitor_counter
        self.__brand: str = brand
        self.__size: str = size 
    
    @property
    def id_monitor(self):
        return self.__id_monitor
    
    @id_monitor.setter
    def id_monitor(self, id_monitor):
        self.__id_monitor = id_monitor
    
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def id_monitor(self, size):
        self.__size = size
    
    def __str__(self):
        return f"Monitor ID: {self.__id_monitor} Monitor Brand: {self.brand} Monitor Size: {self.size}''"

if __name__ == '__main__':
    monitor1 = Monitor('HP', 42)
    print(monitor1)

    monitor2 = Monitor('Acer', 45)
    print(monitor2)