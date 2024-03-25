# Class representing an ugly woman (adaptee)
class UglyWoman:
    def look_ugly(self):
        return "Ugly woman"


# Adapter class (makeup)
class MakeupAdapter:
    def __init__(self, ugly_woman, beautiful_women):
        self._ugly_woman = ugly_woman
        self._beautiful_women = beautiful_women

    def look_beautiful(self):
        # Using the adaptee method with added makeup
        return f"{self._ugly_woman.look_ugly()} ===> {self._beautiful_women.look_beautiful()}"


# Target class representing a beautiful woman
class BeautifulWoman:
    def look_beautiful(self):
        return "Beautiful woman"


# Helper function to check the appearance
def check_appearance(woman):
    print(woman.look_beautiful())


# Create an instance of an ugly woman
ugly_woman = UglyWoman()
beautiful_women = BeautifulWoman()

# Create an adapter with the ugly woman as adaptee
makeup_adapter = MakeupAdapter(ugly_woman, beautiful_women)

# # Create an instance of a beautiful woman as the target
# beautiful_woman = BeautifulWoman()

# Call the check_appearance function using the adapter
check_appearance(makeup_adapter)
