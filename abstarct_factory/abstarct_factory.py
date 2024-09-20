from abc import ABC, abstractmethod

# 1. کلاس‌های انتزاعی خودروها

class SUV(ABC):
    @abstractmethod
    def create_suv(self):
        pass

class Coupe(ABC):
    @abstractmethod
    def create_coupe(self):
        pass


# 2. کلاس انتزاعی کارخانه

class CarFactory(ABC):
    @abstractmethod
    def create_suv(self) -> SUV:
        pass
    
    @abstractmethod
    def create_coupe(self) -> Coupe:
        pass


# 3. پیاده‌سازی کارخانه Benz

class BenzSUV(SUV):
    def create_suv(self):
        return "Benz SUV Created"

class BenzCoupe(Coupe):
    def create_coupe(self):
        return "Benz Coupe Created"

class BenzFactory(CarFactory):
    def create_suv(self) -> BenzSUV:
        return BenzSUV()
    
    def create_coupe(self) -> BenzCoupe:
        return BenzCoupe()


# 3. پیاده‌سازی کارخانه Bmw

class BmwSUV(SUV):
    def create_suv(self):
        return "Bmw SUV Created"

class BmwCoupe(Coupe):
    def create_coupe(self):
        return "Bmw Coupe Created"

class BmwFactory(CarFactory):
    def create_suv(self) -> BmwSUV:
        return BmwSUV()
    
    def create_coupe(self) -> BmwCoupe:
        return BmwCoupe()


# 4. کلاس مشتری برای مدیریت خودروها

class CarManager:
    def __init__(self, factory: CarFactory):
        self.factory = factory
    
    def build_suv(self):
        suv = self.factory.create_suv()
        print(suv.create_suv())
    
    def build_coupe(self):
        coupe = self.factory.create_coupe()
        print(coupe.create_coupe())


# 5. تست سیستم

benz_factory = BenzFactory()
bmw_factory = BmwFactory()

# مدیریت خودروهای Benz
car_manager = CarManager(benz_factory)
car_manager.build_suv()   # خروجی: Benz SUV Created
car_manager.build_coupe()  # خروجی: Benz Coupe Created

# مدیریت خودروهای Bmw
car_manager = CarManager(bmw_factory)
car_manager.build_suv()   # خروجی: Bmw SUV Created
car_manager.build_coupe()  # خروجی: Bmw Coupe Created
