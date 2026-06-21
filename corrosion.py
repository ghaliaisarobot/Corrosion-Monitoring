class CorrosionMonitor:

    def __init__(self, humidity, temperature, ph):
        self.humidity = humidity
        self.temperature = temperature
        self.ph = ph

    def calculate_risk_score(self):
        score = 0

        if self.humidity > 70:
            score += 40

        if self.temperature > 35:
            score += 30

        if self.ph < 5:
            score += 30

        return score

    def classify_risk(self):
        score = self.calculate_risk_score()

        if score >= 70:
            return "High Risk"

        elif score >= 40:
            return "Moderate Risk"

        else:
            return "Low Risk"

    def display_report(self):
        print("\n===== Corrosion Monitoring Report =====")
        print(f"Humidity: {self.humidity}%")
        print(f"Temperature: {self.temperature} °C")
        print(f"pH: {self.ph}")
        print(f"Risk Level: {self.classify_risk()}")


humidity = float(input("Enter humidity (%): "))
temperature = float(input("Enter temperature (°C): "))
ph = float(input("Enter pH value: "))

monitor = CorrosionMonitor(humidity, temperature, ph)

monitor.display_report()