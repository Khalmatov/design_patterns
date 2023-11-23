from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        pass


class Subject(ABC):

    def register_observer(self, o: Observer):
        pass

    def remove_observer(self, o: Observer):
        pass

    def notify_observers(self):
        pass


class WeatherData(Subject):
    observers: list[Observer]
    temperature: float
    humidity: float
    pressure: float

    def __init__(self):
        self.observers = []

    def register_observer(self, o: Observer):
        self.observers.append(o)

    def remove_observer(self, o: Observer):
        self.observers.remove(o)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(temp=self.temperature, humidity=self.humidity, pressure=self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurements_changed()


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class StatisticsDisplay(Observer, DisplayElement):
    max_temp = 0
    min_temp = 200
    temp_sum = 0
    num_readings = 0
    weather_data: WeatherData

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temp_sum += temp
        self.num_readings += 1

        if temp > self.max_temp:
            self.max_temp = temp

        if temp < self.min_temp:
            self.min_temp = temp

        self.display()

    def display(self):
        print(f'Avg/Max/Min temperature = {self.temp_sum / self.num_readings}/{self.max_temp}/{self.min_temp}')


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f'Current conditions: {self.temperature}F degrees and {self.humidity}% humidity')


class ForecastDisplay(Observer, DisplayElement):
    current_pressure = 29.92
    last_pressure: float
    weather_data = WeatherData

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast:", end=' ')
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same")
        elif self.current_pressure < self.last_pressure:
            print("Watch out for cooler, rainy weather!")


def main():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)


if __name__ == '__main__':
    main()
