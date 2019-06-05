from sqlalchemy import Enum

class PrescriptionType(Enum):
    Single_Vision = 1
    Multifocal_Lenses = 2
    Bifocal = 3
    Progressive = 4
    Computer_Glasses = 5
    Reading = 6

